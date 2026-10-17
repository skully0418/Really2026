# Really 2026 · Oilx-Force

Rally Latinoamericano de Innovación 2026, desafío 07: **Reutilización de aceite doméstico**.

Propuesta del equipo: un filtro bajo la tarja, hecho de unicel (poliestireno expandido) reciclado y transformado, que atrape el aceite de cocina antes de que llegue al drenaje. Asesoría técnica: Dra. Dulce María González García (su nombre y opinión se citan solo con su consentimiento expreso).

## Estado al 17 oct 2026

- **Material:** malla de unicel reciclado, disuelto en acetona y hecha por inversión de fases en agua (alternativa: d-limoneno). El electrohilado y el poliuretano se descartaron por precio.
- **Mantenimiento:** cartucho retornable; el aliado saca el aceite.
- **Dispositivo:** filtro de una pieza bajo la tarja, entre la coladera y el céspol. Lleva prefiltro, cámara de calma, cartucho con la malla y tubo de rebose con toma sumergida.
- **Ruta del aceite:** epoxidación para obtener aceite epoxidado, materia prima de plastificantes de PVC y resinas (ni cosméticos ni fármacos), a 55–60 °C en baño María. Ver `documentos/ruta-epoxidacion-aceite.md`.
- **Notas de la doctora sobre la versión 03:** están en `entregables/03b_Propuesta_con_notas_Dra_Dulce.pdf` y transcritas en `documentos/notas-dra-dulce-17oct.md`.
- **Textos corregidos sin contradicciones** para las secciones 2 a 6: `documentos/redaccion-corregida-propuesta.md`.
- **Alcance:** sin cambios por ahora.
- **Diseño:** el modelo paramétrico y la animación están en curso y se suben al terminarlos.
- **Pendientes principales:** decidir la ruta de epoxidación (perfórmica vigente o peracético con resina, como propone el Estudio), investigar cuánto aceite retiene la malla y si se reusa, terminar el diseño, pasar los textos corregidos al docx, rehacer el dimensionamiento con la malla y las preguntas a la doctora (ver `CLAUDE.md`).

## Contenido

| Carpeta | Archivo | Qué es |
| --- | --- | --- |
| raíz | `CLAUDE.md` | Contexto vivo del proyecto: estado, datos, correcciones, riesgos, pendientes y bitácora |
| `contexto/` | `contextoReally.md` | Resumen del trabajo hasta el 16 oct (versiones v0 a v3, evidencia, guía del reporte) |
| `contexto/` | `contexto-proyecto-recoleccion-aceite-con-polimeros.md` | Contexto detallado: hipótesis, clasificación del aceite, datos por hogar, impacto por región, faltantes y preguntas al acopiador |
| `contexto/` | `transcripcion-audios-asesora.md` | Transcripción de los tres audios de la asesora (Whisper "small", con partes dudosas) |
| `documentos/` | `propuestas-dra-dulce-columna-poliestireno.md` | Análisis de lo que propuso la doctora, literatura y cómo plantearlo en el reporte |
| `documentos/` | `consulta-tecnica-dra-dulce-poliestireno.md` | Consulta técnica completa para la doctora (dimensionamiento, siete preguntas, prueba de una hora) |
| `entregables/` | `01_Propuesta_equipo_para_Dra_Dulce_v1.pdf` | Propuesta del equipo de 3 hojas para la doctora, con patentes y proyectos similares |
| `entregables/` | `02_Consulta_tecnica_equipo_para_Dra_Dulce.pdf` | Consulta técnica completa del equipo para la doctora (8 páginas) |
| `entregables/` | `03_Propuesta_centrada_con_Dra_Dulce_casi_final.docx` y `.md` | Propuesta centrada con ayuda de la doctora, casi definitiva (la `.md` es una conversión para leerla en GitHub) |
| `entregables/` | `03b_Propuesta_con_notas_Dra_Dulce.pdf` | Versión 03 con las notas escritas de la doctora (17 oct) |
| `entregables/` | `Punto_6_Propuestas_descartadas.md` y `Formato_obligatorio_con_Punto_6_Propuestas_descartadas.docx` | Punto 6 del formato (10 propuestas descartadas, con razones, notas y referencias); el docx es el formato con el punto 6 ya pegado |
| `formato/` | `Formato_obligatorio_Reporte_Pautado_Rally_2026.docx` | Formato obligatorio del reporte de pautado (7 puntos) |
| `documentos/` | `verificacion-puntos-5-y-6.md` | Revisión de si el material alcanza para los puntos 5 y 6 del formato |
| `documentos/` | `notas-dra-dulce-17oct.md` | Notas de la doctora sobre la versión 03 y cómo se atiende cada una |
| `documentos/` | `ruta-epoxidacion-aceite.md` | Epoxidación del aceite recuperado: rutas, calentamiento accesible (baño María a 55–60 °C), acidez, productos y fuentes |
| `documentos/` | `actualizacion-disolvente-acetona.md` | Cambio de disolvente a acetona: proceso, comparación con el limoneno y sus residuos, regulación y seguridad |
| `documentos/` | `redaccion-corregida-propuesta.md` | Textos de las secciones 2 a 6 sin contradicciones, dentro de los límites de caracteres |
| `referencias/` | `Estudio_EPS_AVU_3_etapas.pdf` | Estudio técnico-bibliográfico del equipo (17 oct): disolvente para el unicel (recomienda d-limoneno; el equipo usa acetona y deja el limoneno como alternativa), inversión de fases contra electrohilado y rutas de epoxidación |
| `referencias/` | `IDEAS_1_columna_EPS_o_PU.pdf` | Reporte de investigación: columna bajo tarja con EPS o PU reciclado (el PU ya se descartó) |
| `referencias/` | `consulta-tecnica-columna-PU.pdf` | Consulta técnica anterior, con espuma de poliuretano (historial; PU descartado por precio) |
| `scripts/` | `build_pdf.py` | Script con el que se generó el PDF de 3 hojas (ReportLab) |

Documentos en línea (Claude): [Propuestas de la Dra. Dulce](https://claude.ai/code/artifact/2c76dd6f-472a-4ea7-bef6-bedf1a94e010) · [Consulta técnica](https://claude.ai/code/artifact/c6aeb3c3-2423-4730-8e22-2729f72f9df4)
