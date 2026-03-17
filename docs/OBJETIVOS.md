# 🎯 Objetivos del Proyecto

**Sistema de Asignación de Salones — Universidad del Valle, Seccional Zarzal**

---

## Objetivo General

Desarrollar e implementar una interfaz web funcional para la Seccional Zarzal de la Universidad del Valle, que integre un algoritmo genético adaptativo ya construido en Python, con el fin de automatizar la asignación de salones considerando restricciones reales como capacidad de aulas, tipo de espacio, franjas horarias, accesibilidad para estudiantes con movilidad reducida y desplazamiento entre campus (sedes Bolívar y Balsas). La plataforma permitirá a administradores y coordinadores gestionar, generar, ajustar y publicar horarios académicos desde una sola herramienta, eliminando el proceso manual actual. Como proyección a futuro, la arquitectura de la plataforma se diseñará de forma que pueda extenderse a otras seccionales regionales de la universidad.

**Indicador de éxito:** reducción de conflictos de asignación en un 30 % a 50 % respecto al proceso manual actual, validada con datos reales del semestre en curso en la Seccional Zarzal.
**Fecha límite:** 8 de junio de 2026, con entregas parciales al cierre de cada milestone.

---

## Contexto técnico del algoritmo

El algoritmo genético adaptativo ya desarrollado opera sobre cuatro fuentes de datos (`asignaturas`, `docentes`, `franjas`, `salones`) y evoluciona una población de horarios durante hasta 200 generaciones. Su función de *fitness* penaliza solapamientos en salones, cambios de sede con menos de 120 minutos de margen (tanto para docentes como para estudiantes), y premia la agrupación de clases del mismo programa en la misma sede y día, así como la densidad horaria con huecos de hasta 60 minutos entre clases consecutivas. La generación inicial combina individuos heurísticos (30 %) que priorizan la sede Balsas con individuos aleatorios (70 %), y la probabilidad de mutación se ajusta dinámicamente según el nivel de estancamiento. Al finalizar, exporta el mejor horario encontrado y un reporte de asignaturas no asignadas con la razón de cada caso.

La interfaz web debe consumir este algoritmo como servicio, alimentarlo con los datos registrados en la plataforma y devolver los resultados al usuario de forma visual e interactiva.

---

## Objetivos Específicos

### Objetivo 1 — Configurar la plataforma con los datos maestros de la Seccional Zarzal

Construir los módulos de configuración y registro de datos que alimentan al algoritmo: períodos académicos, días laborables, franjas horarias, tipos de espacio, salones con su capacidad y sede (Bolívar / Balsas), asignaturas con su código, créditos e intensidad horaria, y parámetros de docentes como tipo de vinculación y valor por hora.

**¿Cómo se mide?**
Módulo de configuración operativo que permita registrar, editar y eliminar cada entidad de datos, con validaciones de integridad que impidan guardar registros incompletos o inconsistentes. Los datos deben ser consumibles directamente por el servicio del algoritmo sin transformaciones manuales.

**¿Por qué importa?**
El algoritmo trabaja sobre cuatro hojas de datos estructurados (`asignaturas`, `docentes`, `franjas`, `salones`). Si esa información no está correctamente registrada en la plataforma, el algoritmo producirá asignaciones incorrectas o dejará asignaturas sin salón. Esta capa de datos es el cimiento de todo el sistema.

> **Conexión con historias de usuario:** HU3 · HU5 · HU6 · HU7 · HU16 · HU17 · HU18

**Herramientas:** Django (`models.py` para entidades, `services/` para reglas de negocio, `views.py` para endpoints API), Supabase como PostgreSQL administrado, React para los formularios y vistas CRUD del frontend.
**Fecha límite:** 31 de marzo de 2026 (primeras 3 semanas del proyecto).

---

### Objetivo 2 — Integrar el algoritmo genético adaptativo como servicio web

Exponer el algoritmo desarrollado en Python como un servicio accesible desde la aplicación Laravel, de manera que un administrador pueda lanzar la ejecución directamente desde la interfaz, monitorear su progreso generación a generación y recibir el horario resultante junto con el reporte de asignaturas no asignadas, todo sin intervención técnica sobre el código fuente.

**¿Cómo se mide?**
El algoritmo debe ejecutarse desde la interfaz web con los parámetros configurables (tamaño de población, número de generaciones, proporción heurística y umbral de estancamiento), completar su ejecución en un tiempo razonable para los volúmenes de datos de la seccional, y retornar tanto el mejor horario encontrado como el listado de asignaturas no asignadas con su razón, sin errores de comunicación entre el servicio Python y Laravel.

**¿Por qué importa?**
Hoy el algoritmo corre en Google Colab sobre un archivo Excel que hay que preparar manualmente. Convertirlo en un servicio integrado elimina esa fricción, hace el proceso repetible y pone la herramienta en manos de los usuarios institucionales sin requerir conocimientos de programación.

> **Conexión con historias de usuario:** HU9 · HU10 · HU11 · HU13 · HU15

**Herramientas:** Python (algoritmo expuesto como servicio mediante Django o FastAPI), Django `views.py` como punto de entrada del endpoint de ejecución, `services/` para encapsular la lógica de invocación del algoritmo, React para el panel de control y la visualización del progreso, GitHub Actions para CI/CD, despliegue en Render.
**Fecha límite:** 30 de abril de 2026 (semanas 4 a 7).

---

### Objetivo 3 — Desarrollar los módulos de programación académica, visualización y publicación

