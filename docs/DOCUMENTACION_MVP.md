# Plan MVP — Sistema de Asignación de Salones
**Universidad del Valle · Seccional Zarzal · 2026**

---

## Objetivo del MVP

Entregar un sistema funcional de extremo a extremo que permita: configurar el entorno académico, registrar datos maestros, programar asignaturas con sus restricciones, ejecutar el algoritmo de asignación de salones y publicar el horario resultante para consulta por parte de docentes y estudiantes.

---

## Alcance del MVP

El MVP cubre **22 historias de usuario** (86 puntos de historia) correspondientes a todas las HU con prioridad **Must have** del backlog. El criterio de selección garantiza que el flujo crítico completo quede operativo desde el primer release.

### Flujo cubierto

```
Autenticación → Configuración → Datos maestros → Programación académica
    → Validación → Algoritmo → Visualización → Publicación → Consulta
```

---

## Historias de usuario incluidas

| ID | Historia | Milestone | Sprint | Pts | Valor |
|----|----------|-----------|--------|-----|-------|
| HU1 | Iniciar sesión según rol | M1 | 1 | 3 | 8 |
| HU2 | Gestionar cuentas y roles de usuarios | M1 | 1 | 5 | 7 |
| HU3 | Configurar parámetros generales del sistema | M1 | 1 | 5 | 9 |
| HU4 | Definir grupos por asignatura | M2 | 2 | 3 | 7 |
| HU5 | Registrar salones disponibles | M2 | 2 | 5 | 10 |
| HU6 | Gestionar parámetros de docentes | M2 | 2 | 3 | 6 |
| HU7 | Gestionar configuración de asignaturas | M2 | 2 | 5 | 9 |
| HU16 | Registrar información básica de asignatura | M2 | 2 | 3 | 8 |
| HU17 | Registrar docente responsable por asignatura | M2 | 3 | 3 | 8 |
| HU18 | Registrar número de estudiantes por asignatura | M2 | 3 | 2 | 9 |
| HU19 | Definir día y franja horaria por asignatura | M3 | 3 | 3 | 10 |
| HU20 | Indicar estudiantes con discapacidad | M3 | 3 | 2 | 8 |
| HU21 | Indicar tipo de espacio requerido | M3 | 3 | 2 | 9 |
| HU22 | Editar programación antes del algoritmo | M3 | 3 | 3 | 7 |
| HU9 | Validar inconsistencias antes del algoritmo | M3 | 4 | 5 | 9 |
| HU10 | Ejecutar algoritmo de asignación de salones | M4 | 4 | 13 | 10 |
| HU11 | Visualizar horario generado en plantilla gráfica | M4 | 4 | 8 | 8 |
| HU23 | Visualizar horario semestral completo | M4 | 4 | 5 | 8 |
| HU14 | Publicar horarios generados | M5 | 5 | 3 | 9 |
| HU24 | Consultar horario por período académico | M5 | 5 | 3 | 9 |
| HU25 | Ver día, hora, sede y salón de cada clase | M5 | 5 | 2 | 9 |
| HU26 | Visualizar horario en plantilla visual | M5 | 5 | 5 | 8 |
| **Total** | | | | **86** | |

---

## Historias excluidas del MVP (Fase 2)

Las siguientes HU tienen prioridad **Should have** y no bloquean ningún flujo crítico. Se difieren a la siguiente fase de desarrollo.

| ID | Historia | Pts | Razón de exclusión |
|----|----------|-----|-------------------|
| HU8 | Importar programación desde CSV/Excel | 8 | El registro manual cubre el MVP; la importación masiva es una mejora de productividad |
| HU12 | Exportar horarios a CSV | 3 | La visualización en pantalla es suficiente para validar el MVP |
| HU13 | Modificar manualmente asignación de salón | 8 | El algoritmo genera el horario; ajustes manuales post-algoritmo son fase 2 |
| HU15 | Ver historial de cambios y trazabilidad | 5 | No hay edición manual en el MVP; no aplica aún |
| HU27 | Filtrar horarios por programa, semestre o docente | 3 | La consulta básica del horario cubre el MVP |
| **Total diferido** | | **27** | |

---

## Resumen de esfuerzo

| Concepto | Valor |
|----------|-------|
| HU incluidas en MVP | 22 de 27 |
| Puntos en MVP | 86 de 114 |
| Puntos diferidos a Fase 2 | 27 |
| Must have cubiertos | 100% (22/22) |
| Sprints planificados | 5 |
| Duración estimada | 10 semanas (~2 semanas por sprint) |

---

## Criterios de éxito del MVP

1. Un administrador puede configurar el sistema, registrar datos maestros y ejecutar el algoritmo sin intervención técnica en el código.
2. El algoritmo genera un horario válido para el volumen de datos real de la seccional.
3. El horario generado es publicable y visible para docentes y estudiantes con los datos completos (día, hora, sede, salón).
4. Todos los roles definidos (administrador, coordinador, docente, estudiante) pueden autenticarse y acceder únicamente a las funcionalidades correspondientes.

---

· Universidad del Valle, Seccional Zarzal · 2026
