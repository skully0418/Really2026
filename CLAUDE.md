# CLAUDE.md: contexto del proyecto Rally 2026, reutilización de aceite doméstico

Corte: 17 oct 2026, 01:20 (hora CDMX). Se actualiza en cada avance y se sube al contexto del proyecto.

## Cómo trabajar en este proyecto
- Idioma: español.
- Registrar aquí cada avance en la bitácora y volver a subir el archivo.
- Afirmar solo lo que tiene fuente; marcar supuestos y datos sin verificar.
- La Dra. Dulce ya autorizó que se mencione su asesoría en el reporte (confirmado por la usuaria el 17 oct); falta saber de qué forma quiere aparecer.

## Qué se entrega
Reporte de pautado de resolución del desafío "Reutilización de aceite doméstico". Secciones y límites de caracteres: 1 Problemática (1250), 2 Solución (1250), 3 Impacto (1000), 4 Innovación (1000), 5 Pre factibilidad (1500), 6 Propuestas descartadas, 7 Referencias. Equipo y sede están por completar. Plazo corto y sin pruebas propias.

El desafío: proponer una forma económica y accesible de reutilizar aceite doméstico para generar energías limpias u otros subproductos. Alcance del equipo: hogares y negocios informales (fondas); restaurantes fuera porque ya están regulados.

## Estado de la propuesta (vigente desde el 17 oct)
- **Material: malla de poliestireno expandido (unicel) reciclado**, disuelto y transformado por electrohilado o por inversión de fases. El electrohilado tiene fuente (Isık y Demir 2018); el equipo agregará la fuente del proceso de inversión de fases.
- **Poliuretano descartado** por precio (decisión del equipo, 17 oct). Ya no es plan B. La evidencia de PU queda en `contexto/` solo como historial.
- **Dispositivo:** filtro de una pieza bajo la tarja, entre la coladera y el céspol. Carcasa de polipropileno; el prototipo se imprime en PETG. Por dentro: prefiltro (pichancha), cámara de calma donde el aceite libre flota, cartucho con la malla enrollada alrededor de un tubo de rebose con campana (toma sumergida) y salida al céspol. Roscas ISO 228-1 (G 1½ en la entrada, G 4 en la tapa). La trampa de grasa de 10 L aparte ya no está en el diseño: la cámara de calma cumple esa función.
- **Ruta del aceite: epoxidación** para obtener aceite epoxidado, materia prima de plastificantes de PVC y resinas epoxi. No va a cosméticos ni fármacos (sector regulado, nota de la doctora). La ruta con más datos con aceite usado es el ácido perfórmico generado in situ (agua oxigenada al 30 % más ácido fórmico), a 55–60 °C durante unas 3 h en baño María. Ese calentamiento se logra con cualquier estufa y nunca pasa de unos 100 °C; no se calienta más porque arriba de 60 °C el epóxido se degrada. Los detergentes se retiran como destino; el enfoque es solo epóxidos. La versión 03 decía "oxidar solo con temperatura y aire", y eso no tiene fuente: se retira. Detalle en `documentos/ruta-epoxidacion-aceite.md`.
- **Alcance:** sin cambios por ahora (hogares, fondas y "algunos restaurantes que no cumplan las normas", como dice la versión 03). La doctora anotó "Los restaurantes ya tienen ruta"; queda pendiente.
- **Diseño:** modelo paramétrico (Onshape FeatureScript, STEP y STL) y animación del funcionamiento hechos el 17 oct. Se terminan con la nueva información (malla en lugar de espuma) y después se suben al repositorio.
- No se usa en jabón ni en nada con contacto humano.

## Lo que dijo la doctora en los audios (transcripción Whisper "small", con partes dudosas)
1. Cambiar de polímero: el del proyecto original absorbe agua (hidrofílico, acrilato de sodio); usar uno hidrofóbico que atrape aceite.
2. Columna empacada con esferas de ese polímero, como las de filtración de agua; se recolectan las esferas y se saca el aceite.
3. Usos: drenajes de ciertas empresas y tuberías caseras.
4. Afinidad química, no tamizado: una malla filtra por tamaño de molécula.
5. Reciclar unicel: no se puede reexpandir, pero sí solubilizar y transformar en mallas modificadas (aerogeles o mallas "electro…", palabra sin confirmar).
6. Plantearlo como nueva aplicación de un material conocido; si se redacta bien, el proyecto puede ganar.
Por escuchar de nuevo: tipo exacto de malla del audio 3 y los años mencionados. La doctora no da tamaños, polímero exacto ni condiciones de operación. Según el contexto, trabaja en poli(éster-uretano)s biomédicos, no tiene publicaciones sobre poliestireno o aceite de cocina; su respaldo es una opinión de consulta.