Construir los módulos que completan el flujo institucional: registro de la programación académica semestral por parte del coordinador (asignatura, docente, grupo, estudiantes, franja, tipo de espacio y accesibilidad), validación previa a la ejecución del algoritmo, visualización gráfica del horario generado, ajuste manual de asignaciones, exportación a CSV y publicación para consulta de docentes y estudiantes.

**¿Cómo se mide?**
Los cinco milestones del sistema deben estar completos y operativos: autenticación por roles (HU1–HU2), datos maestros (HU3–HU7), programación académica (HU16–HU22), generación y gestión de horarios (HU8–HU15), y publicación y consulta (HU12, HU14, HU23–HU27). Cobertura del 95 % en pruebas unitarias y cero errores críticos en pruebas de aceptación con usuarios reales.

**¿Por qué importa?**
El algoritmo resuelve la asignación, pero el flujo completo involucra muchos pasos antes y después: el coordinador registra la programación, el administrador valida y ejecuta, y luego docentes y estudiantes consultan el resultado. Cada módulo cubre una parte de ese flujo que hoy se hace de forma fragmentada o manual.

> **Conexión con historias de usuario:** HU1 · HU2 · HU4 · HU6 · HU8 · HU12 · HU14 · HU16 · HU17 · HU18 · HU19 · HU20 · HU21 · HU22 · HU23 · HU24 · HU25 · HU26 · HU27

**Herramientas:** Django (apps por dominio: `usuarios`, `salones`, `horarios`, `reservas`; lógica en `services/`, endpoints en `views.py`), React (organizado por features: `src/features/salones/`, `src/features/horarios/`, etc.), Supabase PostgreSQL, exportación CSV, despliegue en Render.
**Fecha límite:** 22 de mayo de 2026 (semanas 8 a 11).

---

### Objetivo 4 — Validar la plataforma con datos reales de la Seccional Zarzal

Realizar pruebas de aceptación con administradores y coordinadores de la Seccional Zarzal usando datos académicos reales del semestre en curso, verificar que el algoritmo resuelve correctamente los conflictos de asignación considerando las dos sedes (Bolívar y Balsas) y sus restricciones de desplazamiento, corregir los hallazgos identificados y entregar una versión estable y documentada de la plataforma.

**¿Cómo se mide?**
Mínimo 2 sesiones de pruebas de aceptación con usuarios reales de la seccional, tasa de resolución de conflictos de asignación igual o superior al 90 %, y ningún error crítico pendiente en la versión de entrega. La arquitectura debe estar documentada de forma que una futura extensión a otras seccionales regionales sea técnicamente viable sin rediseñar el sistema desde cero.

**¿Por qué importa?**
Una herramienta que no ha sido probada con datos reales y usuarios reales no puede considerarse lista. Esta fase es la que confirma que el sistema funciona en las condiciones concretas de la Seccional Zarzal —con sus salones, sus programas, sus docentes y sus franjas— y que sienta las bases para que, en el futuro, otras seccionales regionales puedan adoptarla.

> **Conexión con historias de usuario:** HU9 · HU10 · HU11 · HU14 · HU15 · HU23 · HU24 · HU25 · HU26 · HU27

**Herramientas:** pruebas de aceptación con coordinadores y administradores, pytest sobre los servicios Django, React para verificación de flujos en el frontend, datos reales del semestre en curso almacenados en Supabase.
**Fecha límite:** 8 de junio de 2026 — versión estable, validada y documentada, lista para entrega final.

---

## Trazabilidad Objetivos ↔ Milestones ↔ Historias de Usuario

| Objetivo | Milestone | Historias de usuario relacionadas |
|---|---|---|
| OE1 — Datos maestros y configuración | M1 · Fundación · M2 · Registro de datos | HU3, HU5, HU6, HU7, HU16, HU17, HU18 |
| OE2 — Integración del algoritmo | M4 · Generación y gestión de horarios | HU9, HU10, HU11, HU13, HU15 |
| OE3 — Módulos de programación y publicación | M1 · M2 · M3 · M5 (todos) | HU1, HU2, HU4, HU8, HU12, HU14, HU19–HU22, HU23–HU27 |
| OE4 — Validación con datos reales | M4 · M5 · Generación, publicación y consulta | HU9–HU11, HU14, HU15, HU23–HU27 |

---

## Cronograma resumido 2026

| Período | Actividad principal | Milestone |
|---|---|---|
| 16 mar – 31 mar | Configuración y registro de datos maestros (salones, franjas, asignaturas, docentes) | M1 · M2 |
| 1 abr – 30 abr | Integración del algoritmo Python como servicio en Django + consumo desde React | M4 |
| 1 may – 22 may | Módulos de programación académica, visualización, ajuste manual y publicación | M2 · M3 · M5 |
| 23 may – 5 jun | Pruebas de aceptación con usuarios reales y corrección de hallazgos | M4 · M5 |
| 8 jun 2026 | Entrega final — plataforma estable, validada y documentada | M5 |

---

## Alineación con ODS y proyección regional

Este proyecto contribuye al **ODS 4 — Educación de calidad** al reemplazar un proceso manual de asignación de salones por una herramienta automatizada, trazable y accesible para toda la comunidad académica de la Seccional Zarzal. La plataforma se construye con foco en las necesidades concretas de esta sede —incluyendo la gestión de sus dos campus, Bolívar y Balsas, y sus restricciones de desplazamiento— pero con una arquitectura que, en el futuro, permita su adopción por otras seccionales regionales de la Universidad del Valle sin necesidad de rediseñar el sistema.

---

*Documento alineado con las historias de usuario del sistema (HU1–HU27) · Metodología ágil por milestones · Universidad del Valle, Seccional Zarzal · Entrega: 8 de junio de 2026*
