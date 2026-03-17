# 🔧 Issues Técnicas del Proyecto
**Sistema de Asignación de Salones — Universidad del Valle, Seccional Zarzal**

---

| Campo | Detalle |
|---|---|
| **Proyecto** | Sistema de Asignación de Salones |
| **Desarrollador** | RISE S.A.S. |
| **Total de issues** | 43 issues técnicas (TEC-00 a TEC-56) |
| **Entrega final** | 8 de junio de 2026 |

> 📌 Cada issue técnica es una tarea de infraestructura, arquitectura o soporte que el equipo debe completar para habilitar las historias de usuario funcionales. No aportan valor visible al usuario directamente, pero son el cimiento sobre el que todo funciona.

---

## Milestone 0 · Infraestructura y configuración base

> Sin HUs funcionales asociadas — Infraestructura base del proyecto.

---

### TEC-00 · Definir arquitectura base y convenciones

**Título GitHub:** `TEC-00 · Definir arquitectura base y convenciones`

Definir arquitectura base (Django API + React + PostgreSQL/Supabase) y convenciones del proyecto (estructura de carpetas, naming, estilo de código, branching strategy).

---

### TEC-01 · Configurar entornos dev, staging y prod

**Título GitHub:** `TEC-01 · Configurar entornos dev, staging y prod`

Configurar entornos (dev, staging, prod) con variables de entorno y secretos. Asegurar que ninguna credencial quede expuesta en el repositorio.

---

### TEC-02 · Configurar CI/CD mínimo

**Título GitHub:** `TEC-02 · Configurar CI/CD mínimo`

Configurar CI/CD mínimo con GitHub Actions: lint, tests, build y migraciones automáticas en cada push a la rama principal.

---

### TEC-03 · Configurar observabilidad y health checks

**Título GitHub:** `TEC-03 · Configurar observabilidad y health checks`

Configurar observabilidad: logging estructurado, manejo central de errores y health checks del servicio.

---

### TEC-04 · Configurar CORS, seguridad y rate limiting

**Título GitHub:** `TEC-04 · Configurar CORS, seguridad y rate limiting`

Configurar permisos CORS, políticas de seguridad HTTP y rate limiting básico para proteger los endpoints de la API.

---

### TEC-05 · Definir versionado de API y documentación OpenAPI

**Título GitHub:** `TEC-05 · Definir versionado de API y documentación OpenAPI`

Definir estrategia de versionado de API (ej. `/api/v1/`) y documentación automática con OpenAPI/Swagger.

---

### TEC-06 · Seed inicial de catálogos

**Título GitHub:** `TEC-06 · Seed inicial de catálogos`

Seed inicial de catálogos: roles, tipos de espacio, franjas horarias, días laborables y períodos de ejemplo.

---

## Milestone 1 · Fundación del sistema

> HUs relacionadas: **HU1 · HU2 · HU3**

---

### TEC-10 · Diseñar modelo de datos inicial

**Título GitHub:** `TEC-10 · Diseñar modelo de datos inicial`

Diseñar modelo de datos inicial en `models.py`: usuarios, roles, períodos académicos, días laborables, franjas horarias y tipos de espacio.

---

### TEC-11 · Crear migraciones iniciales y restricciones

**Título GitHub:** `TEC-11 · Crear migraciones iniciales y restricciones`

Crear migraciones iniciales y restricciones de base de datos: unicidad, claves foráneas (FK) e índices básicos en Supabase.

---

### TEC-12 · Implementar autenticación JWT con refresh y revocación

**Título GitHub:** `TEC-12 · Implementar autenticación JWT con refresh y revocación`

Implementar autenticación (JWT o sesión) con soporte de refresh tokens y revocación de sesiones.

---

### TEC-13 · Implementar autorización por rol en backend

**Título GitHub:** `TEC-13 · Implementar autorización por rol en backend`

Implementar autorización por rol (administrador, coordinador) en el backend Django. Las rutas deben estar protegidas según el rol del usuario autenticado.

---

### TEC-14 · Endpoint login/logout, perfil /me y middleware de seguridad

**Título GitHub:** `TEC-14 · Endpoint login/logout, perfil /me y middleware de seguridad`

Endpoint de login/logout + perfil del usuario autenticado (`/me`) + middleware de seguridad en `views.py`.

---

### TEC-15 · CRUD backend de usuarios y roles

**Título GitHub:** `TEC-15 · CRUD backend de usuarios y roles`