## Notas escritas de la doctora sobre la versión 03 (17 oct)
Archivo: `entregables/03b_Propuesta_con_notas_Dra_Dulce.pdf`. Transcripción y cómo se atiende cada nota: `documentos/notas-dra-dulce-17oct.md`.
1. "Los restaurantes ya tienen ruta" (junto al alcance). Alcance sin cambios por ahora.
2. "oleofílico" e "inversión de fases o electro hilado", resaltados.
3. "No industria cosmética ni farmacéutica, porque está regulado".
4. "Propuesta de producto de reacciones de epoxidación a temp. ambiente".
5. "Epóxido cíclico básico o lineal, que se ponga en resinas o algo" (significado exacto por confirmar).
6. "Investigar acidez".
7. "Checar su propuesta conforme a lo que se describe arriba": la segunda mitad del documento contradice la primera. Reemplazos en `documentos/redaccion-corregida-propuesta.md`.

## Evidencia encontrada (solo resúmenes leídos)
**Poliestireno reciclado transformado y aceite (existe, la novedad no es el material):**
- Isık y Demir 2018: unicel de desecho electrohilado, hasta 124 g/g y 99 % de separación en aguas aceitosas.
- Lin et al. 2012: fibras nanoporosas de poliestireno, unos 112 g/g con aceite de soya y 97 g/g con girasol.
- Budlayan et al. 2021: microfibras de unicel de desecho con centrífuga adaptada, unos 15.5 g/g.
- Akanji e Iwarere 2024: unicel de desecho con óxido de grafeno reducido, reúso hasta el tercer ciclo.
- Algodón con ZnO recubierto con poliestireno de cubiertos desechables, para aceite vegetal en aguas de cocina.
- Akanbi 2018 (tesis UCL): las mallas electrohiladas son frágiles, sobre todo tras absorber aceite.
- Revisión previa del equipo: Alvarado-Gómez 2024 (esferas de fibra de coco con unicel, 7.6 g/g, 10 ciclos); Naser 2017 (unicel en trozos, no suelta el aceite).
**Epoxidación de aceite de cocina usado (17 oct, solo resúmenes):**
- Bourkaib et al. 2025: ácido perfórmico in situ, 60 °C, 3 h. Con aceite usado: 84.2 % de oxígeno oxiránico relativo y 96.3 % de selectividad.
- Azlan Raofuddin et al. 2023: aceite usado de palma, 55 °C, 70.6 % de conversión relativa.
- Suzuki et al. 2018 (UFMG): aceite usado epoxidado como plastificante de PVC, comparable al comercial.
- Chaiyaraksa et al. 2025: sustituyó por completo al DOP en PVC.
- Rincón Vija 2018 (UNAL): pretratamiento con agua oxigenada; 3.2 % de oxígeno oxiránico.
- AIChE 2024: filtrar y neutralizar, porque las impurezas desactivan el catalizador.
- Temperatura: el óptimo publicado está entre 55 y 60 °C; a 70 °C el oxirano cae bruscamente (Budiyati 2025), y subir la temperatura favorece la apertura del anillo (Campanella 2008). A temperatura ambiente la ruta perfórmica es unas 6.5 a 13.6 veces más lenta (cálculo de Arrhenius con las energías de activación reportadas). Las rutas cercanas a temperatura ambiente (dimetildioxirano con Oxone; lipasa a 45 °C) cuestan más en reactivos o enzima.
**Poliuretano:** descartado por precio. La evidencia previa (Rocha 2025, Mari 2025, etc.) queda en `contexto/` como historial.
**No encontrado:** columna doméstica de unicel mexicano con regeneración; datos de columna o de exprimido de mallas de poliestireno; datos con aceite de cocina usado y detergente real; epoxidación "solo con temperatura y aire"; umbral de acidez publicado para epoxidar aceite usado.

