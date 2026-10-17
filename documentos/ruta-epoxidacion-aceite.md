# Ruta del aceite recuperado: epoxidación

17 oct 2026. Responde a las notas de la Dra. Dulce sobre la propuesta (`entregables/03b_Propuesta_con_notas_Dra_Dulce.pdf`): proponer un producto de reacciones de epoxidación a temperatura ambiente, un epóxido "cíclico básico o lineal" para resinas, no dirigirlo a la industria cosmética ni farmacéutica (está regulada) e investigar la acidez. Los estudios se leyeron en resumen salvo que se indique otra cosa.

## Resumen

- **La epoxidación de aceite de cocina usado está publicada y funciona sin purificar mucho el aceite.** Con ácido perfórmico generado en el momento (agua oxigenada más ácido fórmico) se llegó a 84.2 % de conversión de los dobles enlaces a epóxido, con 96.3 % de selectividad, a 60 °C y 3 h (Bourkaib et al. 2025).
- **El calentamiento accesible alcanza y sobra.** Un baño María en cualquier estufa llega como máximo a unos 100 °C, y la reacción se debe mantener entre 55 y 60 °C. Por encima de 60 °C el epóxido se degrada: a 70 °C el número de oxirano cae rápido después del máximo (Budiyati et al. 2025), y subir la temperatura favorece la apertura del anillo (Campanella et al. 2008). A 100 °C se perdería el producto.
- **A temperatura ambiente la misma reacción es mucho más lenta.** Con la energía de activación reportada, a 25 °C va unas 13.6 veces más lenta que a 60 °C: unas 41 h en lugar de 3 h (cálculo abajo). Las rutas que sí trabajan a temperatura ambiente o cerca (dimetildioxirano y enzimas) cuestan más en reactivos.
- **La afirmación de la versión 03 de "oxidar solo con temperatura y el oxígeno del aire" no tiene fuente.** No encontramos ningún estudio que obtenga epóxidos así. Hay que quitarla.
- **Productos con respaldo:** plastificante para PVC hecho con aceite usado epoxidado, y componente de resinas epoxi curadas con anhídridos o aminas (este último está demostrado con aceite de linaza, no con aceite usado). Ninguno es cosmético ni farmacéutico.
- **La acidez importa** porque el ácido, el agua y el calor abren el anillo epóxido. Hay que medirla en cada lote y neutralizar o lavar si está alta.

## Qué es la reacción

Los aceites vegetales tienen cadenas de ácidos grasos con dobles enlaces C=C. Un perácido le entrega un oxígeno a cada doble enlace y lo convierte en un anillo de tres átomos (oxirano). Es la reacción de Prileschajew:

```
HCOOH + H2O2  ⇌  HCOOOH + H2O              (perácido generado en el mismo reactor)
–CH=CH–  +  HCOOOH  →  –CH(O)CH–  +  HCOOH   (epóxido; el ácido fórmico se regenera)
```

El anillo es la parte "cíclica"; la cadena grasa sigue siendo lineal. **Por confirmar con la Dra.:** qué quiso decir con "epóxido cíclico básico o lineal".

**Cuánto epóxido cabe en un aceite.** Depende del índice de yodo (IV, gramos de yodo por 100 g), que mide los dobles enlaces. El oxígeno oxiránico teórico máximo es:

$$\mathrm{OOC_{teo}}\,[\%] = \frac{X}{100 + X\,A_O}\,A_O\cdot 100,\qquad X = \frac{IV}{2A_I},\quad A_I = 126.9,\ A_O = 16$$

| Índice de yodo | OOC teórico máximo |
| --- | --- |
| 72 | 4.34 % |
| 100 | 5.93 % |
| 119 | 6.98 % |

Los aceites usados de Bogotá tuvieron IV de 72 a 119, valores que el autor considera adecuados para epoxidar (Rincón Vija 2018). Su producto llegó a 3.2 % de oxígeno oxiránico con unos 60 % de conversión. Eso implica un OOC teórico de unos 5.3 %, es decir, un IV de unos 89 dentro de ese rango (cálculo nuestro).

## Rutas comparadas

