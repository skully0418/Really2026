# Contexto del proyecto reto aceite usado: estado, hipótesis, datos y faltantes (corte 16 oct 2026)

> **Actualización 17 oct 2026:** el poliuretano (PU) se descartó por precio; el material vigente es la malla de poliestireno de unicel reciclado y la ruta del aceite es la epoxidación. Lo que este documento dice del PU queda como historial. Estado actual en `CLAUDE.md`.


Oct 16, 2026 · @Alejandro

## Estado actual

La propuesta vigente es un sistema de dos etapas bajo la tarja (trampa de grasa con tanque de retención y un cartucho de pulido de espuma de poliuretano reciclada e hidrofobizada, que se exprime en frío) con el aceite recuperado entregado a un acopiador de biodiésel, y es una hipótesis: la espuma de PU tiene respaldo de laboratorio con aceites minerales, pero nadie la ha medido con aceite de cocina usado, detergente real y caudal de tarja. El aceite de fritura recién usado sigue yendo a botella, que es la ruta principal. El aceite recuperado se clasifica por acidez, agua y sólidos; el de trampa y cartucho se trata como de acidez alta hasta medirlo, y la ruta final la decide el acopiador (preguntas en "Por consultar con el acopiador").

Se descartaron, en este orden: el cartucho de polipropileno (retiene poco frente al aceite que genera un hogar), el jabón como tercera salida, el bio-recubrimiento de fertilizante (por consejo de una doctora en polímeros del IPN: más investigación y más costo) y la columna de unicel (no hay datos de que el aceite se recupere de él). Lo que falta medir está en la sección "Datos que no tenemos"; el más importante es qué fracción del aceite de un hogar baja realmente por la tarja, porque de ese número depende el tamaño del cartucho.

## El reto, el alcance y el plazo

El reto pide reutilizar aceite vegetal doméstico usado para generar energías limpias u otros subproductos. El equipo lo acotó a hogares y negocios informales (fondas, puestos); los restaurantes quedan fuera porque ya están regulados. El plazo es de menos de un día, no habrá pruebas propias, y se necesita la planeación completa con los caveats resueltos. Se evalúan cinco puntos:

| Punto | Qué se evalúa | Estado hoy |
| --- | --- | --- |
| 1. Problemática | Causas y problema real | Cubierto: el aceite obstruye tuberías (desazolve de MXN 4,400 a 12,000 según Expansión) y contamina el agua ("1 L contamina más de 40 mil L", cifra divulgativa). Falta la fracción que baja por la tarja |
| 2. Producto o servicio | Qué se ofrece y por qué es solución | Hipótesis: trampa más cartucho de PU regenerable, con acopio a biodiésel |
| 3. Impacto social y ambiental | Qué cambia y cuánto | Demanda de oxígeno evitada: 2.66 kg de O₂ por litro de aceite (teórico, trioleina), multiplicada por los litros que el sistema realmente retenga (hasta 77 % en el único dato con detergente) |
| 4. Innovación | Qué es nuevo | La integración de trampa, cartucho regenerable y circuito a biodiésel; el material no es nuevo (hay una solicitud de BASF y una esponja de Hong Kong) |
| 5. Sostenibilidad, presupuesto y aceptación | Costos y viabilidad social | Sin precios verificados; la participación de referencia es 20.9 % (Tesalónica) y el cartucho se reutiliza |

## Historial de decisiones

Las rutas se descartaron en este orden. Cada una dejó algo que la siguiente aprovecha.

| Orden | Ruta | Por qué se descartó o cambió | Qué se conserva |
| --- | --- | --- | --- |
| 1 | Combustible y fertilizante (Doc 2, 14 caveats) | Alcance demasiado amplio para un día; el fertilizante depende de una cifra de maíz (22 %) que es real pero con aceite de ricino y leída solo en el resumen | Ruta por índice de acidez (≤ 2 biodiésel alcalino, 2 a 20 esterificación ácida, > 20 codigestión); demanda de oxígeno 2.66 kg O₂/L |
| 2 | Cartucho de polipropileno bajo la tarja | El prototipo "De la coladera al surco" lo proponía, pero no había dato de captura con aceite de cocina | Idea de filtro bajo la tarja y subsección de trampa con Stokes en Doc 2 |
| 3 | Jabón | El aceite recuperado de la tarja no debe tener contacto con la piel | Regla: el aceite recuperado va solo a biodiésel |
| 4 | Biorrecubrimiento (epoxidación más MDI) | Requiere más investigación de resina y sube los costos (consejo de la Dra. del IPN) | Nada en el sistema vigente |
| 5 | Columna de poliestireno (unicel) | EPS es de celda cerrada, rígido, se aplasta y no devuelve el aceite (Naser); se fragiliza en aceite (Guazzotti); el biodiésel disuelve PS; migra estireno | Dimensionamiento de columna (m\_PS = φ·V·ρ/(q·η)) y el argumento de reciclar un residuo contaminante |
| 6 | Trampa más cartucho de espuma de poliuretano (vigente) | Hipótesis; no hay prueba con aceite vegetal usado | Ver la sección siguiente |

La Dra. del IPN que orientó los cambios 4 y 5 no tiene publicaciones sobre poliestireno o aceite de cocina (trabaja en poli(éster-uretano)s biomédicos, híbridos con TiO₂ y geopolímeros en ESIQIE-IPN). Su respaldo es una opinión de consulta; la evidencia es de terceros, y su nombre solo se usará con su consentimiento expreso.

## Hipótesis vigente y sus parámetros

**Hipótesis.** Un sistema de dos etapas bajo la tarja retiene la mayor parte del aceite que hoy baja por el desagüe, y ese aceite se recupera sin calor para entregarlo a un acopiador de biodiésel. El aceite de freír sigue yendo a una botella (ruta principal); el sistema captura lo que se escapa.

- **Etapa 1, trampa de grasa compacta.** Tanque de retención de unos 10 L; separación por flotación a gravedad.
- **Etapa 2, cartucho de pulido.** Espuma flexible de poliuretano reciclada, hidrofobizada (ZnO más ácido hexadecanoico, según Rocha 2025), con *bypass*. Se exprime en frío cada semana en un frasco; el aceite se decanta y se entrega al acopiador.
- **Restricción.** El aceite recuperado no se usa para jabón ni para nada con contacto humano.
- **Novedad que se puede afirmar.** Solo la integración. La solicitud MX2012013514A (BASF SE; presentada el 18 may 2011, publicada el 24 ene 2013; estado legal sin verificar) y la esponja de Hong Kong ya existen.

**Etapa 1: por qué no basta sola.** La velocidad de ascenso de una gota es

```latex
v=\frac{\Delta\rho\, g\, d^{2}}{18\,\mu},\qquad \Delta\rho=78.2\ \mathrm{kg/m^3},\ \mu=1.002\ \mathrm{mPa\cdot s}
```

