# 📄 Contrato de Desarrollo de Software

**Ejercicio Académico — Curso Gestión de Proyectos de Software**

\---

> ⚠️ \*\*Documento de carácter exclusivamente académico — Sin efectos jurídicos reales.\*\*

\---

## Partes del Contrato

|Parte|Rol|Datos|
|-|-|-|
|Universidad del Valle — Seccional Zarzal|**EL CLIENTE**|Calle 14 # 14-00, Zarzal, Valle del Cauca · NIT: 890.399.694-0|
|RISE S.A.S.|**EL DESARROLLADOR**|Zarzal, Valle del Cauca, Colombia · NIT: 900-XXX-XXX-X (Simulado)|

En el municipio de Zarzal, Departamento del Valle del Cauca, República de Colombia, a los \_\_\_ días del mes de \_\_\_\_\_\_\_\_\_\_ de 2026, se celebra el presente Contrato de Desarrollo de Software entre:

**EL CLIENTE:** Universidad del Valle — Seccional Zarzal · NIT: 890.399.694-0 · Dirección: Calle 14 # 14-00, Zarzal, Valle del Cauca · Representante Legal: \[Nombre del Director de Seccional] · Cargo: Director Seccional.

**EL DESARROLLADOR:** RISE S.A.S. · NIT: 900-XXX-XXX-X (Simulado) · Dirección: Zarzal, Valle del Cauca, Colombia · Representante Legal: \[Nombre del Socio Fundador] · Cargo: Gerente General — Representante Legal.

\---

## Cláusula 1 · Objeto del Contrato

EL DESARROLLADOR se compromete a diseñar, desarrollar y entregar el software denominado **Sistema de Asignación de Salones para la Universidad del Valle, Seccional Zarzal**, que consiste en una interfaz web funcional que integra un algoritmo genético adaptativo ya desarrollado en Python para la asignación automatizada de salones académicos, considerando restricciones de capacidad, tipo de espacio, franjas horarias, accesibilidad y desplazamiento entre las sedes Bolívar y Balsas.

El desarrollo se ejecutará bajo la metodología **SCRUM**, estructurado en **5 sprints de 2 semanas calendario** cada uno, con una fecha máxima de entrega del producto final el **8 de junio de 2026**.

El alcance detallado, los entregables por sprint y las especificaciones técnicas se encuentran en el **Anexo 1** (Alcance y Entregables) y el **Anexo 2** (Especificaciones Técnicas), que forman parte integral del presente contrato.

\---

## Cláusula 2 · Estructura de Sprints y Pagos

### 2.1. Planificación de Sprints

Cada sprint tendrá una duración de 2 semanas calendario. Los entregables de cada sprint serán definidos en el documento de Alcance y Entregables (Anexo 1), entregado a EL DESARROLLADOR en cada reunión de Sprint Planning. EL CLIENTE aprobará los entregables de cada sprint mediante un **Acta de Aceptación** firmada por su representante o delegado.

|Sprint|Período|Milestone cubierto|Entregable principal|
|-|-|-|-|
|Sprint 1|16 mar – 31 mar 2026|M1 · Fundación y configuración|Autenticación por roles + módulo de parámetros generales y datos maestros operativo|
|Sprint 2|1 abr – 30 abr 2026|M4 · Integración del algoritmo|Algoritmo Python integrado como servicio web, ejecutable desde la interfaz con visualización de progreso|
|Sprint 3|1 may – 15 may 2026|M2–M3 · Programación académica|Módulos de registro de programación, validación previa y gestión de asignaturas, docentes y grupos|
|Sprint 4|16 may – 29 may 2026|M4–M5 · Horarios y publicación|Visualización gráfica de horarios, ajuste manual, exportación CSV y publicación para consulta|
|Sprint 5|30 may – 8 jun 2026|M5 · Validación y entrega final|Pruebas de aceptación con usuarios reales, correcciones, documentación técnica y entrega final estable|

### 2.2. Pagos

En el marco del presente ejercicio académico, el pago estipulado es simbólico y no refleja tarifas de mercado real, conforme a la Cláusula 7 (Naturaleza Didáctica). Los montos se expresan en la unidad monetaria académica del curso (CM$).

