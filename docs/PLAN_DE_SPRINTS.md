# Planificación de Sprints — MVP Sistema de Asignación de Salones
**Universidad del Valle · Seccional Zarzal · 2026**

---

## Resumen general

| Sprint | Foco | Semanas | HU | Puntos |
|--------|------|---------|-----|--------|
| Sprint 1 | Autenticación y configuración | 1–2 | 3 | 16 |
| Sprint 2 | Catálogos maestros | 3–4 | 5 | 17 |
| Sprint 3 | Programación académica | 5–6 | 6 | 16 |
| Sprint 4 | Algoritmo y visualización del horario | 7–8 | 4 | 24 |
| Sprint 5 | Publicación y consulta | 9–10 | 4 | 13 |
| **Total** | | **10 semanas** | **22** | **86** |

---

## Sprint 1 — Autenticación y configuración del sistema

**Semanas:** 1–2 · **Milestone:** M1 · **Puntos:** 16

**Objetivo:** Dejar operativa la base del sistema: acceso por roles y configuración de los parámetros que habilitan todos los módulos posteriores (períodos académicos, franjas horarias, tipos de espacio).

### Historias de usuario

| ID | Historia | Rol | Pts | Valor |
|----|----------|-----|-----|-------|
| HU1 | Iniciar sesión según rol | Administrador | 3 | 8 |
| HU2 | Gestionar cuentas y roles de usuarios | Administrador | 5 | 7 |
| HU3 | Configurar parámetros generales del sistema | Administrador | 5 | 9 |

**Puntos totales:** 13

> El desfase de 3 puntos con respecto al promedio se reserva como capacidad de buffer para ajustes técnicos del entorno (configuración de Supabase, Django y React).

### Criterios de éxito del sprint

- [ ] Login funcional con redirección según rol (administrador, coordinador, docente, estudiante).
- [ ] Rutas protegidas por rol en el backend.
- [ ] CRUD de usuarios operativo desde la interfaz.
- [ ] Períodos académicos, franjas horarias y tipos de espacio configurables y persistentes.

---

## Sprint 2 — Catálogos maestros

**Semanas:** 3–4 · **Milestone:** M2 (parcial) · **Puntos:** 17 (incluye 3 pts de buffer)

**Objetivo:** Registrar todos los datos de referencia que el algoritmo necesita: salones, docentes, asignaturas y grupos. Al final del sprint el sistema tiene los insumos básicos para la programación académica.

### Historias de usuario

| ID | Historia | Rol | Pts | Valor |
|----|----------|-----|-----|-------|
| HU4 | Definir grupos por asignatura | Administrador | 3 | 7 |
| HU5 | Registrar salones disponibles | Administrador | 5 | 10 |
| HU6 | Gestionar parámetros de docentes | Administrador | 3 | 6 |
| HU7 | Gestionar configuración de asignaturas | Administrador | 5 | 9 |
| HU16 | Registrar información básica de asignatura | Coordinador | 3 | 8 |

**Puntos totales:** 19 *(incluye 2 pts de buffer para integración entre módulos)*

### Criterios de éxito del sprint

- [ ] CRUD completo de salones con validación de código único y atributo de accesibilidad.
- [ ] CRUD completo de docentes y asignaturas consumibles por el servicio del algoritmo.
- [ ] Grupos asociados a asignaturas sin duplicados.
- [ ] Coordinador puede registrar asignaturas en la programación del período activo.

---

## Sprint 3 — Programación académica

**Semanas:** 5–6 · **Milestone:** M2 (final) + M3 · **Puntos:** 16

**Objetivo:** Completar la información de programación de cada asignatura: docente responsable, cupo, franja horaria, accesibilidad y tipo de espacio requerido. Al cierre del sprint, todos los datos necesarios para ejecutar el algoritmo están cargados y editables.

### Historias de usuario

| ID | Historia | Rol | Pts | Valor |
|----|----------|-----|-----|-------|
| HU17 | Registrar docente responsable por asignatura | Coordinador | 3 | 8 |
| HU18 | Registrar número de estudiantes por asignatura | Coordinador | 2 | 9 |
| HU19 | Definir día y franja horaria por asignatura | Coordinador | 3 | 10 |
| HU20 | Indicar estudiantes con discapacidad | Coordinador | 2 | 8 |
| HU21 | Indicar tipo de espacio requerido | Coordinador | 2 | 9 |
| HU22 | Editar programación antes del algoritmo | Coordinador | 3 | 7 |