| Ruta | Condiciones reportadas | Resultado | Pureza que exige | ¿Temperatura ambiente? | Fuente |
| --- | --- | --- | --- | --- | --- |
| Ácido perfórmico in situ (H₂O₂ + ácido fórmico) | C=C : H₂O₂ : HCOOH = 1 : 2.7 : 0.8; 60 °C; 3 h | 84.2 % de OOC relativo y 96.3 % de selectividad, **con aceite de cocina usado** | El resumen no describe pretratamiento | No; a 25 °C unas 13.6 veces más lenta (cálculo abajo) | Bourkaib, Irinislimane y Belhaneche-Bensemra 2025, *Int. J. Environ. Stud.* 82(2) |
| Ácido perfórmico in situ con catalizador | H₂O₂ y ácido fórmico 2.0 : 1 sobre aceite; 0.5 % de catalizador; 55 °C | 70.6 % de conversión relativa, **aceite usado de palma** | No descrita | No; a 25 °C unas 6.5 veces más lenta | Azlan Raofuddin et al. 2023, *Natural Resources Forum* |
| Ácido peracético in situ con resina ácida (Amberlite IR-120) | No dadas en el resumen | Se compararon cinéticas con aceite refinado | **Sí:** filtrar y neutralizar, porque las impurezas desactivan el catalizador | No indicada | AIChE Annual Meeting 2024 |
| Ácido cítrico, sin catalizador sólido | No dadas en el resumen | Aceite usado epoxidado usado como plastificante de PVC, con propiedades comparables a películas comerciales; sin residuos sólidos | No descrita | No indicada | Suzuki et al. 2018, *European Polymer Journal* (UFMG) |
| Dimetildioxirano (Oxone y acetona) en microemulsión | pH 7–8, Oxone : aceite = 2 : 1 | 100 % de conversión en girasol y canola, sin subproductos importantes | Aceites comerciales | El resumen no da la temperatura; este reactivo suele usarse a temperatura ambiente (de memoria, sin fuente leída) | Mukamurara, Mahamat Ahmat y Kaliaguine 2026 |
| Quimioenzimática (lipasa Novozym 435 + H₂O₂) | 45 °C, 16 h, tolueno y agua | Más de 99 % de conversión (ésteres metílicos de aceites de uva, aguacate y oliva comerciales) | Aceites comerciales, transesterificados | Cerca: 45 °C | Sustaita-Rodríguez et al. 2018, *Chemistry Central Journal* 12:39 |
| "Solo temperatura y aire" | — | No encontramos estudios que obtengan epóxidos así | — | — | Sin fuente |

Ventajas y costos de las rutas suaves:

- **Enzimática.** La lipasa forma el perácido a partir de ácidos grasos. El aceite usado ya trae ácidos grasos libres, y los autores proponen que la lipasa también los genera; ese mecanismo es propuesto, no probado. Según Fraunhofer IGB, la ruta enzimática es más selectiva, evita casi toda la apertura del anillo y no usa ácidos minerales fuertes. Su costo es la enzima.
- **Oxone.** Gasta unos 2 kg de Oxone por kilo de aceite, según la relación reportada, y deja sales.

**Cálculo de la velocidad a temperatura ambiente.** Las cinéticas reportadas son de pseudo primer orden: $k(T) = A\,e^{-E_a/RT}$, y el tiempo para una misma conversión escala con $1/k$:

$$\frac{k(25\ ^\circ\mathrm{C})}{k(60\ ^\circ\mathrm{C})} = \exp\!\left[-\frac{E_a}{R}\left(\frac{1}{298.15} - \frac{1}{333.15}\right)\right]$$

- Con $E_a = 14.7$ kcal/mol (61.5 kJ/mol; Bourkaib 2025) el cociente es 0.074. Las 3 h a 60 °C pasan a unas 41 h a 25 °C.
- Con $E_a = 50.55$ kJ/mol (Azlan Raofuddin 2023, a 55 °C) el cociente es 0.155, unas 6.5 veces más lento.

Esto supone que el mecanismo no cambia y que el agua oxigenada no se descompone en ese tiempo. Ninguna de las dos cosas está comprobada.

## Calentamiento accesible (hasta unos 100 °C)

El calor que se consigue en cualquier entorno es el del agua hirviendo, que no pasa de unos 100 °C. La reacción no necesita tanto: la ventana útil es de 55 a 60 °C.

| Temperatura | Qué reportan | Fuente |
| --- | --- | --- |
| ≤ 40 °C | Con agua oxigenada concentrada (hasta 60 % en peso), el proceso a temperatura moderada superó al convencional en conversión, productividad y selectividad (ésteres metílicos de soya) | Campanella, Fontanini y Baltanás 2008, *Chem. Eng. J.* 144(3) |
| 55 °C | 70.6 % de conversión relativa con aceite usado de palma | Azlan Raofuddin et al. 2023 |
| 60 °C | 84.2 % de conversión y 96.3 % de selectividad con aceite de cocina usado, en 3 h | Bourkaib et al. 2025 |
| 60 °C | Óptimo con aceite de semilla de hule, máximo hacia los 210 min | Budiyati, Rahmah y Fauzi 2025, *Eng. Proc.* 84(1):3 |
| 70 °C | El número de oxirano llega a su máximo y luego cae bruscamente | Budiyati et al. 2025 |
| Más alta | "Significativamente perjudicial"; aumenta la apertura del anillo por los ácidos fórmico y perfórmico | Campanella et al. 2008 |