|Concepto|Monto (CM$)|Condición de pago|
|-|-|-|
|Pago por sprint (× 5 sprints)|COP$ 1.000.000 c/u|50% al inicio del sprint · 50% al aprobar el entregable|
|Primer pago — Sprint 1 (anticipo)|COP$ 500.000|Al inicio del Sprint 1|
|Pago por aprobación de entregable|COP$ 500.000 c/sprint|Contra Acta de Aceptación firmada por EL CLIENTE|
|**TOTAL DEL CONTRATO**|**COP$ 5.000.000**|Distribuido en los 5 sprints|

### 2.3. Penalización por Entrega Tardía

En caso de que EL DESARROLLADOR no entregue los entregables acordados dentro de la fecha límite de cada sprint, se aplicará una **penalización del 10 %** sobre el monto del sprint afectado (COP$ 100.000 por sprint), deducible del pago del sprint siguiente. La penalización no aplica cuando el retraso sea consecuencia de fuerza mayor debidamente documentada, conforme a la Cláusula 5.

\---

## Cláusula 3 · Propiedad Intelectual y Derechos

### 3.1. Titularidad del Código y Activos

EL CLIENTE (Universidad del Valle — Seccional Zarzal) será **dueño exclusivo** de todos los derechos de propiedad intelectual derivados del presente contrato, incluyendo el código fuente, componentes frontend en React, servicios backend en Django, esquemas de base de datos en Supabase, documentación técnica y cualquier otro activo generado en el marco del desarrollo.

EL DESARROLLADOR cederá de forma irrevocable todos los derechos de propiedad intelectual al finalizar el alcance del proyecto o los 5 sprints planeados, mediante un documento de cesión formal adjunto al Acta de Entrega Final.

### 3.2. Confidencialidad del Desarrollo

EL DESARROLLADOR se compromete a no divulgar la arquitectura del sistema, el código fuente, la lógica del algoritmo genético adaptativo, los datos institucionales utilizados para pruebas, ni ninguna información técnica o estratégica a terceros ajenos al presente contrato, durante la ejecución del mismo y por un período de **12 meses** posteriores a su terminación.

\---

## Cláusula 4 · Garantías y Mantenimiento

### 4.1. Pruebas de Aceptación

EL CLIENTE estará a cargo del diseño y ejecución de las pruebas de aceptación de cada entregable. Las pruebas se realizarán con administradores y coordinadores reales de la Seccional Zarzal, usando datos académicos del semestre en curso. EL CLIENTE dispondrá de **3 días hábiles** por sprint para revisar y aprobar o rechazar el entregable mediante Acta de Aceptación.

### 4.2. Garantías del Software

EL DESARROLLADOR garantiza que:

* El software entregado estará libre de errores críticos que impidan su funcionamiento principal durante los **30 días** posteriores a la entrega final.
* Cumplirá con todos los requisitos funcionales y no funcionales detallados en el Anexo 2 (Especificaciones Técnicas), incluyendo la correcta integración del algoritmo genético adaptativo y la cobertura del 95 % en pruebas unitarias.
* El sistema resolverá conflictos de asignación con una **tasa de éxito igual o superior al 90 %**, validada con datos reales de la seccional.

### 4.3. Soporte Post-Lanzamiento

EL DESARROLLADOR brindará soporte técnico por **3 meses** tras la entrega final del Sprint 5, incluyendo:

* Corrección de bugs críticos con tiempo de respuesta máximo de **24 horas hábiles**.
* Ajustes menores hasta **10 horas mensuales** sin costo adicional para EL CLIENTE.
* El soporte se prestará de manera remota a través de los canales acordados entre las partes.

\---

## Cláusula 5 · Terminación del Contrato

### 5.1. Causales de Terminación

* Incumplimiento reiterado de plazos: más de 2 sprints entregados con retraso injustificado.
* Entregables no aprobados en 2 revisiones consecutivas por el mismo sprint, sin corrección satisfactoria.
* Incumplimiento grave de la cláusula de confidencialidad (Cláusula 3.2).
* Acuerdo mutuo entre las partes, formalizado por escrito.