y para 0.20 m de profundidad el ascenso tarda 7.8 min con gotas de 100 µm, 31 min con 50 µm y 3.3 h con 20 µm. Con flujo continuo Q a través de un área A, el diámetro mínimo capturado es

```latex
d_c=\sqrt{\frac{18\,\mu\, Q}{\Delta\rho\, g\, A}}
```

A Q = 7 L/min y A = 0.06 m² resulta d\_c = 214 µm; capturar 100 µm exige A = 0.27 m². Las gotas emulsionadas de 5 a 20 µm (supuesto mío) no las separa la trampa; por eso existe la etapa 2.

**Etapa 2: capacidad del cartucho.**

```latex
m_{max}=q\,\rho_b\,V_c=9\ \tfrac{\mathrm{g}}{\mathrm{g}}\times 23\ \tfrac{\mathrm{g}}{\mathrm{L}}\times 1\ \mathrm{L}=207\ \mathrm{g}
```

con q ≈ 9 g/g para espuma tratada (cercano al 9.5 de Rocha); sin tratar, q = 3.2 g/g da 74 g. El tiempo de contacto (EBCT = V/Q) es el cuello de botella: Mari 2025 usó 0.33 L a 40 mL/min (8.25 min), mientras que 1 L a 7 L/min da 8.6 s, unas 58 veces menos. Una solución es un búfer de 10 L que drena a 0.2 L/min por el cartucho: 5 min de contacto y 50 min para vaciarse.

| Parámetro | Valor | Origen |
| --- | --- | --- |
| Δρ agua 20 °C y aceite | 78.2 kg/m³ | Cálculo (aceite 920 kg/m³) |
| Densidad aparente del PU | 23 g/L | Supuesto |
| q tratado | 9 g/g | Rocha 2025 (9.5 con aceite de motor); supuesto para aceite vegetal |
| q sin tratar | 3.2 g/g | RSC Adv 2024 (aceite vegetal) |
| Volumen del cartucho | 1 L | Diseño |
| Caudal de tarja | 7 L/min | Supuesto |
| Contacto objetivo | ≥ 5 min | Mari 2025 (8.25 min) |
| Retención con detergente | 77 % (techo observado) | Mari 2025, 20 mg/L de SDS |

## Aceite recolectado: tipo, uso y clasificación

El aceite no es una sola cosa. Su destino final (biodiésel, codigestión u otro) depende de tres variables medibles (acidez, agua y sólidos), y esas dependen del tipo de aceite, de cómo se usó y de cómo se almacenó o recuperó. Lo marcado **\[Consultar\]** debe confirmarlo el acopiador.

### a) Qué cambia las características

| Factor | Qué cambia | Efecto en el uso final |
| --- | --- | --- |
| Tipo de aceite base | Composición de ácidos grasos (índice de yodo, estabilidad, flujo en frío) | Soya y girasol, muy insaturados, dan biodiésel que se oxida más rápido. Palma y manteca, saturadas, dan peor flujo en frío. Un acopiador suele pagar lo mismo por mezclas, así que pesa menos que los otros dos factores **\[Consultar\]** |
| Cómo se usó (temperatura, número de usos, agua del alimento) | La hidrólisis sube la acidez; la oxidación genera compuestos polares; la polimerización sube la viscosidad | Más acidez obliga a pretratamiento; los polímeros no se convierten en éster y bajan el rendimiento |
| Cómo se almacenó o recuperó (agua, detergente, sólidos, tiempo) | Más agua, jabón, emulsión y, con el tiempo, más acidez | Es lo que más separa el aceite de botella del de trampa |

En México la producción de aceite vegetal es 65.6 % soya, ≈ 13 % palma, ≈ 8 % algodón, ≈ 4.5 % maíz y ≈ 3.6 % cártamo (Legiscomex, solo producción de 2014). No encontré consumo por tipo ni qué aceites usan hogares y fondas. Para la propuesta basta decir que predominan mezclas de aceite de soya, y que en fondas puede haber manteca y manteca vegetal de palma, que solidifican a temperatura ambiente y podrían tapar la espuma al exprimir (hipótesis).

### b) La acidez decide la ruta

La acidez se mide como índice de acidez, AV, en mg KOH/g. Con la masa molar del ácido oleico (282.5 g/mol) y la del KOH (56.1 g/mol):

```latex
\mathrm{FFA}\,[\%]=\frac{AV\cdot 282.5}{56.1\cdot 10}\approx 0.5035\,AV
```

Con Canakci y Van Gerpen (2001): AV 25.15 ≈ 12.7 % (reportan ≈ 12 %) y AV 66.08 ≈ 33 %. Cada gramo de aceite de acidez AV gasta AV mg de KOH en jabón antes de catalizar. Por kilo de aceite, el catalizador perdido es

```latex
m_{KOH,\,perdido}=AV\ \text{g/kg},\qquad m_{NaOH,\,perdido}=0.713\,AV\ \text{g/kg}
```

Con AV = 4 se pierden 4 g de KOH por kilo; con una dosis típica de 1 % (10 g/kg) es 40 % del catalizador convertido en jabón, de donde vienen las emulsiones y el rendimiento bajo. Medición: AV = 56.1·N·V/m, con N la normalidad del KOH, V los mL gastados y m los gramos de muestra (10 g con KOH 0.1 N y 3.6 mL dan AV ≈ 2.0).

| Acidez | Ruta | Respaldo |
| --- | --- | --- |
| AV ≤ 2 (FFA ≤ 1 %) | Transesterificación alcalina directa | Canakci cita ≤ 1 % FFA como límite; con KOH obtuvo mejor conversión con AV < 1 |
| 2 < AV ≤ 20 | Esterificación ácida (H₂SO₄ y metanol), luego alcalina | Grasa amarilla (AV 25.15) bajó a 0.74 a 1.64 en dos pasos y rindió 75 a 82 % |
| AV > 20 | Codigestión anaerobia, o esterificación intensiva si el acopiador la tiene **\[Consultar\]** | Grasa café (AV 66) necesitó 10 % de H₂SO₄ y metanol 20:1 y 40:1, y solo llegó a AV ≈ 2 con 56 a 75 % de rendimiento |

El corte de 20 es una decisión de diseño conservadora, no un límite químico: un acopiador con planta puede procesar AV 25 y hasta 66, pero a un costo que no tiene sentido para lotes de decenas de litros. El agua también limita: la esterificación produce agua, y en un estudio previo citado por Canakci la conversión cayó de 90.5 % a 58.8 % al subir el FFA de 5 % a 33 %.

### c) Qué esperar de cada flujo

Son hipótesis: no hay medición propia ni acidez medida del aceite doméstico mexicano.

| Flujo | Qué esperar | Ruta probable |
| --- | --- | --- |
| Aceite de freír en botella (hogar) | Pocos usos y poca agua, así que acidez baja (el rango típico lo recuerdo de memoria, sin fuente leída) | Alcalina directa si AV ≤ 2 después de filtrar |
| Aceite de freír de fonda | Más usos y más agua, con acidez más alta y a veces mezcla de grasas | Ácida y luego alcalina |
| Recuperado de trampa y cartucho | Mezclado con agua de lavado, detergente, sólidos de comida y días de reposo a temperatura ambiente. Los detergentes con álcali saponifican parte del aceite; la hidrólisis microbiana sube la acidez (hipótesis) | Tratarlo como grasa café hasta medirlo: codigestión o esterificación |