**Puntos totales:** 15

### Criterios de éxito del sprint

- [ ] Coordinador puede completar toda la ficha de programación de cada asignatura.
- [ ] El sistema impide franjas fuera de los días laborables configurados y rangos horarios inválidos.
- [ ] Las restricciones de accesibilidad y tipo de espacio quedan vinculadas al algoritmo.
- [ ] La edición es libre antes de la ejecución del algoritmo y genera advertencia si el algoritmo ya corrió.

---

## Sprint 4 — Algoritmo y visualización del horario

**Semanas:** 7–8 · **Milestone:** M3 (final) + M4 · **Puntos:** 24

**Objetivo:** Habilitar la ejecución del algoritmo de asignación y la visualización gráfica del resultado. Es el sprint de mayor peso técnico del proyecto por la complejidad de la HU10 (13 puntos).

### Historias de usuario

| ID | Historia | Rol | Pts | Valor |
|----|----------|-----|-----|-------|
| HU9 | Validar inconsistencias antes del algoritmo | Administrador | 5 | 9 |
| HU10 | Ejecutar algoritmo de asignación de salones | Administrador | 13 | 10 |
| HU11 | Visualizar horario generado en plantilla gráfica | Administrador | 8 | 8 |
| HU23 | Visualizar horario semestral completo | Coordinador | 5 | 8 |

**Puntos totales:** 31 *(el equipo deberá priorizar HU9 y HU10 en la primera semana del sprint)*

> **Nota técnica:** La HU10 involucra la integración Django → servicio Python del algoritmo con progreso en tiempo real. Se recomienda iniciar la integración técnica desde el Sprint 3 como spike, dejando la HU completamente funcional en este sprint.

### Criterios de éxito del sprint

- [ ] La validación previa detecta: asignaturas sin franja, sin docente, sin cupo, sin tipo de espacio y conflictos de docente.
- [ ] El botón de ejecución se habilita solo si la validación pasa sin errores críticos.
- [ ] El algoritmo se lanza desde la interfaz sin intervención técnica en el código.
- [ ] Los parámetros del algoritmo (población, generaciones, umbral de estancamiento) son configurables desde la UI.
- [ ] El progreso se muestra en tiempo real o mediante polling.
- [ ] La plantilla gráfica muestra el horario en formato grilla semanal con filtro por sede.
- [ ] Las asignaturas no asignadas se listan con su razón.

---

## Sprint 5 — Publicación y consulta

**Semanas:** 9–10 · **Milestone:** M5 · **Puntos:** 13

**Objetivo:** Cerrar el ciclo completo: publicar el horario generado y habilitarlo para consulta de docentes y estudiantes con la vista en grilla semanal.

### Historias de usuario

| ID | Historia | Rol | Pts | Valor |
|----|----------|-----|-----|-------|
| HU14 | Publicar horarios generados | Administrador | 3 | 9 |
| HU24 | Consultar horario por período académico | Docente / Estudiante | 3 | 9 |
| HU25 | Ver día, hora, sede y salón de cada clase | Usuario general | 2 | 9 |
| HU26 | Visualizar horario en plantilla visual | Usuario general | 5 | 8 |

**Puntos totales:** 13

### Criterios de éxito del sprint

- [ ] El administrador puede publicar y despublicar el horario del período activo.
- [ ] Solo se muestra el horario en estado "publicado" a docentes y estudiantes.
- [ ] La grilla semanal es la vista principal para usuarios generales, legible en escritorio y tablet.
- [ ] Cada clase muestra: asignatura, día, hora inicio, hora fin, sede y código de salón.

---

## Definición de listo (Definition of Ready)

Una HU entra al sprint solo si:

- [ ] Está estimada en puntos de historia.
- [ ] Tiene criterios de aceptación Gherkin aprobados por el Product Owner.
- [ ] Las dependencias técnicas del sprint anterior están resueltas.
- [ ] El diseño de la interfaz (si aplica) está disponible.

## Definición de hecho (Definition of Done)

Una HU se considera terminada cuando:

- [ ] El código pasa revisión de pares (pull request aprobado).
- [ ] Las pruebas unitarias tienen cobertura ≥ 95 % en servicios críticos.
- [ ] La funcionalidad es verificable en el entorno de staging.
- [ ] El Product Owner ha aprobado el comportamiento según los criterios de aceptación.

---

· Universidad del Valle, Seccional Zarzal · 2026*