**Cómo hacerlo con equipo común:** un frasco de vidrio con tapa floja dentro de una olla con agua (baño María), un termómetro de cocina y agitación.
- El baño María pone un tope natural de unos 100 °C y amortigua los cambios de temperatura.
- Se mantiene entre 55 y 60 °C ajustando el fuego.
- El agua oxigenada al 30 % es la de uso comercial. La de 60 % del estudio de Campanella es más peligrosa y no es "de cualquier entorno".
- Agregar el agua oxigenada poco a poco y no tapar herméticamente, porque la reacción desprende calor y gas. Esto es práctica general de laboratorio que no verificamos en una fuente.
- El ácido fórmico y el agua oxigenada concentrados son corrosivos. Aun con equipo común, la reacción se haría en un laboratorio o planta aliada, no en casa.

## Acidez (nota de la Dra.)

- **Por qué importa.** El medio ácido, el agua y la temperatura abren el anillo epóxido y forman dioles. Eso baja el rendimiento si el producto buscado es el epóxido. Fraunhofer IGB lo menciona como la reacción secundaria indeseable de la ruta química. Azlan Raofuddin et al. (2026) hacen esa apertura a propósito para obtener ácido dihidroxiesteárico, con ácido cítrico más sulfúrico a 70 °C.
- **Qué trae el aceite usado.** Su acidez, peróxidos, compuestos polares y color varían mucho con la forma de freír (Rincón Vija 2018). El aceite que se recupera de la cámara de calma y de la malla además trae agua y detergente. Hasta medirlo, se trata como de acidez alta (ver la clasificación en el contexto del proyecto).
- **Pretratamiento con respaldo.** Filtrar y neutralizar (AIChE 2024). Desgomar y blanquear con agua oxigenada, que redujo el color 74.2 % y quitó 1.2 % de sólidos hidratables en una etapa (Rincón Vija 2018). Secar antes de reaccionar.
- **Medición por lote.** Índice de acidez por titulación con KOH: $AV = 56.1\,N\,V/m$ (mg KOH/g), con $N$ la normalidad del KOH, $V$ los mL gastados y $m$ los gramos de muestra. También índice de yodo y agua.
- **Sin umbral publicado.** No encontramos un límite de acidez para epoxidar aceite usado. Proponemos registrarla y fijar el corte con la Dra.
- **Fibras de poliestireno.** El aceite que sale de la malla debe filtrarse para que no lleve fibras. Inferimos que el poliestireno resiste ácidos diluidos, pero no lo verificamos para estas condiciones.

## Qué producto proponer

| Producto | Respaldo | Comentario |
| --- | --- | --- |
| Plastificante para PVC | Suzuki et al. 2018 (aceite usado epoxidado, desempeño comparable al comercial). Chaiyaraksa et al. 2025, *Key Eng. Mater.* 1017 (aceite doméstico usado; la mejor mezcla fue 100 % aceite epoxidado, sin DOP) | Sustituye ftalatos tóxicos como el DOP. Es el producto con más evidencia usando aceite usado |
| Componente de resina epoxi | Fonseca 2025, UFRGS: aceite de linaza epoxidado con Oxone, curado con anhídrido metiltetrahidroftálico o con la amina Priamine 1071 | Con aceite usado no se encontró; el aceite usado tiene menos dobles enlaces que la linaza |
| Intermedio para polioles o dioles | Azlan Raofuddin et al. 2026 (ácido dihidroxiesteárico a partir de aceite usado) | Abre otra salida si el epóxido se degrada |
| Cosméticos o fármacos | — | **Excluido** por indicación de la Dra.: sector regulado |

## Cómo no contradecir el descarte anterior

El biorrecubrimiento descartado consistía en epoxidar el aceite y formular nosotros una resina con MDI para recubrir fertilizante. Se descartó por la investigación y el costo de la resina. Lo que se propone ahora es distinto: entregar **aceite epoxidado como materia prima** a quien fabrica plastificantes o resinas, sin formular la resina. Así se debe redactar en la sección de propuestas descartadas.

## Propuesta para el reporte

El aceite recuperado del filtro se pretrata de forma sencilla: filtrar, secar y neutralizar si su acidez es alta. Luego se epoxida con ácido perfórmico generado en el reactor a partir de agua oxigenada al 30 % y ácido fórmico, que es la ruta con más datos usando aceite de cocina usado (84.2 % de conversión). La reacción se mantiene a 55–60 °C durante unas 3 h en baño María, un calentamiento que se logra con cualquier estufa y que nunca pasa de unos 100 °C. No se calienta más porque arriba de 60 °C el epóxido se degrada. El aceite epoxidado se destina a plastificantes de PVC o a resinas epoxi, no a cosméticos ni fármacos.

La epoxidación se haría en un laboratorio o planta aliada, no en casa.

Si la Dra. exige temperatura ambiente estricta, hay tres alternativas:

1. La misma reacción con más tiempo, del orden de 2 días (estimación nuestra).
2. Dimetildioxirano (Oxone y acetona), con más costo en reactivos.
3. La vía enzimática a unos 45 °C, con el costo de la enzima.

## Pendientes

1. Confirmar con la Dra. qué significa "epóxido cíclico básico o lineal" y si acepta el baño María a 55–60 °C en lugar de temperatura ambiente estricta.
2. Conseguir los textos completos de Bourkaib 2025 y Suzuki 2018: pretratamiento, temperatura y reactivos exactos.
3. Fijar con la Dra. un umbral de acidez para epoxidar y el pretratamiento mínimo.
4. Buscar un comprador o laboratorio aliado de aceite epoxidado, y su precio.

## Fuentes

- Budiyati, E.; Rahmah, A.; Fauzi, N. A. (2025). The in-situ epoxidation of rubber seed oil (*Hevea brasiliensis*) by peroxyacids. *Engineering Proceedings* 84(1):3. https://www.mdpi.com/2673-4591/84/1/3
- Campanella, A.; Fontanini, C.; Baltanás, M. A. (2008). High yield epoxidation of fatty acid methyl esters with performic acid generated in situ. *Chemical Engineering Journal* 144(3):466–475. https://ri.conicet.gov.ar/handle/11336/19782
- Bourkaib, N. E. H.; Irinislimane, R.; Belhaneche-Bensemra, N. (2025). Recycling used cooking oil into a biobased epoxide by experimental design using R. *International Journal of Environmental Studies* 82(2):1653–1669. https://dspace.univ-boumerdes.dz/items/850a7eae-7213-4c39-b7d5-015dbdbad649
- Azlan Raofuddin, D. N.; Azmi, I. S.; Rahim, N. H.; Jalil, M. J. (2023). Sustainable synthesis of epoxidized waste cooking oil via Prileschajew reaction. *Natural Resources Forum*. https://update.library.uitm.edu.my/Record/2-s2.0-85176937385/Details
- AIChE Annual Meeting (2024). Pre-treatment of used cooking oils and further epoxidation using Amberlite IR-120 catalyst. https://proceedings.aiche.org/conferences/aiche-annual-meeting/2024/proceeding/paper/pre-treatment-used-cooking-oils-and-further-epoxidation-using-amberlite-ir-120-catalyst
- Suzuki, A. H.; Botelho, B. G.; Oliveira, L. S.; Franca, A. S. (2018). Sustainable synthesis of epoxidized waste cooking oil and its application as a plasticizer for polyvinyl chloride films. *European Polymer Journal*. https://repositorio.ufmg.br/items/1e36d0c2-3a7b-4b12-b3c2-4f1bcffe5646
- Chaiyaraksa, C. et al. (2025). Cleaner bio-based plasticizer synthesis from waste cooking oil to substitute toxic dioctyl phthalate in PVC film. *Key Engineering Materials* 1017:103–108. https://dspace.kmitl.ac.th/items/0fb7f4f1-e560-4a20-b66d-414df29144e1/full
- Rincón Vija, L. A. (2018). Reutilización de aceites de cocina usados en la producción de aceites epoxidados. Tesis de maestría, Universidad Nacional de Colombia. https://repositorio.unal.edu.co/handle/unal/68873
- Mukamurara, D.; Mahamat Ahmat, Y.; Kaliaguine, S. (2026). Epoxidation of canola and sunflower oils using dimethyldioxirane in microemulsions. DOI 10.1021/acsomega.6c04347. https://www.citedrive.com/en/discovery/epoxidation-of-canola-and-sunflower-oils-using-dimethyldioxirane-in-microemulsions/
- Sustaita-Rodríguez, A. et al. (2018). Epoxidación quimioenzimática de ésteres metílicos de aceites de uva, aguacate y oliva (descripción nuestra; título exacto por confirmar). *Chemistry Central Journal* 12:39. https://link.springer.com/article/10.1186/s13065-018-0409-2
- Fraunhofer IGB. Preparation of triglyceride and fatty acid epoxides (chemo-enzymatic). https://www.igb.fraunhofer.de/en/research/industrial-biotechnology/bioprocess-engineering/establishment-and-scale-up-of-technical-enzyme-processes/preparation-of-triglyceride-and-fatty-acid-epoxides.html
- Fonseca, C. S. (2025). Estudo da cinética de cura de resina epoxídica baseada em óleo de linhaça com endurecedores do tipo anidrido e amina. Disertación, UFRGS. https://lume.ufrgs.br/handle/10183/291664
- Azlan Raofuddin, D. N. et al. (2026). Catalytic epoxidation and subsequent conversion of waste cooking oil to dihydroxystearic acid using citric and sulfuric acid. DOI 10.1515/ijcre-2026-0029.