El único dato que apoya "grasa de trampa es grasa café" es una definición general (amarilla < 15 % FFA, café > 15 %, recolectada de hogares, restaurantes y plantas de tratamiento; De Gruyter 2017), no una medición de una trampa doméstica. **Consecuencia para la propuesta:** la promesa "el aceite de la trampa va a biodiésel" no tiene sustento hoy. Lo defendible es que el aceite de botella entra por AV y el de trampa y cartucho se entrega a un acopiador que decide la ruta.

### d) Respuesta modelo para la propuesta

> Los aceites que se recolectan son principalmente mezclas de aceite de soya y, en menor medida, canola, girasol, maíz o palma, usadas en fritura doméstica y en fondas. Sus características cambian con el número de usos, la temperatura, el agua del alimento y el tiempo de almacenamiento: aumentan los ácidos grasos libres, los compuestos polares y la viscosidad. Por eso cada lote se clasifica por índice de acidez (titulación con KOH), agua y sólidos visibles. Si AV ≤ 2 mg KOH/g va a transesterificación alcalina; entre 2 y 20, a esterificación ácida previa; arriba de 20, a codigestión anaerobia. El aceite de la trampa y el cartucho se considera, mientras no se mida, de acidez alta y se canaliza por la ruta de menor exigencia. El acopiador aliado define la ruta final de cada lote. No se destina a jabón ni a ningún uso con contacto humano.

### e) Qué registrar por lote

- Origen: botella de hogar, fonda o trampa y cartucho.
- Tipo de aceite declarado y número de usos aproximado.
- Alimentos fritos: con agua, empanizados, carne.
- Días almacenado y a qué temperatura.
- Acidez (titulación), agua (prueba de burbujeo en sartén como estimación) y sólidos.
- Color y olor.

## Datos de consumo, desperdicio y destino del aceite doméstico

**Aviso de calidad.** No encontré ningún dato mexicano que diga qué fracción del aceite doméstico usado baja por la tarja. Todo lo de abajo es proxy (otro país o nivel nacional) o cálculo mío; la columna "Tipo" lo marca. Las cifras no se pueden mezclar sin cuidado: unas son litros por hogar, otras por persona y otras totales nacionales.

### a) Cuánto aceite usado genera un hogar

| Dato | Valor | Tipo | Fuente |
| --- | --- | --- | --- |
| Aceite usado por persona | 3 a 4 kg/año | Proxy (reporte previo, vía Mena) | Reporte de investigación de la sesión |
| Hogar de 4 personas | 13 a 17 L/año (0.92 kg/L) | Cálculo mío | Derivado de la fila anterior |
| Misantla, Veracruz | 1.45 L en 2 meses para 5 personas; ≈ 24 mL/día; ≈ 8.7 L/año por hogar | México, muestra pequeña | Estudio de Misantla (recolección por separado) |
| México, volumen nacional (GISA 2022; no verifiqué si es consumo o aceite usado) | 320 millones de L/año; ≈ 2.5 L/persona | México, nacional | GISA 2022 |
| México, consumo (Mongabay 2021) | 1,280 millones de L/año, la mitad en hogares; ≈ 4.9 L/persona, ≈ 19.7 L por hogar de 4 | México, sin fuente primaria | Mongabay 2021 |
| España | ≈ 150 millones de L/año de aceite usado | Proxy | MITECO |
| Ciudad Valles, SLP | ≈ 83,776 L/año | México, solo establecimientos de comida | Estudio local |

**Corrección al valor de trabajo.** Las dos cifras nacionales de consumo difieren cuatro veces (320 contra 1,280 millones de L) y la de Mongabay es consumo de aceite, no aceite usado. Hay tres datos más de aceite *usado* por persona:

- Argentina 2022 (más de 3,000 encuestas, La Capital): consumo de 20.3 L/persona/año y descarte de fritura de ≈ 2.5 L/persona/año; 60 a 90 millones de L/año a nivel nacional. 53 % de los hogares nunca recupera el aceite.
- Guayaquil 2020 (441 hogares, LACCEI): 5.11 g/persona/día = 1.87 kg/año ≈ 2.0 L/persona/año (conversión mía con 0.92 kg/L).
- México (GISA 2022): ≈ 2.5 L/persona/año.

Con 2.0 a 2.5 L por persona y 3.56 personas por hogar (Censo 2020, cálculo mío: 125,514,839 / 35,219,141) salen 7.2 a 8.9 L por hogar al año; en CDMX (3.32 personas por hogar) salen 6.7 a 8.3 L. Misantla (8.7 L) coincide. Los 13 a 17 L de Mena (3 a 4 kg/persona) darían 12 a 15 L en un hogar mexicano promedio y quedan como extremo alto. **Valor de trabajo: 8 L por hogar al año (rango 6.7 a 15).** Los cálculos de abajo usaban 15 L antes de esta corrección y se rehicieron.

### b) A dónde va

| País o lugar | Muestra | Resultado | Tipo |
| --- | --- | --- | --- |
| Tesalónica, Grecia | n = 1,429 | 20.9 % recicla; entre los que no, 48.1 % lo vierte en la tarja y 22.3 % en el inodoro. Total: ≈ 38 % por la tarja y ≈ 56 % por algún desagüe | Proxy |
| Yaguará, Colombia | n = 363 | Desagüe 37 %, basura 32 %, suelo 15 %, alimento animal 13 %, reciclaje 2 % | Proxy |
| Mata de São João, Brasil | — | 85 % por la tarja | Proxy |
| CDMX, programa SEDEMA 2021 | — | 11,123 L acopiados ≈ 0.025 % del consumo doméstico | México, cálculo mío con cifra de consumo incierta |
| Mercados de Cuauhtémoc | — | ≈ 10 a 11 L/día por punto de acopio | México, punto de acopio |
| Monterrey | — | ≈ 50 L por centro en el primer mes | México, programa piloto |

Lectura honesta: el reciclaje formal en México es muy bajo (el 0.025 % es del orden de magnitud, no una medida), y los tres proxy ponen la fracción que va por el desagüe entre 37 % y 85 %. Eso está por encima de los escenarios de 10, 30 y 50 % que usábamos antes. Ojo: esos escenarios dependían de un programa de botella funcionando; la línea base sin programa es otra cantidad.

### c) Qué significa para el cartucho de 1 L

El aceite semanal que baja por la tarja es L × 1000 × 0.92 × φ / 52 (en gramos), con L los litros de aceite usado por hogar al año y φ la fracción que baja por la tarja. Se muestra el valor de trabajo (8 L) y el extremo alto (15 L). Porcentajes respecto a la capacidad de un cartucho de 1 L: 207 g tratado, 74 g sin tratar.

