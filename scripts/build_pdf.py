from reportlab.lib.pagesizes import letter
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                Table, TableStyle, PageBreak, Flowable, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, white
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT

GF = "/usr/share/fonts/truetype/google-fonts/"
CX = "/usr/share/fonts/truetype/crosextra/"
pdfmetrics.registerFont(TTFont("Pop", GF + "Poppins-Regular.ttf"))
pdfmetrics.registerFont(TTFont("PopM", GF + "Poppins-Medium.ttf"))
pdfmetrics.registerFont(TTFont("PopB", GF + "Poppins-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Body", CX + "Carlito-Regular.ttf"))
pdfmetrics.registerFont(TTFont("BodyB", CX + "Carlito-Bold.ttf"))
pdfmetrics.registerFont(TTFont("BodyI", CX + "Carlito-Italic.ttf"))
pdfmetrics.registerFont(TTFont("BodyBI", CX + "Carlito-BoldItalic.ttf"))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily("Body", normal="Body", bold="BodyB", italic="BodyI", boldItalic="BodyBI")

INK = HexColor("#1B2A33")
MUTED = HexColor("#5B6B75")
TEAL = HexColor("#0F5C63")
TEAL_L = HexColor("#E6F0F0")
AMBER = HexColor("#C8862A")
AMBER_L = HexColor("#FBF1E2")
RULE = HexColor("#D5DEE0")

W, H = letter
M = 18 * mm

s_h1 = ParagraphStyle("h1", fontName="PopB", fontSize=20, leading=24, textColor=INK)
s_sub = ParagraphStyle("sub", fontName="Pop", fontSize=10, leading=14, textColor=MUTED)
s_h2 = ParagraphStyle("h2", fontName="PopB", fontSize=12, leading=15, textColor=TEAL,
                      spaceBefore=9, spaceAfter=4)
s_body = ParagraphStyle("body", fontName="Body", fontSize=10.5, leading=14, textColor=INK)
s_bul = ParagraphStyle("bul", parent=s_body, leftIndent=11, bulletIndent=0, spaceAfter=2.5)
s_small = ParagraphStyle("small", parent=s_body, fontSize=8.6, leading=11, textColor=MUTED)
s_cell = ParagraphStyle("cell", parent=s_body, fontSize=9.2, leading=11.6)
s_cellb = ParagraphStyle("cellb", parent=s_cell, fontName="BodyB")
s_head = ParagraphStyle("head", parent=s_cell, fontName="PopM", fontSize=8.6, textColor=white)
s_callout = ParagraphStyle("callout", parent=s_body, fontSize=10.5, leading=14)


def P(t, s=s_body):
    return Paragraph(t, s)


def bullets(items, style=s_bul):
    return [Paragraph(i, style, bulletText="•") for i in items]


class Callout(Flowable):
    """Bloque con barra lateral de color."""
    def __init__(self, paras, bar=AMBER, bg=AMBER_L, width=None, pad=7):
        super().__init__()
        self.paras, self.bar, self.bg, self.pad = paras, bar, bg, pad
        self._w = width

    def wrap(self, aw, ah):
        self.w = self._w or aw
        inner = self.w - 2 * self.pad - 4
        self.hs = [p.wrap(inner, ah)[1] for p in self.paras]
        self.h = sum(self.hs) + 2 * self.pad + 3 * (len(self.paras) - 1)
        return self.w, self.h

    def draw(self):
        c = self.canv
        c.setFillColor(self.bg)
        c.roundRect(0, 0, self.w, self.h, 3, stroke=0, fill=1)
        c.setFillColor(self.bar)
        c.rect(0, 0, 4, self.h, stroke=0, fill=1)
        y = self.h - self.pad
        for p, h in zip(self.paras, self.hs):
            y -= h
            p.drawOn(c, 4 + self.pad, y)
            y -= 3