### 5.2. Efectos de la Terminación

* EL CLIENTE pagará únicamente por los sprints cuyo entregable haya sido formalmente aprobado mediante Acta de Aceptación.
* EL DESARROLLADOR entregará todo el código fuente, documentación y activos generados hasta la fecha de terminación, en el estado en que se encuentren.
* Las cláusulas de confidencialidad (3.2) y propiedad intelectual (3.1) conservarán su vigencia tras la terminación del contrato.

### 5.3. Caso Fortuito y Fuerza Mayor

Las partes quedan exoneradas de responsabilidad por el incumplimiento de sus obligaciones cuando dicho incumplimiento sea consecuencia directa de un evento de fuerza mayor o caso fortuito, debidamente invocado y constatado conforme a la ley colombiana (Código Civil, artículo 64) y la jurisprudencia de la Corte Suprema de Justicia. En tal caso, la parte afectada deberá notificar a la otra de forma inmediata y por escrito.

\---

## Cláusula 6 · Confidencialidad

Ambas partes se comprometen a mantener estricta confidencialidad sobre los términos económicos del contrato, la información técnica del sistema, los datos institucionales de la Universidad del Valle utilizados durante el desarrollo y las pruebas, y las estrategias comerciales o académicas de cualquiera de las partes. Esta obligación se extenderá por **12 meses** posteriores a la terminación del contrato por cualquier causa.

\---

## Cláusula 7 · Naturaleza Didáctica y Prevalencia

> ⚠️ \*\*Esta cláusula prevalece sobre cualquier otra disposición del contrato, anulando términos que le resulten contradictorios.\*\*

El presente contrato se suscribe en el marco de un ejercicio académico del Curso de Gestión de Proyectos de Software, con carácter exclusivamente didáctico y sin fines comerciales. Las partes reconocen que:

1. La relación «cliente–desarrollador» es simulada. El pago estipulado es simbólico en unidades monetarias académicas (COP$) y no refleja tarifas de mercado real.
2. La capacidad máxima de trabajo del Equipo Desarrollador se limita a **5 horas semanales** por cada desarrollador y **5 horas semanales** del Scrum Master, priorizando el aprendizaje sobre los resultados funcionales.
3. El objetivo principal es evaluar habilidades de gestión de proyectos (metodología, planificación, gestión de riesgos) y trabajo en equipo, bajo supervisión docente.
4. Se empleará la metodología SCRUM con sprints de 2 semanas. Las tareas se seleccionarán en reuniones de Sprint Planning mediante acuerdo entre las partes, priorizando el Product Backlog definido por EL CLIENTE y ajustándose a la capacidad operativa del equipo.
5. **Esta cláusula prevalece sobre cualquier otra disposición del contrato, anulando términos que le resulten contradictorios.**

\---

## Cláusula 8 · Jurisdicción

El presente contrato se rige por las leyes de la República de Colombia, en particular por el Código Civil (Ley 84 de 1873), el Código de Comercio (Decreto 410 de 1971) y la Ley 23 de 1982 sobre Derechos de Autor. Cualquier disputa que surja en relación con la ejecución, interpretación o terminación del presente contrato será resuelta en primera instancia mediante negociación directa entre las partes. De no llegarse a un acuerdo, las controversias se someterán a los tribunales competentes del municipio de **Zarzal, Valle del Cauca, Colombia**.

\---

## Firmas

En constancia de lo anterior, las partes suscriben el presente contrato en dos (2) ejemplares del mismo tenor y valor, en la fecha y lugar indicados en el encabezado.

|||
|-|-|
|**EL CLIENTE**|**Fecha:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|
|\[Nombre del Representante Legal]|**C.C. / NIT:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|
|Director Seccional — Universidad del Valle, Seccional Zarzal||
|NIT: 890.399.694-0||

|||
|-|-|
|**EL DESARROLLADOR**|**Fecha:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|
|\[Nombre del Representante Legal de RISE S.A.S.]|**C.C. / NIT:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|
|Gerente General — RISE S.A.S.||
|NIT: 900-XXX-XXX-X||