| φ | Origen del valor | 8 L: g/semana | % tratado | % sin tratar | 15 L: g/semana | % tratado | % sin tratar |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.37 | Yaguará / Tesalónica (tarja) | 52 | 25 % | 71 % | 98 | 47 % | 133 % |
| 0.557 | Tesalónica (cualquier desagüe) | 79 | 38 % | 107 % | 148 | 71 % | 200 % |
| 0.85 | Brasil | 120 | 58 % | 163 % | 226 | 109 % | 305 % |

Consecuencias:

- Con 8 L por hogar, el cartucho tratado de 1 L aguanta una semana con holgura (25 a 58 %). El sin tratar se llena o rebasa con φ ≥ 0.52 (74 g × 52 / (8,000 mL × 0.92)).
- Con 15 L, el sin tratar se satura en menos de una semana con cualquier φ y el tratado con φ ≥ 0.78.
- Por eso la hidrofobización no es opcional, y la trampa de 10 L y el exprimido semanal son parte del diseño: si el hogar no exprime a tiempo, el cartucho pasa a *bypass* y el aceite llega al drenaje.
- Los números suponen que el cartucho recibe todo lo que baja por la tarja. Con la etapa 1 recibe menos, pero no hay dato de cuánto, y con el techo de 77 % observado con detergente al menos 23 % del aceite emulsionado sigue su camino.

## Investigación encontrada: poliuretano y unicel

Todo es de laboratorio y casi todo con aceite mineral o crudo. Ningún estudio probado con aceite vegetal usado de cocina en una columna doméstica. Lo que se leyó completo y lo que solo se leyó en resumen se indica en la columna "Lectura".

### Poliuretano (PU)

| Estudio | Resultado | Aceite | Lectura |
| --- | --- | --- | --- |
| Rocha 2025 | PU de colchón con ZnO más ácido hexadecanoico: hasta 9.5 g/g en agua de mar; > 83 % retenido tras 30 min; 50 ciclos con prensa de tornillo | Motor 20W40 | Reporte |
| Hwang, Lee y Oh 2022 | PU con 20 % de lignina acetilada: conserva 97.9 % de la capacidad con aceite de oliva tras 50 ciclos; 92.3 % con crudo | Oliva, crudo | Reporte |
| JMSE 2022 | 17.1 g/g (aceite blanco) y 13.1 g/g (crudo) recuperados a 27.8 kN/m² en 50 ciclos | Blanco, crudo | Reporte |
| Mari 2025 (*Polymers* 17:1127) | Lecho fijo PU/grafeno de 260 × 40 mm a 40 mL/min: 77.15 % de retención de aceite emulsionado con 20 mg/L de SDS. El PU saturado se clasificó como residuo peligroso (Brasil) | Emulsión | Reporte |
| MRC/ASU 2025 | PU tratado con líquido iónico: 21.4 g/g de aceite y 2.7 g/g de agua | Aceite | Reporte |
| RSC Adv 2024 | PU sin tratar con aceite vegetal: 3.2 g/g | Vegetal | Reporte |
| Cossari 2026 | PU blando molido: 20 a 30 g/g | Aceite | Reporte |
| CityU "Smart Sponge" | Esponja comercial modificada (la página no dice que sea PU): 12 a 15 g/g (versión de madera), más de 100 reusos, más de 90 % de recuperación | Aceite | Página |
| Patente MX2012013514A (BASF SE) | Presentada el 18 may 2011, publicada el 24 ene 2013; estado legal sin verificar | — | Ficha |

Para nuestra hipótesis, el dato más cercano es RSC Adv 2024 (3.2 g/g con aceite vegetal, sin tratar) y el más duro es Mari 2025: confirma que un lecho de PU retiene aceite emulsionado, pero con techo de 77 % y con el espuma saturada clasificada como residuo peligroso. El PU de colchón viejo puede traer retardantes de flama (TDCPP, 1 a 5 %) y aminas aromáticas (TDA); calentar por encima de 165 °C genera TDA, así que el exprimido debe ser en frío.

### Esponjas que absorben aceite: qué dicen y qué no dicen las fuentes

Pregunta del equipo: ¿hay una esponja que absorba el aceite al lavar? **No encontré ninguna fuente que describa una esponja de uso doméstico que absorba aceite durante el lavado de trastes.** Lo más cercano son tres esponjas comerciales modificadas, ninguna probada con aceite de cocina usado:

| Fuente | Material | Qué reporta | Qué no dice |
| --- | --- | --- | --- |
| Oleo Sponge (Argonne; DOE CX-018039, 2018) | Espuma de poliuretano tratada químicamente; invento patentado de Argonne | Absorbe aceite del agua de forma selectiva; reutilizable | Capacidad y método de recuperación (la página es un registro ambiental) |
| OHM "smart sponge" (Northwestern, 2020) | Cualquier esponja comercial con recubrimiento oleofílico, hidrofóbico y magnético | Más de 30 veces su peso en crudos; el aceite se recupera exprimiendo; "varias decenas" de usos; menos de 1 % del aceite regresa al agua en una prueba de agitación | Que la base sea PU; aceites vegetales; cualquier lavado |
| Smart Sponge (CityU Hong Kong, 2023) | Esponja comercial modificada, polimérica o vegetal (la página no dice que sea PU) | 12 a 15 g/g (versión de madera); más de 100 reusos; más de 90 % del aceite recuperable; usos listados: limpieza de grasa doméstica, derrames y acuicultura (prueba en granja de langostinos: costo de remover aceite reducido en más de 20 %) | Método de recuperación (lavar, exprimir o solvente), tipos de aceite, disponibilidad comercial; es un proyecto de I+D |

Lectura:

- Las tres confirman el concepto (esponja comercial modificada, selectiva para aceite, reutilizable), pero ninguna es una esponja que "lave": el lavado o exprimido es la regeneración del material, no el uso.
- La única con base PU confirmada es la Oleo Sponge, y apoya la elección de material. También implica otra patente (Argonne), además de la de BASF, en la lista de libertad de operación.
- Nada de esto sustituye la prueba con aceite de cocina usado y detergente.

### Poliestireno expandido (unicel)