class Flow(Flowable):
    """Esquema del sistema: tarja -> trampa -> cartucho -> drenaje, y salida de aceite."""
    def __init__(self, width, height=150):
        super().__init__()
        self.width, self.height = width, height

    def wrap(self, aw, ah):
        return self.width, self.height

    def box(self, x, y, w, h, title, sub, fill, fg=INK, border=None):
        c = self.canv
        c.setFillColor(fill)
        c.setStrokeColor(border or fill)
        c.setLineWidth(1)
        c.roundRect(x, y, w, h, 5, stroke=1 if border else 0, fill=1)
        c.setFillColor(fg)
        c.setFont("PopB", 8.8)
        c.drawCentredString(x + w / 2, y + h - 15, title)
        c.setFont("Body", 8.4)
        for i, line in enumerate(sub):
            c.drawCentredString(x + w / 2, y + h - 28 - i * 10, line)

    def arrow(self, x1, y1, x2, y2, col=TEAL):
        c = self.canv
        c.setStrokeColor(col)
        c.setFillColor(col)
        c.setLineWidth(1.6)
        c.line(x1, y1, x2, y2)
        import math
        a = math.atan2(y2 - y1, x2 - x1)
        L = 6
        p = c.beginPath()
        p.moveTo(x2, y2)
        p.lineTo(x2 - L * math.cos(a - 0.45), y2 - L * math.sin(a - 0.45))
        p.lineTo(x2 - L * math.cos(a + 0.45), y2 - L * math.sin(a + 0.45))
        p.close()
        c.drawPath(p, stroke=0, fill=1)

    def draw(self):
        c = self.canv
        n, gap = 4, 16
        bw = (self.width - gap * (n - 1)) / n
        bh = 64
        y = self.height - bh - 4
        boxes = [
            ("1. Tarja y coladera", ["Agua de lavado con", "aceite y detergente;", "la coladera retiene sólidos"], TEAL_L, INK, None),
            ("2. Trampa de grasa", ["Tanque de unos 10 L:", "el agua reposa y el", "aceite libre flota"], TEAL_L, INK, None),
            ("3. Cartucho", ["Sorbente hidrofóbico de", "unicel reciclado y", "transformado"], TEAL, white, None),
            ("4. Drenaje", ["Sale el agua con", "mucho menos aceite"], TEAL_L, INK, None),
        ]
        xs = []
        for i, (t, sub, f, fg, b) in enumerate(boxes):
            x = i * (bw + gap)
            xs.append(x)
            self.box(x, y, bw, bh, t, sub, f, fg, b)
            if i:
                self.arrow(x - gap + 2, y + bh / 2, x - 2, y + bh / 2)
        # salida de aceite
        ox = xs[1]
        ow = xs[2] + bw - ox
        oy = 4
        oh = 46
        c.setFillColor(AMBER_L)
        c.setStrokeColor(AMBER)
        c.setLineWidth(1)
        c.roundRect(ox, oy, ow, oh, 5, stroke=1, fill=1)
        c.setFillColor(INK)
        c.setFont("PopB", 8.8)
        c.drawCentredString(ox + ow / 2, oy + oh - 15, "Aceite recuperado: frasco y entrega a un acopiador")
        c.setFont("Body", 8.4)
        c.drawCentredString(ox + ow / 2, oy + oh - 28, "La trampa se vacía y el sorbente se regenera periódicamente.")
        c.drawCentredString(ox + ow / 2, oy + oh - 38, "El acopiador decide la ruta (biodiésel u otra). Nunca a jabón.")
        self.arrow(xs[1] + bw / 2, y - 2, xs[1] + bw / 2, oy + oh + 2, AMBER)
        self.arrow(xs[2] + bw / 2, y - 2, xs[2] + bw / 2, oy + oh + 2, AMBER)


def table(rows, widths, header_bg=TEAL, zebra=True):
    data = [[P(c, s_head) for c in rows[0]]]
    for r in rows[1:]:
        data.append([P(r[0], s_cellb)] + [P(c, s_cell) for c in r[1:]])
    t = Table(data, colWidths=widths, repeatRows=1)
    st = [
        ("BACKGROUND", (0, 0), (-1, 0), header_bg),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 1), (-1, -1), 0.5, RULE),
    ]
    if zebra:
        for i in range(1, len(data)):
            if i % 2 == 0:
                st.append(("BACKGROUND", (0, i), (-1, i), HexColor("#F5F8F8")))
    t.setStyle(TableStyle(st))
    return t


