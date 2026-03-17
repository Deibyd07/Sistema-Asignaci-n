# 📋 Alcance y Entregables del Proyecto
**Sistema de Asignación de Salones — Universidad del Valle, Seccional Zarzal**

---

| Campo | Detalle |
|---|---|
| **Cliente (Product Owner)** | Universidad del Valle — Seccional Zarzal |
| **Desarrollador** | RISE S.A.S. |
| **Metodología** | SCRUM — 5 sprints de 2 semanas |
| **Fecha de inicio** | 16 de marzo de 2026 |
| **Fecha de entrega final** | 8 de junio de 2026 |
| **Versión del documento** | v1.0 — Marzo 2026 |

> 📌 **Nota Scrum:** Este documento es una declaración de intenciones y límites, no una biblia inamovible. El alcance es **variable y flexible**; el tiempo y el costo son **fijos**. Cualquier cambio de alcance debe ser acordado entre el Product Owner y el Scrum Master antes del Sprint Planning correspondiente.

---

## 1. Resumen Ejecutivo

### 1.1. Declaración de Visión del Producto

Proporcionar a la Universidad del Valle — Seccional Zarzal una plataforma web que elimine el proceso manual de asignación de salones, integrando un algoritmo genético adaptativo ya desarrollado para generar horarios académicos óptimos de forma automatizada. La herramienta permitirá a administradores y coordinadores gestionar, validar, ajustar y publicar horarios en un entorno centralizado, considerando las restricciones reales de las sedes Bolívar y Balsas, y sentará las bases técnicas para su adopción futura en otras seccionales regionales de la universidad.

### 1.2. Objetivos Estratégicos

- Reducir en un **30 % a 50 %** los conflictos de asignación de salones respecto al proceso manual actual, medido con datos reales del semestre en curso.
- Integrar el algoritmo genético adaptativo como servicio web ejecutable desde la interfaz, **sin intervención técnica** sobre el código fuente.
- Entregar una plataforma con roles diferenciados (administrador, coordinador, docente, estudiante) que cubra el ciclo completo: configuración → programación → generación → publicación → consulta.
- Validar el sistema con usuarios reales de la seccional antes de la entrega final, logrando una **tasa de resolución de conflictos ≥ 90 %**.
- Documentar la arquitectura de forma que la extensión a otras seccionales sea técnicamente viable **sin rediseño estructural**.

---

## 2. Stakeholders

| Rol | Nombre / Cargo | Responsabilidad en el proyecto |
|---|---|---|
| Product Owner (PO) | Representante de la Universidad del Valle — Seccional Zarzal | Define y prioriza el Product Backlog. Aprueba entregables mediante Acta de Aceptación. Participa en Sprint Reviews. |
| Scrum Master | Integrante del equipo RISE designado | Facilita las ceremonias Scrum, elimina impedimentos y asegura que el equipo siga la metodología. |
| Equipo de desarrollo | Desarrolladores de RISE S.A.S. | Diseñan, construyen y prueban los incrementos del producto en cada sprint. |
| Usuarios clave | Administradores y coordinadores de la seccional | Participan en pruebas de aceptación del Sprint 5 con datos académicos reales. |
| Usuarios finales | Docentes y estudiantes de la seccional | Consultan los horarios publicados a través de la interfaz pública del sistema. |
| Supervisor docente | Docente del curso Gestión de Proyectos de Software | Supervisa el proceso académico y evalúa la gestión del equipo. |

---

## 3. Product Backlog — Alcance Funcional

> El Product Backlog es el alcance dinámico del proyecto. Las épicas representan los grandes bloques de funcionalidad. El orden de implementación lo define el Product Owner según el valor de negocio de cada ítem.

### 3.1. Épicas del Sistema