| Estudio | Resultado | Lectura |
| --- | --- | --- |
| Gazi | Styrofoam granular 4.4 a 8.1 g/g; espuma de PS 32 a 41 g/g (crudo, 24 h) | Reporte |
| Naser 2017 | 43 a 53 g/g en prueba de campo (unas 4 veces el laboratorio); el aceite no se puede recolectar; densidad del EPS 13 a 18 kg/m³ | Reporte |
| Kim 2024 | Esponja de EPS electrohilada ≈ 10 a 12 g/g con canola, soya y mineral; > 90 % de separación (la página se contradice con 262 g/g) | Reporte |
| IPICYT 2024 | Esponja de fibra de coco más EPS: 7.6 g/g, 10 ciclos | Reporte |
| Isik y Demir 2018 | Fibras: 55 a 124 g/g con aceite vegetal | Reporte |
| Jibril 2024 | PS más rGO: 133 a 169 g/g | Reporte |
| Ajaj (Kingston) | Migración de estireno desde envase de EPS: 1.31 µg/mL a 60 °C y 5.57 µg/mL a 70 °C en etanol al 95 %; fragmentos microplásticos por Nile Red | Reporte |
| UABC/RECIT | 125,000 t/a de EPS en México, 0.1 % reciclado, 98 % aire | Reporte |
| Misantla | EPS densificado en aceite usado de cocina a 200 a 250 °C, 90 % de reducción de volumen; el aceite no se recupera en cantidad apreciable | Solo resumen (Dialnet); temperaturas del reporte |

Capacidad alta no es lo mismo que recuperación: el EPS tiene celda cerrada, se aplasta y no devuelve el aceite, y por eso se pasó al PU. El 'por qué' es el cuadro del historial.

### Qué sostiene cada parte de la hipótesis

| Parte | Respaldo | Fuerza |
| --- | --- | --- |
| PU absorbe aceite | Varios estudios, 3.2 a 21 g/g | Alta (en laboratorio) |
| Se exprime y se reutiliza | Rocha, Hwang, JMSE: 50 ciclos | Media (aceite mineral o crudo; sin aceite vegetal usado) |
| Funciona con flujo continuo | Mari 2025 (40 mL/min) | Baja a media (tiempo de contacto 58 veces mayor que el nuestro) |
| Funciona con detergente | Mari 2025: 77 % | Baja (un solo estudio) |
| Se hace con PU reciclado de colchón | Rocha 2025 | Media (aceite de motor; aditivos sin evaluar para aceite de cocina) |
| El aceite recuperado sirve para biodiésel | Sin estudio con este aceite | Ninguna |

## Impacto estimado por región (LatAm, México, CDMX)

CDMX es la región con más datos (censo, SEDEMA, alcaldía Cuauhtémoc, norma NADF-012-AMBT-2015, multas). Monterrey es la segunda, pero solo en daño a la red: 150 km de tubería en muy mal estado y "buena parte" de los problemas ligados a grasas y aceites, sin porcentaje (Milenio, 17 mar 2026). Ningún estado tiene medida la fracción del aceite doméstico que baja por la tarja.

### a) Base: cuánto aceite usado doméstico hay

| Región | Población | Hogares | Aceite usado doméstico al año (central y rango) | Origen |
| --- | --- | --- | --- | --- |
| CDMX | 9,209,944 | 2,756,319 | 22.1 millones de L (18.5 a 41.3) | Censo 2020; cálculo mío con 8 L (6.7 a 15) por hogar |
| México | 126,014,024 | 35,219,141 | 282 millones de L (236 a 528) | Censo 2020; cálculo mío; GISA 2022 (320 millones de L) cae dentro |
| Latinoamérica | 663 millones (CEPAL, 2024) | No obtenido | 860 a 1,660 millones de L | Extrapolación mía con 1.3 a 2.5 L/persona (Argentina, Guayaquil, México); es la cifra menos confiable |

El dato argentino nacional (60 a 90 millones de L) implica unos 1.3 a 2.0 L/persona con ≈ 46 millones de habitantes (población de memoria, no de la fuente), por eso el límite inferior es 1.3. CEPAL reporta que la población creció menos de lo esperado y envejece; no revisé sus proyecciones de hogares, así que no sé si el aceite por hogar sube o baja.

**Lo que ya se capta.** SEDEMA CDMX 2021: 11,123 L acopiados, ≈ 0.05 % (0.03 a 0.06 %) del aceite doméstico usado de CDMX según mi cálculo. Alcaldía Cuauhtémoc (boletín 359, 8 oct 2025): 370 L/día en 35 contenedores de mercados, ≈ 135,000 L/año, pero de negocios de comida y no de hogares. La cifra de "440 millones de litros de agua protegidos al mes" de ese boletín sale de multiplicar por 40,000 L de agua por L de aceite, un factor divulgativo que aquí no se usa.

### b) Aceite que retendría el sistema

```latex
V_{ret}=N_{hog}\cdot a\cdot L\cdot \varphi\cdot \eta,\qquad \mathrm{DQO}_{evitada}\le 2.66\ \tfrac{\mathrm{kg\,O_2}}{\mathrm{L}}\cdot V_{ret}
```

con *a* la fracción de hogares que lo instala, *L* los litros de aceite usado por hogar al año, φ la fracción que baja por la tarja y η la fracción de eso que el sistema retiene. El 2.66 es la demanda teórica de oxígeno de la trioleina: es un tope, no una medición. Escenarios (η es supuesto mío; el único dato observado es el techo de 77 % con detergente):

| Escenario | L (L/hogar/año) | φ | η | Fracción del aceite doméstico retenida por hogar instalado |
| --- | --- | --- | --- | --- |
| Bajo | 6.7 | 0.37 | 0.30 | 11 % de 6.7 L = 0.74 L |
| Central | 8 | 0.557 | 0.50 | 28 % de 8 L = 2.2 L |
| Alto | 15 | 0.85 | 0.77 | 65 % de 15 L = 9.8 L |

| Región y adopción | Bajo (L/año) | Central (L/año) | Central (toneladas de aceite) | Central (toneladas de O₂, tope) | Alto (L/año) |
| --- | --- | --- | --- | --- | --- |
| CDMX, 1 % de hogares | 20,500 | 61,400 | 56 | 163 | 270,600 |
| CDMX, 5 % | 102,500 | 307,100 | 283 | 817 | 1,353,000 |
| CDMX, 20 % | 410,000 | 1,228,200 | 1,130 | 3,267 | 5,412,000 |
| México, 1 % | 261,900 | 784,700 | 722 | 2,087 | 3,457,600 |
| México, 5 % | 1,309,600 | 3,923,400 | 3,610 | 10,436 | 17,288,200 |
| México, 20 % | 5,238,500 | 15,693,600 | 14,438 | 41,745 | 69,152,800 |

Lectura:

- En el caso central, cada punto porcentual de adopción retiene ≈ 0.28 % del aceite doméstico usado de la región. Con 5 % de adopción son ≈ 1.4 %: 307,000 L/año en CDMX, unas 28 veces lo que SEDEMA acopió en 2021.
- El impacto es pequeño en volumen nacional (1.4 % con 5 %) y la incertidumbre es de un factor 13 entre bajo y alto en el mismo escenario. Los rangos de arriba son extremos combinados, no intervalos de confianza.
- El valor del aceite no paga el sistema: ≈ 2.2 L/año por hogar en el caso central, a un poco menos de 7 MXN/L (Mongabay 2021, Amro) son ≈ 15 MXN al año por hogar. La justificación es evitar el desazolve (MXN 4,400 a 12,000 según Expansión) y la multa (21 a 30 UMA), no vender aceite.
- La tendencia temporal del consumo y del desecho no se pudo establecer: no encontré una serie de tiempo para México ni para CDMX (las fuentes de mercado están tras muro de pago). Lo que sí hay es señal de política: campaña "Mi cocina no contamina" (SEDEMA, septiembre 2026), contenedores en mercados desde 2025, norma NADF-012 y multa en CDMX.