|||
|-|-|
|**SUPERVISOR DOCENTE**|**Fecha:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|
|\[Nombre del Docente]|**C.C.:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|
|Docente — Curso Gestión de Proyectos de Software||

\---

## Anexo 1 · Alcance y Entregables por Sprint

Los siguientes entregables constituyen el alcance acordado para cada sprint. Cualquier modificación al alcance deberá ser acordada por escrito por ambas partes antes del inicio del sprint afectado.

|Sprint|Período|Historias de Usuario|Entregable / Criterio de aceptación|
|-|-|-|-|
|Sprint 1|16–31 mar|HU1, HU2, HU3, HU5, HU6, HU7|Módulo de autenticación por roles operativo + CRUD completo de datos maestros (salones, docentes, asignaturas, parámetros generales). Accesible desde la interfaz React con datos persistidos en Supabase.|
|Sprint 2|1–30 abr|HU9, HU10, HU11|Servicio Python del algoritmo expuesto vía API REST e integrado en Django. Ejecutable desde la interfaz con parámetros configurables. Validación previa, ejecución y plantilla gráfica del horario generado.|
|Sprint 3|1–15 may|HU4, HU8, HU16, HU17, HU18, HU19, HU20, HU21, HU22|Módulo de programación académica completo: registro de asignaturas por período, asignación de docentes, cupos, franjas, accesibilidad y tipo de espacio. Importación desde CSV/Excel operativa.|
|Sprint 4|16–29 may|HU12, HU13, HU14, HU15, HU23, HU24, HU25, HU26, HU27|Ajuste manual de asignaciones, historial de trazabilidad, exportación CSV, publicación de horarios y módulo de consulta pública con filtros por programa, semestre y docente.|
|Sprint 5|30 may–8 jun|Validación general|Pruebas de aceptación con usuarios reales de la seccional. Tasa de resolución ≥ 90 %. Corrección de hallazgos. Documentación técnica completa. Entrega del repositorio GitHub con CI/CD activo.|

\---

## Anexo 2 · Especificaciones Técnicas

### Stack Tecnológico

|Capa|Tecnología|Rol en el sistema|
|-|-|-|
|Frontend|React (organizado por features)|Interfaz de usuario: formularios, grillas de horarios, panel de ejecución del algoritmo y vistas de consulta pública|
|Backend|Django (patrón MVT)|API REST: endpoints en `views.py`, reglas de negocio en `services/`, entidades en `models.py`, rutas en `urls.py`|
|Base de datos|Supabase (PostgreSQL administrado)|Persistencia de todos los datos del sistema; preparado para extender con autenticación y realtime|
|Algoritmo|Python (servicio independiente)|Algoritmo genético adaptativo expuesto vía API, consumido por Django; parámetros configurables desde la interfaz|
|CI/CD|GitHub Actions|Pipeline de integración y despliegue continuo; cobertura de pruebas ≥ 95 % en servicios Django|
|Despliegue|Render|Hospedaje del backend Django y el servicio del algoritmo en entorno de producción accesible por URL pública|

### Requisitos No Funcionales

* **Rendimiento:** el algoritmo debe retornar resultados en tiempo razonable para el volumen de datos de la seccional (hasta \~100 asignaturas).
* **Seguridad:** autenticación con roles diferenciados; rutas protegidas en el backend Django.
* **Usabilidad:** la interfaz debe ser legible y operable desde pantallas de escritorio y tablet sin entrenamiento especializado.
* **Trazabilidad:** todo cambio manual en el horario queda registrado con usuario, fecha/hora y detalle del cambio.
* **Escalabilidad:** la arquitectura Django por apps de dominio permite extender el sistema a otras seccionales regionales sin rediseño estructural.

### Repositorio y Entrega

* El código fuente se entregará en el repositorio GitHub del equipo, con historial de commits, ramas por feature y Actions configuradas.
* La documentación técnica incluirá: README con instrucciones de despliegue, diagrama de arquitectura, modelo de datos y manual de usuario básico.

\---

*RISE S.A.S. · "Donde tu idea se convierte en solución" · Renovamos, Impulsamos y Solucionamos tu Empresa · Zarzal, Valle del Cauca, Colombia · Ejercicio académico 2026*