| Épica | Descripción | Milestone | HUs incluidas | Prioridad |
|---|---|---|---|---|
| **E1 · Autenticación y configuración** | Control de acceso por roles y parametrización general del sistema (períodos, franjas, tipos de espacio). | M1 | HU1, HU2, HU3 | Must have |
| **E2 · Registro de datos maestros** | Gestión de salones, docentes, asignaturas y grupos que alimentan al algoritmo. | M2 | HU4, HU5, HU6, HU7 | Must have |
| **E3 · Programación académica** | Registro semestral de asignaturas por coordinadores: docente, cupo, franja, accesibilidad y tipo de espacio. | M3 | HU8, HU9, HU16–HU22 | Must have |
| **E4 · Motor de asignación** | Integración del algoritmo genético como servicio web, ejecución desde la interfaz y visualización de resultados. | M4 | HU10, HU11, HU13, HU15 | Must have |
| **E5 · Publicación y consulta** | Exportación CSV, publicación del horario y consulta pública con filtros para docentes y estudiantes. | M5 | HU12, HU14, HU23–HU27 | Must have |

### 3.2. MVP — Mínimo Producto Viable

El MVP es el conjunto mínimo de historias de usuario que debe estar operativo para que el sistema pueda usarse en producción real, cubriendo el flujo completo de extremo a extremo.

| HU | Descripción | Razón de inclusión en MVP |
|---|---|---|
| HU1 | Iniciar sesión según rol | Sin autenticación no hay sistema. |
| HU3 | Configurar parámetros generales | El algoritmo necesita franjas, tipos de espacio y períodos definidos. |
| HU5 | Registrar salones disponibles | Dato crítico de entrada para el algoritmo. |
| HU7 | Gestionar configuración de asignaturas | Dato crítico de entrada para el algoritmo. |
| HU17 | Registrar docente por asignatura | El algoritmo verifica conflictos de docente. |
| HU18 | Registrar número de estudiantes | Determina la capacidad mínima del salón. |
| HU19 | Definir día y franja horaria | Restricción fija del algoritmo. |
| HU9 | Validar inconsistencias antes del algoritmo | Evita ejecuciones con datos corruptos. |
| HU10 | Ejecutar algoritmo de asignación | Funcionalidad central del sistema. |
| HU11 | Visualizar horario en plantilla gráfica | El administrador debe poder validar el resultado. |
| HU14 | Publicar horarios generados | Sin publicación, docentes y estudiantes no pueden consultarlos. |
| HU24 | Consultar horario por período | Propósito final del sistema para los usuarios. |
| HU25 | Ver día, hora, sede y salón | Información mínima que necesita cualquier usuario. |

---

## 4. Entregables del Proyecto

### 4.1. Entregables de Software — Incrementos por Sprint

| Sprint | Período | Épicas | Incremento entregable |
|---|---|---|---|
| **Sprint 1** | 16–31 mar 2026 | E1 · E2 | Módulo de autenticación por roles (HU1–HU2) + configuración general (HU3) + CRUD completo de datos maestros: salones (HU5), docentes (HU6), asignaturas (HU7) y grupos (HU4). Interfaz React conectada a Supabase y endpoints Django operativos. |
| **Sprint 2** | 1–30 abr 2026 | E4 | Servicio Python del algoritmo expuesto vía API REST e integrado en Django. Ejecutable desde la interfaz con parámetros configurables. Validación previa (HU9), ejecución (HU10) y plantilla gráfica del horario generado (HU11). |
| **Sprint 3** | 1–15 may 2026 | E3 | Módulo de programación académica completo: registro de información básica (HU16), docente (HU17), estudiantes (HU18), franja horaria (HU19), accesibilidad (HU20), tipo de espacio (HU21) y edición previa al algoritmo (HU22). Importación desde CSV/Excel (HU8). |
| **Sprint 4** | 16–29 may 2026 | E4 · E5 | Ajuste manual de asignaciones (HU13), historial de trazabilidad (HU15), exportación CSV (HU12), publicación de horarios (HU14), visualización semestral para coordinador (HU23) y módulo de consulta pública con filtros (HU24–HU27). |
| **Sprint 5** | 30 may–8 jun 2026 | Validación | Pruebas de aceptación con administradores y coordinadores reales. Corrección de hallazgos. Documentación técnica completa (README, arquitectura, manual de usuario). Entrega del repositorio GitHub con CI/CD activo en Render. |

