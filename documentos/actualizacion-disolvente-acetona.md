# Actualización del disolvente: acetona (d-limoneno como alternativa)

Equipo Oilx-Force · Rally 2026 · 17 de octubre de 2026

Aplicado al repositorio el 17 oct (CLAUDE.md, README, redacción, punto 6 y notas). Sin las preguntas para la doctora.

## 1. Qué cambia

| | Antes (repositorio) | Ahora |
|---|---|---|
| Disolvente del unicel | d-limoneno ("propuesta a investigar") | **Acetona** (la que mencionó la Dra. Dulce) |
| Baño para precipitar | Etanol | **Agua** (la acetona se mezcla con agua) |
| Recuperación del disolvente | Destilación de limoneno y etanol | Destilación de la mezcla acetona-agua |
| d-limoneno | Disolvente principal | **Alternativa**, con sus residuos considerados (sección 3) |

Lo que no cambia: malla de poliestireno expandido (unicel de empaque) reciclado, formada por inversión de fases; el electrohilado sigue descartado por costo; la malla se enrolla en el cartucho de polipropileno.

## 2. Proceso con acetona (puntos de partida a probar, no resultados)

1. Unicel de empaque limpio y seco (no unicel de construcción, que puede traer retardante de flama HBCD), en trozos pequeños.
2. Disolver en acetona, en recipiente de vidrio o metal con tapa, con agitación suave: de 10 a 20 % de poliestireno en peso como arranque. Colar para quitar etiquetas e impurezas.
3. Precipitar: mezclar la solución con un gran exceso de agua (empezar con 5 a 10 partes de agua por una de solución; por confirmar). La acetona pasa al agua y el poliestireno precipita poroso. También se puede recubrir un no tejido de polipropileno con la solución e inmersión en agua (la prueba que ya plantea el repositorio, cambiando etanol por agua).
4. Lavar con agua y secar por completo, antes de acercar la malla al cartucho.
5. Recuperar la acetona del baño por destilación.

Riesgo técnico principal (por probar): la precipitación en agua es muy rápida y puede formar una piel densa con poco poro. Hay que variar concentración y velocidad de adición y medir cuánto aceite retiene la malla.

## 3. Alternativa: d-limoneno, considerando residuos

| Aspecto | **Acetona (principal)** | **D-limoneno (alternativa)** |
|---|---|---|
| Baño de precipitación | Agua | Etanol (más caro) |
| Residuo líquido | Mezcla acetona-agua | Mezcla limoneno-etanol (orgánica, sin agua) |
| Recuperación por destilación | Fácil: la acetona hierve a unos 56 °C | Más costosa: el limoneno hierve a unos 176 °C |
| Restos en la malla | Pocos: se evapora rápido | Más persistentes: poco volátil; pueden pasar al aceite recuperado |
| Toxicidad acuática | Baja, pero no debe ir al drenaje | Alta (el repositorio lo marca tóxico acuático) |
| Otros riesgos | Muy inflamable, vapores | Inflamable (unos 48 °C), sensibilizante de piel; el repositorio señala que puede hinchar el polipropileno |
| Regulación en México | **Controlada** (ver sección 4) | Sin control conocido |

Regla de residuos para ambas: ningún baño ni disolvente al drenaje; se juntan, se destilan para reutilizar y lo que no se recupera se entrega como residuo del laboratorio.

## 4. Regulación: punto a verificar

La **acetona** y el **ácido sulfúrico** aparecen como "productos químicos esenciales" (fracción II del artículo 4) en la Ley Federal para el Control de Precursores Químicos, Productos Químicos Esenciales y Máquinas para Elaborar Cápsulas, Tabletas y/o Comprimidos (consultada en un compendio en línea, sdv.com.mx; falta contrastar con el DOF). Esto contradice el criterio "sin reactivos regulados". Consecuencias:

- La acetona debe comprarse con un proveedor que cumpla los avisos de la ley, o conseguirse a través del laboratorio o la doctora; no es para uso doméstico.
- En la propuesta, la acetona se usa **solo en la fabricación de la malla en laboratorio o planta**, nunca en el hogar. El usuario recibe un cartucho ya seco.
- La ruta de epoxidación del repositorio (ácido fórmico y agua oxigenada) no usa ácido sulfúrico; no reintroducir el sulfúrico como catalizador sin revisar esto.
- Falta confirmar si hay cantidades mínimas exentas para laboratorio.

## 5. Riesgos de seguridad de la acetona

Muy inflamable: sin flamas, parrillas ni chispas; ventilación o campana; guantes y lentes; recipiente cerrado. Evitar contacto con el prototipo impreso en PETG (la acetona puede dañarlo); fabricar la malla aparte y secarla antes de montarla.

## 6. Pendientes

- Contrastar la regulación de la acetona con el DOF y las cantidades de laboratorio.
- Medir acetona residual en la malla seca.
- Probar porosidad y retención de aceite (control: unicel en trozos).
- Confirmar que la acetona disuelva el unicel de empaque a 10–20 % sin quedar en gel: con parámetros de Hansen de tablas (citados de memoria) queda justo en el límite (RED ≈ 1.0).

## Fuentes

- Repositorio del equipo (README, CLAUDE.md, `redaccion-corregida-propuesta.md`): https://github.com/skully0418/Really2026 (leído en resumen; no se pudo abrir el PDF del estudio)
- Ley Federal para el Control de Precursores Químicos, art. 4 (compendio): https://sdv.com.mx/compendio/ley-federal-para-el-control-de-precursores-quimicos-productos-quimicos-esenciales-y-maquinas-para-elaborar-capsulas-tabletas-yo-comprimidos/articulo-4/
- US 8,546,455 B2 (disolución de EPS con acetona): https://patents.google.com/patent/US8546455
- US 7,728,047 B2 (recuperación de solvente por destilación): https://patents.google.com/patent/US7728047