## Datos de aceite (preferir los del contexto del equipo)
- Aceite usado por hogar: valor de trabajo 8 L/año (rango 6.7 a 15), a partir de 2.0 a 2.5 L por persona (Argentina, Guayaquil, GISA 2022) y 3.56 personas por hogar (Censo 2020).
- Consumo de aceite (no es aceite usado): 10 L por persona al año (Profeco); 1,280 millones de L al año (Mongabay 2021, sin fuente primaria). No usarlos como aceite desechado.
- Volumen nacional de aceite usado: 320 millones de L al año (GISA 2022 y TecNM; no verificado si es consumo o aceite usado). Hay estimaciones de hasta 360 millones de L (CEMIE-BIO).
- Fracción que baja por el desagüe: 37 % a 85 % en estudios de otros países; sin dato mexicano.
- Daño: "1 L contamina 40 mil L de agua" (UNAM, Sedema, alcaldía Cuauhtémoc): cifra divulgativa.
- Acopio actual: Cuauhtémoc, 370 L al día en mercados (unos 135,000 L al año, cerca de 0.04 % del volumen nacional estimado, cálculo mío); SEDEMA 2021, 11,123 L.
- Costos: desazolve MXN 4,400 a 12,000 (Expansión); multa de 21 a 30 UMA; norma NADF-012-AMBT-2015 (CDMX).
- Mercado (de valor, no de volumen): aceite comestible México 3.87 % anual 2026-2034 (IMARC); aceite de cocina usado, 88.3 millones USD en 2025 y 5.11 % anual (IMARC).
- Impacto por escenarios (contexto): caso central, 2.2 L retenidos por hogar con el sistema; 5 % de adopción en CDMX, unos 307,000 L al año y hasta 817 t de oxígeno de demanda evitada (tope teórico de 2.66 kg O₂/L); factor de incertidumbre de unas 13 veces.
- Dimensionamiento del cartucho: el cálculo anterior (1 L, 207 g) se hizo con datos de PU, ya descartado. Hay que rehacerlo con las capacidades de la malla de poliestireno: 15.5 g/g (Budlayan 2021) a 124 g/g (Isık y Demir 2018), ambas de laboratorio. El aceite semanal por hogar no cambia: 52, 79 y 120 g con 8 L al año y φ de 0.37, 0.557 y 0.85.

## Correcciones registradas
- Dije que un hogar generaba unos 36 L de aceite al año. Error: usé consumo por persona (Profeco). Corregido a 8 L en el documento de la doctora.
- El descarte de la "columna de unicel" del contexto aplica al unicel en trozos; las mallas transformadas que propone la doctora tienen estudios de reúso, con pocos ciclos.
- Afirmar que la propuesta de la doctora "no existe" sería incorrecto: el material está publicado. Solo la integración doméstica se puede presentar como nueva.
- Los cálculos de impacto del borrador de la sección 1 (4.5 L por hogar, 180 mil litros de agua) usaban 15 L por hogar; hay que rehacerlos con 8 L y φ de 0.37 a 0.85 (unos 3 a 6.8 L, o 120 mil a 270 mil litros de agua con el factor divulgativo).

## Riesgos técnicos
Forma de empaque sin datos de caída de presión; electrohilado con solventes tóxicos (THF, DMF) y equipo de alto voltaje (laboratorio, no casa); mallas frágiles tras absorber aceite (método para sacar el aceite por confirmar); sin datos con detergente real; caudal de grifo de 1 a 8 L/min contra 40 mL/min de la única columna publicada; aceite de la malla tratado como de acidez alta hasta medirlo; en la epoxidación, el ácido, el agua y la temperatura abren el anillo epóxido (no pasar de 60 °C); a temperatura ambiente estricta tarda más de un día; ácido fórmico y agua oxigenada son corrosivos (laboratorio o planta aliada); filtrar las fibras de poliestireno del aceite antes de epoxidar.