### 4.2. Entregables de Gestión — Documentación Scrum

| Artefacto Scrum | Descripción | Frecuencia |
|---|---|---|
| Product Backlog actualizado | Listado priorizado y estimado de todas las historias de usuario (HU1–HU27), mantenido vivo por el Product Owner. | Antes de cada Sprint Planning |
| Sprint Backlog | Subconjunto del Product Backlog comprometido para el sprint en curso, con tareas desglosadas por el equipo. | Al inicio de cada sprint |
| Acta de Aceptación | Documento firmado por el Product Owner que certifica la aprobación del incremento entregado. | Al final de cada sprint |
| Reporte de Burn-down | Gráfico que muestra el trabajo restante vs. el tiempo disponible en el sprint. Evidencia la velocidad del equipo. | Actualizado diariamente |
| Definition of Ready (DoR) | Lista de condiciones que debe cumplir una HU antes de poder entrar al Sprint Backlog. | Verificada en Sprint Planning |
| Definition of Done (DoD) | Lista de condiciones que debe cumplir un incremento para considerarse terminado. | Verificada en Sprint Review |
| Retrospectiva | Registro de lo que funcionó bien, lo que debe mejorar y las acciones concretas del equipo para el siguiente sprint. | Al cierre de cada sprint |

---

## 5. Acuerdos de Calidad — DoR y DoD

### 5.1. Definition of Ready (DoR)

Una Historia de Usuario está lista para entrar al Sprint Backlog cuando cumple **todos** los siguientes criterios:

- [ ] La HU está redactada en formato «Como [rol], quiero [objetivo], para [beneficio]».
- [ ] Tiene al menos 2 criterios de aceptación definidos en formato Gherkin (Dado / Cuando / Entonces).
- [ ] Tiene estimación en puntos de historia acordada por el equipo (serie Fibonacci).
- [ ] Tiene prioridad MoSCoW asignada por el Product Owner.
- [ ] No tiene dependencias bloqueantes sin resolver con otras HUs.
- [ ] El diseño de UI (si aplica) o el endpoint API está esbozado o acordado.
- [ ] El equipo entiende el alcance y puede desglosarla en tareas durante el Sprint Planning.

### 5.2. Definition of Done (DoD)

Un incremento de producto se considera terminado cuando cumple **todos** los siguientes criterios:

#### A — Nivel de tarea
- [ ] El código está implementado y cumple las convenciones del proyecto (PEP8 para Python, ESLint para React).
- [ ] Las pruebas unitarias están escritas y pasan con cobertura ≥ 95 % en los servicios Django.
- [ ] El código está integrado en la rama principal del repositorio GitHub sin conflictos.
- [ ] El gestor de tareas (GitHub Issues / Projects) está actualizado con el estado «Done».

#### B — Nivel de Historia de Usuario
- [ ] Todos los criterios de aceptación definidos en el DoR han sido verificados.
- [ ] Las pruebas de integración con el frontend React y el backend Django pasan sin errores críticos.
- [ ] El incremento es accesible desde la URL de despliegue en Render.
- [ ] El código está documentado con comentarios donde la lógica no es evidente.
- [ ] Cumple con los requisitos no funcionales aplicables (seguridad de rutas, validación de datos, accesibilidad).
- [ ] Aprobado por el Product Owner mediante Acta de Aceptación.

#### C — Nivel de Sprint
- [ ] Todas las HUs comprometidas en el Sprint Backlog están en estado Done o el equipo comunicó al PO cualquier ítem no completado.
- [ ] La Sprint Review se realizó con presencia del Product Owner.
- [ ] La Retrospectiva se realizó y se documentó al menos una acción de mejora.
- [ ] El Burn-down del sprint está actualizado y visible para el equipo.