## Contexto global: uso, desperdicio y tendencia

Las cifras globales dan contexto y tendencia, pero no sirven para dimensionar un hogar: casi todo el aceite usado del mundo viene de industria y servicios de alimentos.

| Dato | Valor | Lectura | Fuente |
| --- | --- | --- | --- |
| Producción mundial de aceites vegetales, 2024/25 | 228.3 Mt, ≈ +4.5 Mt (≈ +2 %, cálculo mío) frente a 2023/24 | Es el único año con cambio leído; no es una serie | USDA citado por UFOP (Renewable Carbon News) |
| Consumo mundial, 2024/25 | ≈ 224.9 Mt | La página lo da con "presumiblemente" | Misma fuente |
| Aceite de cocina usado (UCO) mundial | 41 a 67 Mt/año | El resumen no cita fuente para el rango | Revisión *Discover Sustainability* 6:119 (2025) |
| El mismo artículo, en la introducción | ≈ 190 Mt/año (cita Mannu 2020) | Se contradice con el resumen y sería ≈ 85 % del consumo; lo descarto | Misma revisión |
| UCO como fracción del aceite comestible usado | 20 a 32 % | Chequeo mío: 20 a 32 % de 224.9 Mt son 45 a 72 Mt, consistente con 41 a 67 Mt | Revisión (cita Cárdenas 2021 y Teixeira 2018) |
| Por país (23 países, 2018) | China 5.6 Mt/año; India 1.135; Canadá, Dinamarca, España, Italia, Japón, Corea del Sur, Malasia y Reino Unido 0.1 a 0.5 cada uno; EE.UU. ≈ 450 millones de kg | La revisión los toma de Teixeira 2018 y Biodiesel Association 2023; México y el resto de Latinoamérica no aparecen | Revisión |
| Recolección | Solo 10 a 20 % del UCO de servicios de alimentos se recolecta para reciclar | Es el sector más fácil de captar; para hogares no hay dato | Biodiesel Association 2023, vía la revisión |
| Comercio de UCO para combustibles, 2022 | 3.7 mil millones de galones (≈ 13 Mt, conversión mía) | La misma página da 1.3 mil millones en otro párrafo; no queda claro si es comercio o suministro | LMC/GlobalData para Clean Fuels (sep 2023) |
| Proyección 2030 | 5 a 10 mil millones de galones, y 4 a 7 más si crece la recolección | Hay potencial de recolección en Asia, Sudamérica y Europa; el flujo principal va de Asia a Europa | Misma fuente |
| Exportaciones de UCO de China, 2024 | Máximo histórico por demanda de EE.UU., UE y Singapur | Solo vi el titular | S&P Global |

**Tendencia, con las reservas de arriba.**

- El aceite sube ≈ 2 % al año (un solo año leído), así que el aceite usado crece al menos con el consumo.
- El UCO se volvió insumo de combustibles: las proyecciones de oferta para 2030 son de 1.4 a 2.7 veces el comercio de 2022 (cálculo mío con las cifras de arriba). Eso favorece que un acopiador reciba el aceite, pero compite por volumen: lo que paga se basa en lotes grandes de restaurantes, y un hogar genera 4 a 8 L al año. Hace falta agregar (edificios, mercados, fondas) o un acopiador dispuesto a lotes pequeños.
- No leí la regulación que impulsa esa demanda (mandatos de EE.UU. y UE), así que no afirmo que la demanda se mantenga.
- Por persona, 41 a 67 Mt entre ≈ 8 mil millones de habitantes (población de memoria) son 5 a 8 kg/año, entre 2 y 4 veces el aceite doméstico de la sección anterior (2.0 a 2.5 L/persona). La diferencia es industria y servicios de alimentos.

**Chequeo cruzado que baja mi valor de trabajo.** Si la mitad de los 1,280 millones de L de consumo de México (Mongabay, sin fuente primaria) es doméstica y 20 a 32 % se vuelve aceite usado, salen 128 a 205 millones de L, es decir 3.6 a 5.8 L por hogar. Eso está por debajo de los 8 L de trabajo (6.7 a 15), así que el límite bajo real podría ser ≈ 3.6 L. Con 3.6 L, el caso bajo retiene ≈ 46 % menos de lo calculado, y la carga semanal del cartucho para φ = 0.37, 0.557 y 0.85 es 24, 36 y 54 g: 11 a 26 % de un cartucho tratado y 32 a 73 % de uno sin tratar. En ese caso un cartucho sin tratar bastaría y la hidrofobización dejaría de ser decisiva. No sé cuál de los dos extremos es el real, y por eso L está en la lista de faltantes con prioridad alta.

## Datos que no tenemos

| Prioridad | Dato faltante | Por qué importa | Cómo conseguirlo rápido |
| --- | --- | --- | --- |
| Alta | Fracción φ del aceite doméstico que baja por la tarja en México | Mueve el impacto de 37 % a 85 % entre proxies | Encuesta corta a 30 a 50 hogares; pregunta a SACMEX o SEDEMA si tienen estudio |
| Alta | Litros de aceite usado por hogar mexicano (rango 6.7 a 15) | Factor 2.2 en todo el dimensionamiento | La misma encuesta: botellas por mes |
| Alta | Capacidad q del PU con aceite vegetal usado y con residuos de comida | El único dato vegetal es 3.2 g/g sin tratar | Prueba mínima de una hora del documento para la Dra. |
| Alta | Aceite residual después de exprimir y retención en ciclos 2 a 5 | Define si el cartucho es reutilizable | Misma prueba |
| Alta | Desempeño con detergente de tarja y caída de presión a caudal de grifo | Mari 2025 es un solo estudio (77 %) a 40 mL/min | Prueba con agua jabonosa; medir tiempo de llenado |
| Media | Tamaño de gota del aceite aguas abajo de una tarja doméstica | Mi 5 a 20 µm es supuesto; decide si la trampa sirve | Literatura de emulsiones o medición con microscopio |
| Media | Lixiviados y aditivos del PU reciclado (retardantes, TDA) | Seguridad y aceptación del acopiador | Preguntar al acopiador y a la Dra.; usar PU de proveedor identificado |
| Media | Efecto de ese aceite en la transesterificación | Sin esto, la ruta a biodiésel no está demostrada | Consulta con acopiador (por ejemplo, Kolibrie Energy) |
| Media | Precio y oferta de PU reciclado en México y costo del cartucho | Presupuesto del punto 5 | Cotizar con colchoneras |
| Media | Estado legal de MX2012013514A y libertad de operación | Novedad e impedimentos | Consulta en IMPI |
| Media | Si la espuma saturada es residuo peligroso en México | En Brasil se clasificó así (Mari 2025) | Revisar NOM-052-SEMARNAT-2005 o consultar a especialista |
| Media | Fracción de hogares con tarja y espacio instalable (rentas, tarjas sin gabinete) | Mercado alcanzable | Datos de vivienda del Censo 2020 (no revisados) |
| Baja | Aceptación social en México | La referencia es Tesalónica (20.9 % recicla) | Encuesta con la misma muestra |
| Baja | Serie de tiempo del consumo y desecho | Tendencia | Pedir a Profeco o INEGI; buscar tras el plazo |
| Pendiente | Si la Dra. revisará y autoriza usar su nombre | Respaldo | Enviar el documento de consulta |
| Alta | Acidez, agua y sólidos del aceite recolectado, por flujo (botella, fonda, trampa y cartucho) | Define la ruta (cortes de 2 y 20 mg KOH/g); hoy son hipótesis | Titulación de muestras de hogares y fondas; datos del acopiador |
| Alta | Especificaciones, precio y condiciones del acopiador (las 10 preguntas de la sección dedicada) | Sin esto la ruta a biodiésel y el presupuesto son supuestos | Llamada o reunión con el acopiador candidato |
| Media | Desempeño de esponjas modificadas con aceite de cocina usado (ninguna fuente lo mide) y patente Argonne (Oleo Sponge) además de la de BASF | Apoyo al material y libertad de operación | Prueba mínima de una hora; consulta en IMPI |