def on_page(c, doc):
    c.saveState()
    c.setFillColor(TEAL)
    c.rect(0, H - 9 * mm, W, 9 * mm, stroke=0, fill=1)
    c.setFillColor(AMBER)
    c.rect(0, H - 9 * mm - 1.4, W, 1.4, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("PopM", 8)
    c.drawString(M, H - 6 * mm, "Equipo Oilx-Force  ·  Rally 2026  ·  Desafío: reutilización de aceite doméstico")
    c.drawRightString(W - M, H - 6 * mm, "16 de octubre de 2026")
    c.setFillColor(MUTED)
    c.setFont("Body", 8)
    c.drawString(M, 10 * mm, "Documento de trabajo para revisión técnica  ·  Equipo Oilx-Force")
    c.drawRightString(W - M, 10 * mm, f"{doc.page} / 3")
    c.restoreState()


doc = BaseDocTemplate("/home/claude/out/Propuesta_OilxForce_Dra_Dulce.pdf", pagesize=letter,
                      leftMargin=M, rightMargin=M, topMargin=16 * mm, bottomMargin=16 * mm,
                      title="Filtro de aceite para tarja con unicel reciclado: propuesta para asesoría técnica",
                      author="Equipo Oilx-Force", subject="Rally 2026, reutilización de aceite doméstico")
frame = Frame(M, 15 * mm, W - 2 * M, H - 16 * mm - 15 * mm, id="f", leftPadding=0, rightPadding=0,
              topPadding=0, bottomPadding=0)
doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=on_page)])
CW = W - 2 * M

story = []

# ---------------- PÁGINA 1 ----------------
story += [
    Spacer(1, 4),
    P("Filtro de aceite para tarja con unicel reciclado", s_h1),
    Spacer(1, 3),
    P("Propuesta del equipo Oilx-Force para la Dra. Dulce María González García, "
      "nuestra asesora en la parte técnica del proyecto", s_sub),
    Spacer(1, 9),
    Callout([
        P("<b>En una frase.</b> Queremos atrapar en casa el aceite de cocina que hoy se va por la tarja, "
          "con un filtro hecho de unicel reciclado, y entregar ese aceite a quien lo aproveche. "
          "La idea del material y de la columna empacada es suya; el equipo se encarga de la investigación, "
          "el diseño del sistema y la redacción. Le pedimos su revisión técnica antes de presentarlo.", s_callout)
    ]),
    P("El problema", s_h2),
]
story += bullets([
    "Al lavar trastes, parte del aceite se va por la coladera sin que nadie lo note. Al enfriarse se pega a las "
    "tuberías, forma tapones y provoca encharcamientos, sobre todo en temporada de lluvias.",
    "Destapar un drenaje cuesta entre 4,400 y 12,000 pesos, y en la Ciudad de México tirar aceite al drenaje "
    "es una falta que se multa (norma NADF-012).",
    "El aceite de fritura en botella ya tiene programas de acopio. El que se mezcla con agua y detergente "
    "en la tarja no tiene ninguna ruta, y nadie lo recupera. Ese es el aceite que queremos atrapar.",
    "Alcance: hogares y fondas. Los restaurantes quedan fuera porque ya están regulados.",
])
story += [
    P("Nuestra propuesta", s_h2),
    P("Un sistema de dos etapas que se instala bajo la tarja, como los filtros de agua domésticos:", s_body),
    Spacer(1, 6),
    Flow(CW, 158),
    Spacer(1, 4),
    P("Lo que su orientación cambió", s_h2),
]
story += bullets([
    "<b>Polímero hidrofóbico, no hidrofílico.</b> El polímero que absorbe agua (acrilato de sodio) se sustituye por "
    "uno que repele el agua y atrapa el aceite por afinidad química, no por tamizado.",
    "<b>Columna empacada.</b> El sorbente va empacado como en un filtro de agua, en tubería casera o en drenajes de empresas.",
    "<b>Unicel transformado.</b> El unicel de vasos y empaques no se puede reexpandir, pero sí disolver y convertir en "
    "esferas, mallas o aerogeles. Así el filtro limpia aceite y además recicla un residuo.",
    "<b>Cómo presentarlo.</b> Como una nueva aplicación de un material conocido, que es lo que podemos defender.",
])

story.append(PageBreak())