## Documentos
- Documento "Propuestas de la Dra. Dulce: columna empacada con poliestireno reciclado": https://claude.ai/code/artifact/2c76dd6f-472a-4ea7-bef6-bedf1a94e010 (resumen, audios, literatura, tabla por sección del reporte, riesgos, preguntas para la doctora, fuentes). La tabla "Cómo plantearlo" se actualizó con el contexto del 16 oct.
- Documento "Consulta técnica para la Dra. Dulce: sorbente de poliestireno reciclado para aceite de cocina" (para enviarle): https://claude.ai/code/artifact/c6aeb3c3-2423-4730-8e22-2729f72f9df4. Nueve secciones: qué se le pide, su orientación en seis puntos, propuesta de dos etapas con poliestireno como eje y PU como alternativa (el PU ya se descartó), tabla de literatura, dimensionamiento (aceite semanal de 52, 79 y 120 g; 3.4 a 24 g de sorbente según q), siete preguntas, prueba de una hora con umbrales, qué se afirma y qué no, fuentes. Pendiente de revisión del equipo antes de enviarlo.
- PDF de 3 hojas para la doctora: "Filtro de aceite para tarja con unicel reciclado" (Propuesta_OilxForce_Dra_Dulce.pdf). Dice explícitamente que ella asesora la parte técnica; sin fórmulas. Incluye problema, esquema del sistema, lo que cambió su orientación, patentes similares (US 4,022,694 Hydronautics 1977 expirada; MX2012013514A BASF, estado sin verificar; US 11,065,602 University of South Africa 2021, nanofibras de EPS para crudo, activa; US 2023/0183602 McCarthy, trampa de grasa con bolsas absorbentes), proyectos en otros países (Izmir 2018, Filipinas 2021, IPICYT 2024, Smart Sponge Hong Kong, Oleo Sponge Argonne, OLEOTRAP Malasia), cinco preguntas, prueba de una hora, qué se afirma y qué no, siguientes pasos.
- Versión revisada por el equipo de la propuesta para la doctora (docx, 16 oct 23:50): cambia el destino del aceite a oxidación para obtener moléculas epoxidadas (detergentes o resinas) en lugar de entrega a biodiésel; menciona inversión de fases o electrohilado para la malla; amplía el alcance a pequeños comercios y algunos restaurantes que no cumplen la norma. La aparente contradicción con el descarte del biorrecubrimiento se resuelve así: lo descartado fue formular nosotros una resina con MDI para recubrir fertilizante; ahora se entrega aceite epoxidado como materia prima (ver `documentos/redaccion-corregida-propuesta.md`).
- Versión 03 con notas de la doctora (PDF, 17 oct): `entregables/03b_Propuesta_con_notas_Dra_Dulce.pdf`; notas transcritas en `documentos/notas-dra-dulce-17oct.md`.
- Ruta del aceite: `documentos/ruta-epoxidacion-aceite.md` (rutas comparadas, temperatura ambiente, acidez, productos, fuentes).
- Redacción corregida sin contradicciones: `documentos/redaccion-corregida-propuesta.md` (secciones 2 a 6 del reporte dentro de los límites de caracteres y reemplazos para la segunda mitad del documento de la doctora).
- Diseño (aún fuera del repositorio): FeatureScript paramétrico para Onshape, STEP, STL para PETG y animación del ensamble y funcionamiento con malla de poliestireno. Se suben cuando se termine el diseño con la nueva información.
- Repositorio GitHub: https://github.com/skully0418/Really2026 (todo el material organizado en contexto/, documentos/, entregables/, referencias/, scripts/).
- Contexto del proyecto del equipo (corte 16 oct 2026): documento compartido por el usuario; incluye consulta técnica para la doctora (columna de PU), historial de decisiones, datos y lista de faltantes.
- Borrador del reporte en el chat (secciones 1 a 7 con PU y trampa de grasa): quedó desactualizado frente a la orientación de la doctora y los datos corregidos; rehacer.

## Pendientes
1. Agregar la fuente del proceso de inversión de fases para la malla (la sube el equipo).
2. Terminar el diseño con la malla de poliestireno (los parámetros del modelo ya dicen "malla"; falta definir cómo se saca el aceite de la malla) y subir modelo, STEP, STL y animación.
3. Pasar al docx de la versión 03 los textos de `documentos/redaccion-corregida-propuesta.md` y corregir las erratas listadas en las notas.
4. Rehacer el dimensionamiento del cartucho con las capacidades de la malla de poliestireno.
5. Preguntar a la doctora: significado de "epóxido cíclico básico o lineal"; si acepta el baño María a 55–60 °C en lugar de temperatura ambiente estricta; umbral de acidez y pretratamiento; cómo sacar el aceite de la malla; consentimiento para citarla.
6. Decidir el alcance (nota "Los restaurantes ya tienen ruta") y la zona ("sociedad mexiquense" frente a datos de CDMX). Por ahora sin cambios.
7. Al pasar los textos al docx, quitar "detergentes" como destino (el enfoque es solo epóxidos).
8. Completar equipo y sede del reporte; costo por filtro; fin de vida del relleno saturado; laboratorio o comprador del aceite epoxidado.