## Por consultar con el acopiador

Sin estas respuestas, la ruta del aceite recuperado (y todo lo que dice la propuesta sobre biodiésel) queda como supuesto. Candidato para empezar: Kolibrie Energy, que procesa a biodiésel el aceite de los contenedores de los mercados de Cuauhtémoc (boletín 359, 2025); es un candidato, no un contacto confirmado.

| # | Pregunta | Por qué importa | Qué decide |
| --- | --- | --- | --- |
| 1 | ¿Recibe lotes de 10 a 50 L? ¿Mínimo, frecuencia, recolecta o hay que llevarlo? | Un hogar genera 4 a 8 L al año; sin agregación no hay ruta | Modelo de acopio (edificio, mercado, fonda, ruta propia) |
| 2 | Especificación de entrada: acidez o FFA máximos, humedad, impurezas, color. ¿Qué hace con lo que no cumple? | Es el criterio que usará para aceptar o rechazar cada lote | Los cortes de 2 y 20 mg KOH/g de la clasificación |
| 3 | ¿Acepta aceite de trampa o cartucho (con agua, detergente y sólidos)? ¿Cuánta agua tolera? ¿Cobra por recibirlo? | Es nuestro flujo más difícil; hoy lo tratamos como grasa café | Si el cartucho puede prometer biodiésel o solo "entrega a acopiador" |
| 4 | Precio por litro según clase de aceite (acidez baja, media y alta) | Referencias previas: poco menos de 7 MXN/L (Mongabay 2021) y costo de producir biodiésel de 11.12 a 13.70 MXN/L (UAEH 2025, sin fuente) | Presupuesto del punto 5; si el aceite paga el frasco |
| 5 | ¿Qué rutas tiene (alcalina, esterificación ácida, codigestión) y qué hace con AV > 20? | Define si el corte de 20 es nuestro o suyo | Clasificación y destino por lote |
| 6 | ¿Afectan a su proceso trazas de espuma, retardantes, jabón o detergente? ¿Cuánto toleran? | No hay estudio del efecto en la transesterificación | Si se necesita filtrar o lavar antes de entregar |
| 7 | ¿Cuántos litros de aceite de hogares y fondas le llegan hoy y con qué acidez típica? | Sería el primer dato mexicano de acidez doméstica | Supuesto de acidez por flujo |
| 8 | Documentación: manifiesto, registro como transportista o acopiador de residuo de manejo especial, constancia de destino | NADF-012-AMBT-2015 rige el manejo en CDMX; no verifiqué qué exige a un acopio de hogares | Permisos y cumplimiento |
| 9 | ¿Proporciona envases o frascos y los recoge? ¿Puede dar constancia de litros recibidos? | Sirve para medir impacto con datos propios | Métrica de impacto |
| 10 | ¿Daría una carta de intención o alianza para la propuesta? | Es parte de lo que falta en sostenibilidad | Entregable del punto 5 |

Al cerrar la consulta, el documento debe pasar de cada fila a un dato o un "no aplica"; mientras tanto se declaran como supuestos.

## Documentos vigentes