CRUD completo de usuarios y roles en el backend Django, con validaciones de negocio en `services/`.

---

### TEC-16 · CRUD backend de parámetros generales del sistema

**Título GitHub:** `TEC-16 · CRUD backend de parámetros generales del sistema`

CRUD backend de parámetros generales del sistema: períodos académicos, días laborables, franjas horarias y tipos de espacio.

---

### TEC-17 · Pantallas frontend de login y gestión de usuarios

**Título GitHub:** `TEC-17 · Pantallas frontend de login y gestión de usuarios`

Pantallas frontend en React para login, gestión de usuarios y configuración de parámetros generales del sistema.

---

### TEC-18 · Pruebas de autenticación y RBAC

**Título GitHub:** `TEC-18 · Pruebas de autenticación y RBAC`

Pruebas de autenticación y control de acceso basado en roles (RBAC): pruebas unitarias + integración con cobertura ≥ 95 %.

---

## Milestone 2 · Datos maestros

> HUs relacionadas: **HU4 · HU5 · HU6 · HU7 · HU16 · HU17 · HU18**

---

### TEC-20 · Modelo y CRUD de asignaturas, grupos, docentes y salones

**Título GitHub:** `TEC-20 · Modelo y CRUD de asignaturas, grupos, docentes y salones`

Modelo y CRUD de asignaturas, grupos, docentes, salones, sedes y programas académicos.

---

### TEC-21 · Reglas de negocio de capacidad, tipo espacio y créditos

**Título GitHub:** `TEC-21 · Reglas de negocio de capacidad, tipo espacio y créditos`

Reglas de negocio en `services/`: validación de capacidad de salón, tipo de espacio, créditos e intensidad horaria.

---

### TEC-22 · Endpoints de registro para coordinador

**Título GitHub:** `TEC-22 · Endpoints de registro para coordinador`

Endpoints para registro del coordinador: información básica de asignatura, docente responsable y número de estudiantes.

---

### TEC-23 · Validaciones backend y frontend de datos maestros

**Título GitHub:** `TEC-23 · Validaciones backend y frontend de datos maestros`

Validaciones backend y frontend: duplicados, campos obligatorios y rangos válidos.

---

### TEC-24 · Catálogos parametrizables por tipo

**Título GitHub:** `TEC-24 · Catálogos parametrizables por tipo`

Catálogos parametrizables por tipo: tipo de vinculación docente, tipo de clase y tipo de espacio académico.

---

### TEC-25 · Importación masiva de maestros CSV/Excel con reporte de errores

**Título GitHub:** `TEC-25 · Importación masiva de maestros CSV/Excel con reporte de errores`

Importación masiva de datos maestros desde archivos CSV o Excel, con reporte de errores detallado por fila.

---

### TEC-26 · Pruebas de integridad referencial y reglas de dominio

**Título GitHub:** `TEC-26 · Pruebas de integridad referencial y reglas de dominio`

Pruebas de integridad referencial y reglas de dominio sobre los datos maestros.

---

## Milestone 3 · Programación académica

> HUs relacionadas: **HU8 · HU9 · HU19 · HU20 · HU21 · HU22**

---

### TEC-30 · Modelo de programación académica

**Título GitHub:** `TEC-30 · Modelo de programación académica`

Modelo de programación académica en `models.py`: día, hora inicio/fin, grupo, docente responsable, número de estudiantes y flag de accesibilidad.

---

### TEC-31 · CRUD de programación pre-algoritmo con versionado de borrador

**Título GitHub:** `TEC-31 · CRUD de programación pre-algoritmo con versionado de borrador`

CRUD de programación pre-algoritmo con soporte de edición y versionado de borrador antes de ejecutar el algoritmo.

---

### TEC-32 · Módulo de importación de programación CSV/Excel

**Título GitHub:** `TEC-32 · Módulo de importación de programación CSV/Excel`

Módulo de importación de la programación académica desde archivos CSV o Excel, con mapeo flexible de columnas.

---

### TEC-33 · Motor de validación previa de solapes y capacidad

**Título GitHub:** `TEC-33 · Motor de validación previa de solapes y capacidad`

Motor de validación previa: detección de solapes de docentes/grupos/salones, verificación de capacidad y franjas horarias inválidas.

---

### TEC-34 · Reporte de inconsistencias con severidad y trazabilidad

**Título GitHub:** `TEC-34 · Reporte de inconsistencias con severidad y trazabilidad`