## Bitácora
- 16 oct 19:38: borrador del reporte de pautado con trampa de grasa y cartucho de PU.
- 16 oct 19:41: reescritura de la sección 1 con cifras verificables en vez de exageraciones.
- 16 oct 19:45: búsqueda de volumen actual y tendencia del aceite; se detectó el error de 36 L por hogar.
- 16 oct 19:51: búsqueda de literatura; la propuesta de la doctora sí tiene estudios previos.
- 16 oct 19:56: se plantea la columna empacada de unicel transformado.
- 16 oct 19:58: creado el documento "Propuestas de la Dra. Dulce".
- 16 oct 20:03: reutilizar unicel; no se pudo abrir el enlace compartido (devuelve página vacía; pegar el texto o PDF).
- 16 oct 20:16: revisado el contexto del equipo; corregido el dato de 8 L; tabla del documento actualizada.
- 16 oct 20:20: creado este CLAUDE.md y subido al proyecto.
- 16 oct 20:35: creado el documento de consulta técnica para la doctora, con poliestireno como eje y PU como alternativa; CLAUDE.md actualizado.
  - Supuestos que el equipo debe confirmar: PU como alternativa y no como material principal; umbrales de la prueba propuestos por nosotros (incluido desprendimiento ≤ 1 %); masa de sorbente calculada con capacidades de laboratorio, sin densidad de empaque.
- 16 oct 20:55: generado el PDF de 3 hojas para la doctora con patentes y proyectos similares. Supuesto: "Oilx-Force" es el nombre del equipo. Sin datos de contacto ni nombres de integrantes.
- 16 oct 23:55: el equipo envió la versión revisada (docx) de la propuesta para la doctora; se organizó todo el material en un repositorio local para subirlo a GitHub (skully0418/Really2026).
- 17 oct 00:03: subido a GitHub (skully0418/Really2026, rama main, commit c73de2b).
- 17 oct 00:15: verificados los puntos 5 y 6 del formato (`documentos/verificacion-puntos-5-y-6.md`): el 6 se puede redactar ya; al 5 le faltan costo por filtro, fuente de la epoxidación y fin de vida del relleno. Archivos renombrados (01 propuesta del equipo, 02 consulta técnica, 03 propuesta centrada con la doctora) y formato obligatorio agregado.
- 17 oct 00:50: notas escritas de la doctora agregadas (`03b` y `notas-dra-dulce-17oct.md`). PU descartado por precio; material vigente: malla de poliestireno (electrohilado o inversión de fases). Investigada la epoxidación de aceite usado (`ruta-epoxidacion-aceite.md`); se retira la "oxidación solo con temperatura y aire" por falta de fuente. Redactadas las secciones 2 a 6 sin contradicciones (`redaccion-corregida-propuesta.md`). Alcance sin cambios. Diseño (modelo paramétrico y animación) pendiente de terminar antes de subirlo.
- 17 oct 00:55: calentamiento definido como baño María a 55–60 °C (accesible con cualquier estufa, tope de unos 100 °C; arriba de 60 °C el epóxido se degrada, Budiyati 2025 y Campanella 2008). Detergentes retirados; enfoque solo en epóxidos. En el diseño y la animación el relleno se llama malla de poliestireno.
- 17 oct 01:20: punto 6 redactado y pegado en el formato (`entregables/Punto_6_Propuestas_descartadas.md` y `entregables/Formato_obligatorio_con_Punto_6_Propuestas_descartadas.docx`): 10 propuestas descartadas. Verificadas Naser (SPE-172000-MS, 2014; frase sobre no reutilizar ni recolectar el aceite) y Yamane y Kawasaki 2015 (el biodiésel disuelve EPS). Decisiones de la usuaria: epoxidación como destino final; fertilizante descartado por costos y viabilidad económica y social, enfocándose en el filtro; PU descartado por precio y por mejor viabilidad ambiental del poliestireno reciclado; la Dra. Dulce autorizó mencionar su asesoría. Pendiente: referencias del punto 7 (Naser, Yamane y Kawasaki, RECIT, Bourkaib, Cuauhtémoc) y revisar Bourkaib y Cuauhtémoc, leídos solo en resumen.