# ---------------- PÁGINA 2 ----------------
story += [
    P("Qué ya existe", s_h2),
    P("Revisamos patentes y proyectos para saber qué es nuevo y qué no. El material ya está publicado; "
      "no encontramos un filtro doméstico de tarja con unicel reciclado y entrega del aceite a un acopiador.", s_body),
    Spacer(1, 6),
    P("<b>Patentes similares</b>", s_body),
    Spacer(1, 3),
    table([
        ["Patente", "Titular y país", "Qué protege", "Qué nos dice"],
        ["US 4,022,694 (1977)", "Hydronautics Inc., EE.UU.",
         "Separador agua-aceite: el agua pasa por un bloque de espuma de poliuretano que se exprime con un pistón para sacar el aceite y reusarlo.",
         "La columna con espuma que se regenera exprimiéndola existe desde los años 70. Ya expiró."],
        ["MX2012013514A (2013)", "BASF SE, Alemania (solicitud en México)",
         "Esponjas de poliuretano que absorben aceite y tienen buena resistencia mecánica.",
         "Antecedente directo en México. No verificamos si está vigente."],
        ["US 11,065,602 (2021)", "University of South Africa, Sudáfrica",
         "Nanofibras de poliestireno expandido que adsorben crudo del agua; se regeneran lavándolas con un solvente (hexano).",
         "Lo más parecido a su propuesta: unicel en fibras como sorbente, en tanque, para petróleo. Aparece como activa."],
        ["US 2023/0183602 (solicitud)", "M. F. McCarthy, EE.UU.",
         "Bolsas porosas con material absorbente (turba, cáscara de naranja, polipropileno) a la entrada y salida de una trampa de grasa; la grasa se usa como combustible.",
         "Trampa de grasa con absorbente y salida energética ya está solicitada, pero con otros materiales."],
    ], [30 * mm, 33 * mm, 60 * mm, CW - 123 * mm]),
    Spacer(1, 9),
    P("<b>Proyectos y estudios en otros países</b>", s_body),
    Spacer(1, 3),
    table([
        ["Proyecto", "Dónde", "Qué hicieron", "Relevancia"],
        ["Fibras de unicel de desecho", "Instituto de Tecnología de Izmir, Turquía (2018)",
         "Disolvieron unicel y lo electrohilaron en mallas; absorbieron mucho aceite en aguas aceitosas.",
         "Respalda el camino de solubilizar y electrohilar que usted propone."],
        ["Microfibras con centrífuga", "Filipinas (2021)",
         "Hicieron fibras de unicel de desecho con una centrífuga de laboratorio adaptada.",
         "Vía de fabricación más sencilla que el electrohilado."],
        ["Esferas de coco con unicel", "IPICYT, México (2024)",
         "Esferas de fibra de coco recubiertas con unicel disuelto; se reusaron 10 ciclos.",
         "Antecedente mexicano y de forma esférica, como las del audio."],
        ["Smart Sponge", "City University, Hong Kong (2022-2023)",
         "Esponja con recubrimiento que absorbe aceite y repele agua; se reusa más de 100 veces. Medalla de plata en Ginebra 2022.",
         "Lista la limpieza de grasa doméstica entre sus usos."],
        ["Oleo Sponge", "Argonne National Laboratory, EE.UU.",
         "Espuma de poliuretano tratada que atrapa aceite dentro y fuera del agua; patentada y reutilizable.",
         "Muestra que la espuma modificada ya tiene dueño."],
        ["OLEOTRAP", "Universiti Teknologi MARA, Malasia",
         "Filtro para desagües domésticos con una capa de fibras de queratina que adsorbe aceite.",
         "La idea de filtro casero de aceite ya se exploró con otro material."],
    ], [32 * mm, 37 * mm, 58 * mm, CW - 127 * mm]),
    Spacer(1, 9),
    Callout([
        P("<b>Qué nos distingue.</b> No el material, sino la combinación: un filtro bajo la tarja para hogares y fondas, "
          "con trampa de grasa, un cartucho de unicel posconsumo mexicano que se regenera, y entrega del aceite a un acopiador. "
          "Tampoco encontramos estudios con aceite de cocina usado, detergente de trastes real y el flujo de una tarja; "
          "eso es lo que falta probar.", s_callout)
    ], bar=TEAL, bg=TEAL_L),
]

story.append(PageBreak())