Reporte de inconsistencias con niveles de severidad (error, warning) y trazabilidad por asignatura.

---

### TEC-35 · Soporte de accesibilidad y tipo de espacio especial

**Título GitHub:** `TEC-35 · Soporte de accesibilidad y tipo de espacio especial`

Soporte de requerimientos especiales: flag de accesibilidad/discapacidad y tipo de espacio requerido por asignatura.

---

### TEC-36 · Bloqueo del algoritmo si existen errores críticos

**Título GitHub:** `TEC-36 · Bloqueo del algoritmo si existen errores críticos`

Bloqueo de ejecución del algoritmo si existen errores críticos sin resolver en la validación previa.

---

## Milestone 4 · Generación y gestión de horarios

> HUs relacionadas: **HU10 · HU11 · HU13 · HU15 · HU23**

---

### TEC-40 · Diseñar servicio de asignación independiente

**Título GitHub:** `TEC-40 · Diseñar servicio de asignación independiente`

Diseñar el servicio de asignación como módulo independiente, con entradas y salidas versionadas para facilitar su evolución.

---

### TEC-41 · Implementar algoritmo v1 con restricciones duras y blandas

**Título GitHub:** `TEC-41 · Implementar algoritmo v1 con restricciones duras y blandas`

Implementar el algoritmo genético adaptativo v1 con restricciones duras (sin solapamientos, capacidad mínima) y blandas (agrupación por sede, densidad horaria).

---

### TEC-42 · Endpoint de ejecución asíncrona y estado de procesamiento

**Título GitHub:** `TEC-42 · Endpoint de ejecución asíncrona y estado de procesamiento`

Endpoint de ejecución asíncrona con job queue y endpoint de consulta del estado de procesamiento en tiempo real.

---

### TEC-43 · Persistencia de resultados por corrida

**Título GitHub:** `TEC-43 · Persistencia de resultados por corrida`

Persistencia de resultados por corrida del algoritmo (snapshot de asignaciones) en Supabase PostgreSQL.

---

### TEC-44 · Visualización de horario en plantilla gráfica

**Título GitHub:** `TEC-44 · Visualización de horario en plantilla gráfica`

Visualización del horario generado en plantilla gráfica (grilla semanal) para la vista de administrador y coordinador en React.

---

### TEC-45 · Edición manual post-algoritmo con validación en tiempo real

**Título GitHub:** `TEC-45 · Edición manual post-algoritmo con validación en tiempo real`

Edición manual post-algoritmo con validación en tiempo real de conflictos de asignación.

---

### TEC-46 · Historial de cambios y auditoría con antes/después

**Título GitHub:** `TEC-46 · Historial de cambios y auditoría con antes/después`

Historial de cambios y auditoría: registro de quién hizo el cambio, cuándo, y el estado antes/después de cada modificación.

---

### TEC-47 · Pruebas de performance y consistencia del algoritmo

**Título GitHub:** `TEC-47 · Pruebas de performance y consistencia del algoritmo`

Pruebas de performance y consistencia del algoritmo genético con datasets medianos representativos de la seccional.

---

## Milestone 5 · Publicación y consulta

> HUs relacionadas: **HU12 · HU14 · HU24 · HU25 · HU26 · HU27**

---

### TEC-50 · Flujo de publicación borrador → publicado → archivado

**Título GitHub:** `TEC-50 · Flujo de publicación borrador → publicado → archivado`

Flujo de publicación del horario: borrador → publicado → archivado, gestionado por período académico.

---

### TEC-51 · Exportación a CSV con filtros

**Título GitHub:** `TEC-51 · Exportación a CSV con filtros`

Exportación del horario a CSV con filtros aplicables por programa, semestre, docente y grupo.

---

### TEC-52 · API pública de consulta por rol

**Título GitHub:** `TEC-52 · API pública de consulta por rol`

API pública de consulta del horario diferenciada por rol: docente, estudiante y usuario general.

---

### TEC-53 · Filtros e índices de base de datos para consultas rápidas

**Título GitHub:** `TEC-53 · Filtros e índices de base de datos para consultas rápidas`

Filtros e índices de base de datos en Supabase para garantizar consultas rápidas bajo carga.

---

### TEC-54 · Vista de horario personal y semestral responsive

**Título GitHub:** `TEC-54 · Vista de horario personal y semestral responsive`