#### D — Nivel de Entrega Final (Sprint 5)
- [ ] El sistema pasa las pruebas de aceptación con usuarios reales de la seccional con tasa de resolución ≥ 90 %.
- [ ] El repositorio GitHub contiene el código completo, historial de commits limpio y GitHub Actions configuradas.
- [ ] La documentación técnica está completa: README con instrucciones de despliegue, diagrama de arquitectura MVT + React, modelo de datos Supabase y manual de usuario básico.
- [ ] El código fuente y todos los activos han sido cedidos formalmente al cliente mediante el documento de cesión adjunto al contrato.

---

## 6. Límites del Proyecto — Out of Scope

> ⚠️ **Todo lo que aparece en esta sección NO será desarrollado en el alcance actual.** Cualquier solicitud de incorporar estos elementos implica una negociación formal de cambio de alcance con el Product Owner.

| ✅ Lo que SÍ incluye este proyecto | ❌ Lo que NO incluye (Out of Scope) |
|---|---|
| Asignación automatizada de salones para la Seccional Zarzal (sedes Bolívar y Balsas). | Integración con otros sistemas institucionales de la Universidad del Valle (SIA, Banner, etc.) en esta fase. |
| Gestión de roles: administrador, coordinador, docente y estudiante. | Aplicación móvil nativa (iOS / Android). Solo se entrega interfaz web responsiva. |
| Ejecución del algoritmo genético con parámetros configurables desde la interfaz. | Desarrollo o modificación del algoritmo genético en sí (ya está construido; solo se integra). |
| Exportación de horarios en formato CSV. | Exportación en formatos PDF, Excel o integración con Google Calendar en esta fase. |
| Publicación y consulta pública de horarios por parte de docentes y estudiantes. | Sistema de notificaciones automáticas (email, WhatsApp, push) ante cambios en el horario. |
| Ajuste manual de asignaciones con trazabilidad de cambios. | Módulo de gestión financiera, nómina docente o liquidación de contratos. |
| Arquitectura extensible a otras seccionales (documentada para uso futuro). | Despliegue real en infraestructura oficial de la Universidad del Valle. Solo se despliega en Render (entorno académico). |
| Soporte técnico por 3 meses post-entrega (bugs críticos y ajustes menores). | Soporte técnico indefinido o SLA garantizado más allá de los 3 meses estipulados en el contrato. |

---

## 7. Criterios de Aceptación de Incrementos

Cada incremento de producto será aceptado o rechazado por el Product Owner al final de cada sprint mediante el siguiente proceso:

| Paso | Responsable | Descripción |
|---|---|---|
| 1 · Sprint Review | Equipo RISE + PO | El equipo demuestra el incremento funcionando en el entorno de Render. Se ejecutan los escenarios de los criterios de aceptación de cada HU comprometida. |
| 2 · Validación funcional | Product Owner | El PO verifica que cada HU cumple sus criterios de aceptación Gherkin y el DoD. Dispone de **3 días hábiles** para la revisión. |
| 3 · Aprobación o rechazo | Product Owner | Si el incremento es **aprobado**: firma el Acta de Aceptación y se libera el pago del sprint. Si es **rechazado**: documenta los hallazgos; el equipo dispone de máximo 1 sprint para corregir. |
| 4 · Acta de Aceptación | Ambas partes | Documento firmado que certifica la entrega. Es el habilitador del pago por sprint definido en el contrato. |
| 5 · Entrega final — Sprint 5 | Equipo RISE + PO + Supervisor | Pruebas de aceptación con usuarios reales (administradores y coordinadores). Tasa de resolución ≥ 90 %. Entrega del repositorio, documentación y cesión de derechos. |

---

*RISE S.A.S. · "Donde tu idea se convierte en solución" · Documento vivo — v1.0 · Marzo 2026 · Sujeto a revisión en cada Sprint Planning · Universidad del Valle, Seccional Zarzal*