# ---------------- PÁGINA 3 ----------------
story += [
    P("Lo que necesitamos de usted", s_h2),
    P("Cinco preguntas, ordenadas por cuánto cambiarían el proyecto si la respuesta fuera negativa:", s_body),
    Spacer(1, 3),
]
qs = [
    "<b>Forma del sorbente.</b> ¿Qué recomienda para empacar en una tubería: esferas, mallas cortadas o aerogeles? "
    "¿Resistirían el flujo sin compactarse ni soltar fibras?",
    "<b>Fabricación.</b> ¿Hay en el IPN equipo o un grupo que pueda disolver y electrohilar (o hilar por centrifugado) unicel reciclado? "
    "¿Qué solventes usaría y cómo se manejarían de forma segura?",
    "<b>Regeneración.</b> ¿El sorbente se exprime en frío para sacar el aceite o conviene cambiarlo cuando se sature? "
    "¿Cuántos usos serían realistas con aceite de cocina usado?",
    "<b>Detergente y aceite recuperado.</b> ¿El sorbente seguiría atrapando aceite con el jabón de trastes? "
    "Y como el biodiésel disuelve el poliestireno, ¿cómo evitamos que pasen fibras al aceite que entregamos?",
    "<b>Alternativa.</b> ¿Conviene mantener la espuma de poliuretano reciclada como plan B? Tiene más evidencia de reúso, "
    "y su experiencia en poliuretanos nos ayudaría a decidir.",
]
story += [Paragraph(q, s_bul, bulletText=f"{i}.") for i, q in enumerate(qs, 1)]
story += [
    Spacer(1, 2),
    P("Y una petición aparte: ¿nos autoriza a mencionar su asesoría en el reporte, y de qué forma?", s_body),
    P("Prueba sencilla que proponemos", s_h2),
    P("Antes de presentar el proyecto queremos datos propios. Proponemos una prueba de una hora con balanza de cocina: "
      "mezclar agua, aceite de cocina usado y detergente; sumergir cada material, escurrirlo y pesarlo; exprimirlo y medir "
      "cuánto aceite suelta; repetir cinco veces. Compararíamos unicel en trozos, espuma de poliuretano y, si el laboratorio "
      "nos facilita una muestra, unicel transformado en malla. El material pasa si absorbe bastante más aceite que agua, "
      "suelta la mayor parte al exprimirlo, conserva su capacidad tras cinco usos y casi no suelta fragmentos. "
      "Le pedimos que nos diga si la prueba es razonable o cómo mejorarla.", s_body),
    P("Qué afirmamos y qué no", s_h2),
]
two = Table([
    [P("<b>Sí afirmamos</b>", ParagraphStyle("a", parent=s_cell, textColor=TEAL, fontName="BodyB")),
     P("<b>No afirmamos todavía</b>", ParagraphStyle("b", parent=s_cell, textColor=AMBER, fontName="BodyB"))],
    [[Paragraph(t, ParagraphStyle("c", parent=s_cell, leftIndent=9, bulletIndent=0, spaceAfter=2), bulletText="•") for t in [
        "El unicel reciclado y transformado en fibras absorbe aceite en laboratorio.",
        "El unicel en trozos no suelta el aceite; por eso hay que transformarlo.",
        "La espuma de poliuretano modificada se exprime y se reusa muchas veces.",
        "Lo nuevo es la integración del sistema, no el material.",
    ]],
     [Paragraph(t, ParagraphStyle("d", parent=s_cell, leftIndent=9, bulletIndent=0, spaceAfter=2), bulletText="•") for t in [
        "Que funcione con aceite usado, detergente y el flujo de una tarja.",
        "Que las mallas aguanten el exprimido o un empaque en tubería.",
        "Que el aceite recuperado sirva para biodiésel: lo decide el acopiador.",
        "Que usted respalde el proyecto, sin su autorización.",
    ]]],
], colWidths=[CW / 2 - 4, CW / 2 - 4], hAlign="LEFT")
two.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BACKGROUND", (0, 0), (0, -1), TEAL_L),
    ("BACKGROUND", (1, 0), (1, -1), AMBER_L),
    ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
    ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("LINEAFTER", (0, 0), (0, -1), 4, white),
]))
story += [two]
story += [
    P("Siguientes pasos", s_h2),
]
story += bullets([
    "Recibir sus comentarios y ajustar el material, la forma del sorbente y la prueba.",
    "Hacer la prueba de una hora y registrar los resultados.",
    "Consultar a un acopiador de aceite usado si acepta el aceite de la trampa y en qué condiciones.",
    "Redactar el reporte del Rally con lo que se confirme y declarar lo que siga pendiente.",
])
story += [
    Spacer(1, 6),
    P("<b>Fuentes principales.</b> Patentes: US 4,022,694 (Google Patents); MX2012013514A (Google Patents); US 11,065,602 "
      "(Google Patents); US 2023/0183602 (Justia). Estudios: Isık y Demir, <i>Sustainable Materials and Technologies</i>, 2018; "
      "Budlayan et al., <i>Journal of Engineering and Applied Science</i> 68, 2021; Alvarado-Gómez et al., IPICYT, 2024; "
      "Akanbi, tesis UCL, 2018 (fragilidad de las mallas). Proyectos: Smart Sponge (CityU Hong Kong); Oleo Sponge (Argonne); "
      "OLEOTRAP (repositorio UiTM). Costos y norma: Expansión; NADF-012-AMBT-2015. Las fuentes se consultaron en "
      "resumen o ficha; los detalles completos están en nuestra consulta técnica ampliada.", s_small),
]

doc.build(story)
print("ok")