Vista de horario personal y semestral en plantilla visual responsive en React, legible desde escritorio y tablet.

---

### TEC-55 · Control de acceso a información publicada y no publicada

**Título GitHub:** `TEC-55 · Control de acceso a información publicada y no publicada`

Control de acceso a información publicada y no publicada según el rol del usuario autenticado.

---

### TEC-56 · Pruebas E2E de consulta, filtros y hardening final

**Título GitHub:** `TEC-56 · Pruebas E2E de consulta, filtros y hardening final`

Pruebas E2E de consulta y filtros + hardening final de seguridad antes de la entrega.

---

## Índice completo de issues técnicas

| ID | Título | Milestone |
|---|---|---|
| TEC-00 | Definir arquitectura base y convenciones | M0 |
| TEC-01 | Configurar entornos dev, staging y prod | M0 |
| TEC-02 | Configurar CI/CD mínimo | M0 |
| TEC-03 | Configurar observabilidad y health checks | M0 |
| TEC-04 | Configurar CORS, seguridad y rate limiting | M0 |
| TEC-05 | Definir versionado de API y documentación OpenAPI | M0 |
| TEC-06 | Seed inicial de catálogos | M0 |
| TEC-10 | Diseñar modelo de datos inicial | M1 |
| TEC-11 | Crear migraciones iniciales y restricciones | M1 |
| TEC-12 | Implementar autenticación JWT con refresh y revocación | M1 |
| TEC-13 | Implementar autorización por rol en backend | M1 |
| TEC-14 | Endpoint login/logout, perfil /me y middleware de seguridad | M1 |
| TEC-15 | CRUD backend de usuarios y roles | M1 |
| TEC-16 | CRUD backend de parámetros generales del sistema | M1 |
| TEC-17 | Pantallas frontend de login y gestión de usuarios | M1 |
| TEC-18 | Pruebas de autenticación y RBAC | M1 |
| TEC-20 | Modelo y CRUD de asignaturas, grupos, docentes y salones | M2 |
| TEC-21 | Reglas de negocio de capacidad, tipo espacio y créditos | M2 |
| TEC-22 | Endpoints de registro para coordinador | M2 |
| TEC-23 | Validaciones backend y frontend de datos maestros | M2 |
| TEC-24 | Catálogos parametrizables por tipo | M2 |
| TEC-25 | Importación masiva de maestros CSV/Excel con reporte de errores | M2 |
| TEC-26 | Pruebas de integridad referencial y reglas de dominio | M2 |
| TEC-30 | Modelo de programación académica | M3 |
| TEC-31 | CRUD de programación pre-algoritmo con versionado de borrador | M3 |
| TEC-32 | Módulo de importación de programación CSV/Excel | M3 |
| TEC-33 | Motor de validación previa de solapes y capacidad | M3 |
| TEC-34 | Reporte de inconsistencias con severidad y trazabilidad | M3 |
| TEC-35 | Soporte de accesibilidad y tipo de espacio especial | M3 |
| TEC-36 | Bloqueo del algoritmo si existen errores críticos | M3 |
| TEC-40 | Diseñar servicio de asignación independiente | M4 |
| TEC-41 | Implementar algoritmo v1 con restricciones duras y blandas | M4 |
| TEC-42 | Endpoint de ejecución asíncrona y estado de procesamiento | M4 |
| TEC-43 | Persistencia de resultados por corrida | M4 |
| TEC-44 | Visualización de horario en plantilla gráfica | M4 |
| TEC-45 | Edición manual post-algoritmo con validación en tiempo real | M4 |
| TEC-46 | Historial de cambios y auditoría con antes/después | M4 |
| TEC-47 | Pruebas de performance y consistencia del algoritmo | M4 |
| TEC-50 | Flujo de publicación borrador → publicado → archivado | M5 |
| TEC-51 | Exportación a CSV con filtros | M5 |
| TEC-52 | API pública de consulta por rol | M5 |
| TEC-53 | Filtros e índices de base de datos para consultas rápidas | M5 |
| TEC-54 | Vista de horario personal y semestral responsive | M5 |
| TEC-55 | Control de acceso a información publicada y no publicada | M5 |
| TEC-56 | Pruebas E2E de consulta, filtros y hardening final | M5 |

---

*RISE S.A.S. · "Donde tu idea se convierte en solución" · Issues Técnicas — Sistema de Asignación de Salones · Universidad del Valle, Seccional Zarzal · 2026*