| Documento | Para qué sirve | Estado |
| --- | --- | --- |
| [Consulta técnica para la Dra.: columna de espuma de poliuretano reciclada](https://claude.ai/code/artifact/8ee2e396-0e17-4262-8c83-6ee4d9854f0b) | Enviar a la Dra. del IPN para verificar la hipótesis; incluye prueba mínima de una hora y umbrales | Completo, 4 a 5 páginas (se pidieron 2 a 4) |
| [Columna de poliestireno reciclado](https://claude.ai/code/artifact/ed26d609-e7ba-4928-9035-0dd6a30ab115) | Análisis del unicel con dimensionamiento y respaldo | Secciones 1 a 4 y respaldo; faltan destino del aceite, respuestas al reto, números, caveats, plan y fuentes. Probablemente conviene rehacerlo alrededor del PU |
| [Propuesta de combustible y fertilizante (Doc 2)](https://claude.ai/code/artifact/2cd7cb71-79ff-4675-acb4-f6db6071ab61) | Propuesta anterior, 14 caveats, subsección de filtro-trampa | Superada por el giro a PS y PU; conserva la ruta por índice de acidez y los caveats |
| Este documento | Estado, hipótesis, datos y faltantes | Corte al 16 oct 2026 |

**Pendientes del plan anterior (Bloques 1 a 5 de Doc 2):** límite de palabras, nombre y pitch, abrir textos completos de las cifras de portada, pegar las respuestas, tabla de presupuesto, carta de aliado, revisión de unidades, descanso y ensayo.

## Cobertura contra los lineamientos

Base: los cinco puntos evaluados y el alcance (hogares y fondas, sin restaurantes). El texto original del reto no está en esta sesión (se resumió antes), así que conviene releerlo contra esta tabla.

| Punto | Lo que el documento ya tiene | Lo que podría faltar |
| --- | --- | --- |
| 1. Problemática | Costo de desazolve (MXN 4,400 a 12,000), multa (21 a 30 UMA), norma NADF-012; volumen de aceite por región (CDMX, México, Latinoamérica, mundo); destino del aceite en tres países proxy | Fracción φ en México; porcentaje de obstrucciones de la red de CDMX causadas por grasa (no lo encontré); daño medido en cuerpos de agua (solo el factor divulgativo de 40,000 L); costo para el hogar de una obstrucción interna; voz de usuarios (encuesta o entrevistas) |
| 2. Producto o servicio | Sistema de dos etapas con parámetros, dimensionamiento del cartucho, ruta del aceite y restricción de uso; qué sostiene cada parte | Esquema o dibujo con dimensiones del gabinete; quién exprime, cada cuánto y dónde se entrega el frasco; indicador de saturación; modelo (venta, suscripción o servicio de recolección); usuario inicial (hogar o fonda); PU específico y proveedor; higiene y olor bajo la tarja; seguridad del cartucho saturado (rancidez y posible autocalentamiento de espuma empapada en aceite insaturado: no lo investigué) |
| 3. Impacto social y ambiental | Escenarios por región con litros, toneladas y tope de demanda de oxígeno | Impacto social cuantificado (ahorro por hogar, empleo, salud); PU desviado de relleno por cartucho (no calculado); CO₂ evitado (solo la cifra del boletín de Cuauhtémoc); residuo de la espuma saturada y del frasco; análisis de ciclo de vida |
| 4. Innovación | Novedad solo en la integración; patente BASF y esponja de Hong Kong ya existen; comparación unicel contra PU | Trampas de grasa domésticas comerciales (no las investigué) y qué las diferencia; estado de la técnica en México; libertad de operación de la patente; qué parte es defendible |
| 5. Sostenibilidad, presupuesto y aceptación | El aceite no paga el sistema (≈ 15 MXN/año por hogar); la justificación es evitar desazolve y multa; referencia de participación de 20.9 % | Presupuesto con precios (trampa, cartucho, instalación, frascos); precio al usuario y disposición a pagar; ciclo de reemplazo y mantenimiento; financiamiento; carta del acopiador; plan de escalamiento; riesgos y mitigación; aceptación social en México |
| Transversal | Hipótesis con parámetros, lista de datos faltantes y prueba mínima de una hora para la Dra. | Ninguna prueba propia (es parte del alcance); aval y consentimiento de la Dra.; límite de palabras; nombre y pitch; qué se afirma y qué no, en un solo lugar |

**Lo más débil hoy:** presupuesto (punto 5, sin precios) y diseño físico del producto (punto 2, sin esquema). Ambos se pueden cubrir en el plazo con cotizaciones y un dibujo; los demás faltantes son datos que el equipo no puede obtener sin pruebas y se declaran como supuestos.

## Fuentes

Leídas directamente en esta sesión (página o resumen): [INEGI, Censo 2020 CDMX](https://www.inegi.org.mx/contenidos/programas/ccpv/2020/doc/cpv2020_pres_res_cdmx.pdf); [INEGI, Censo 2020 nacional](https://iieg.gob.mx/ns/wp-content/uploads/2021/02/Presentación-INEGI-resultados-Censo-2020-Estados-Unidos-Mexicanos.pdf); [La Capital, Argentina 2022](https://www.lacapital.com.ar/la-region/mas-la-mitad-los-hogares-no-separa-el-aceite-usado-n10012762.html); [Guayaquil, LACCEI 2020](https://pure.ups.edu.ec/en/publications/domestic-waste-cooking-oil-generation-in-the-city-of-guayaquil-an/); [Mongabay 2021](https://es.mongabay.com/2021/08/biocombustible-mexico-burocracia-impuestos-crimen-organizado/); [Alcaldía Cuauhtémoc, boletín 359](https://alcaldiacuauhtemoc.mx/wp-content/uploads/2025/11/359.-PROGRAMA-DE-RECOLECCION-DE-ACEITE-EN-MERCADOS-DE-LA-CUAUHTEMOC-PROTEGE-440-MILLONES-DE-LITROS-DE-AGUA-AL-MES.pdf); [TECTZAPIC, Ciudad Valles 2018](https://www.eumed.net/rev/tectzapic/2018/02/aceites-grasas-residuales.html); [Milenio, Monterrey 2026](https://amp.milenio.com/comunidad/ayd-arranca-rehabilitacion-drenaje-area-metropolitana-monterrey); [ADN40, SEDEMA 2026](https://www.adn40.mx/es-tendencia/2026-09-25/que-hacer-con-el-aceite-usado-de-la-cocina-el-metodo-correcto-segun-sedema/); [TEPEXI, UAEH 2025](https://repository.uaeh.edu.mx/revistas/index.php/tepexi/article/download/14796/12601/99642) (precio sin fuente); [CEPAL vía Montevideo Portal](https://www.montevideo.com.uy/Noticias/Poblacion-de-America-Latina-crece-menos-de-lo-esperado-y-llega-a-663-millones-segun-Cepal-uc907959) (solo titular).

Leídas para el contexto global, la clasificación y las esponjas: [Canakci y Van Gerpen 2001](https://www.biodieseleducation.org/Literature/Journal/2001_Canakci_Biodiesel_production.pdf); [glicerólisis como pretratamiento, De Gruyter 2017](https://www.degruyterbrill.com/document/doi/10.1515/gps-2017-0118/html); [Legiscomex, producción de aceites en México](https://www.legiscomex.com/sites/legiscomex/files/2024-09/El%2065%2C6%25%20de%20la%20producci%C3%B3n%20de%20aceites%20vegetales%20en%20M%C3%A9xico%20corresponde%20a%20aceite%20de%20soya.pdf); [USDA vía UFOP, producción 2024/25](https://renewable-carbon.eu/news/2024-25-vegetable-oil-production-to-hit-record-levels/); [Clean Fuels, oferta global de UCO](https://cleanfuels.org/clean-fuels-releases-outlook-on-global-supplies-of-used-cooking-oil-for-biodiesel-and-renewable-diesel-production/); [revisión Discover Sustainability 2025](https://link.springer.com/article/10.1007/s43621-025-00905-7); [Oleo Sponge, DOE CX-018039](https://www.energy.gov/node/3585032); [OHM sponge, Northwestern 2020](https://news.northwestern.edu/stories/2020/05/smart-sponge-could-clean-up-oil-spills/); [Smart Sponge, CityU 2023](https://www.cityu.edu.hk/en/chem/about-us/news/2023/smart-sponge-cost-effective-and-sustainable-solution-waste-oil-treatment); [Smart Sponge, HK Tech 300](https://www.cityu.edu.hk/en/hktech300/start-ups/seed-fund-teams/smart-sponge).

Tomadas de informes de investigación de la sesión, no releídas aquí: los estudios de PU y EPS de las secciones de investigación (Rocha 2025, Hwang, Lee y Oh 2022, Mari 2025 en *Polymers* 17:1127, Naser 2017, Gazi, Kim 2024, Misantla, Ajaj y los demás), Tesalónica, Yaguará, Mata de São João, MITECO, GISA 2022, SEDEMA 2021, Expansión sobre desazolve y multas, y Mena. Cualquier cifra de esas debe abrirse en su fuente antes de usarse en el documento final.

**No encontré ni verifiqué:** un dato mexicano de la fracción por la tarja, una serie de tiempo del consumo de aceite, la proyección de hogares de CEPAL, el estado legal de la patente MX2012013514A, y cualquier estudio de PU con aceite vegetal usado en columna.
