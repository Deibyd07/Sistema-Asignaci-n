# 🎯 Documentación del Producto Mínimo Viable (MVP)
**Sistema de Asignación de Salones — Universidad del Valle, Seccional Zarzal**

Este documento recopila de manera exclusiva el alcance, la arquitectura y las Historias de Usuario (HU) requeridas para la construcción del **Mínimo Producto Viable (MVP)** funcional del sistema.

---

## 1. Visión y Propósito del MVP
El MVP es el conjunto mínimo de características que debe estar operativo para que el sistema pueda utilizarse en un escenario real de producción. Su función principal es validar el flujo transversal o de un extremo a otro (**End-to-End**): desde la autenticación al sistema hasta que un administrador ejecuta el algoritmo y un estudiante puede consultar gráficamente la asignación óptima.

---

## 2. Flujo Operativo del MVP

1. **Gestión de Accesos:** Inicio de sesión en el sistema respetando los roles y privilegios (Administrador, Coordinador, y Visor/Usuario).
2. **Configuración Base:** Parametrización inicial por parte de los administradores de los períodos académicos, franjas válidas para clases y tipos de espacio, que funcionarán como el cimiento para todas las reglas.
3. **Registro Maestro de Entidades Básicas:** Alimentación de los catálogos del sistema, empezando por recintos (Salones con su capacidad y disponibilidad en Bolívar/Balsas) y materia prima educacional (Configuración de Asignaturas).
4. **Lógica de Programación por Coordinación:** Los coordinadores vinculan docentes, asignan el cupo (número de estudiantes), e indican explícitamente en qué franjas de fechas deben correr las clases. 
5. **Generación por Algoritmo:** 
   - Se validan las posibles inconsistencias humanas (profesores solapados, falta de cupos, etc). 
   - Se ejecuta externamente el Algoritmo Genético, devolviendo la organización de salones perfecta basada en las restricciones.
6. **Despliegue y Consulta:** El administrador inspecciona visualmente en una grilla y publica oficialmente los horarios para que docentes y estudiantes puedan conectarse y ver la ruta crítica en sus salones de clase.

---

## 3. Resumen y Justificación del Alcance Funcional para el MVP

| ID | Título de la Historia de Usuario | Razón de inclusión en el MVP Funcional |
| :-: | -------------------------------- | -------------------------------------- |
| **HU1** | Iniciar sesión según rol | Sin autenticación y distinción (Admin/Visor) no hay control. |
| **HU3** | Configurar parámetros generales | El algoritmo necesita franjas, tipos de espacio y períodos base. |
| **HU5** | Registrar salones disponibles | Dato crítico y final de salida del sistema; el lugar físico a asignar. |
| **HU7** | Gestionar configuración de asignaturas | Dato crítico académico (créditos y peso ponderado inicial). |
| **HU17**| Registrar docente por asignatura | Restricción clave (un docente no puede estar en dos partes a la vez). |
| **HU18**| Registrar número de estudiantes | Condición para evitar que se asigne salón con capacidad menor al cupo. |
| **HU19**| Definir día y franja horaria | Regla pre-fijada (el algoritmo respeta esta franja para asentar la clase). |
| **HU9** | Validar inconsistencias previo a algoritmo | Detecta corrupción de datos (salva el algoritmo y fallas 500). |
| **HU10**| Ejecutar algoritmo de asignación | **La característica central y resolutiva del proyecto.** |
| **HU11**| Ver horario en plantilla gráfica | Permite la revisión y aprobación formal del cruce logístico. |
| **HU14**| Publicar horarios generados | Determina si el evento está en borrador o listo para el público. |
| **HU24**| Consultar horario por período | Resuelve la necesidad del público de saber sobre su semestre. |
| **HU25**| Ver día, hora, sede y salón | Nivel de detalle mínimo que permite ser aplicable en el mundo real. |

---

## 4. Detalle y Criterios de Aceptación del MVP (Conversación y Confirmación)

### 🔑 Fase Transversal: Acceso y Base
**HU1 · Iniciar sesión según rol**
- **Cómo:** Como administrador/usuario, quiero iniciar sesión con credenciales.
- **Criterios de Aceptación:**
  - Login exitoso redirecciona al panel del rol asignado.
  - Se debe negar la entrada con credenciales incorrectas.
  - Un usuario coordinador no debe poder ver rutas o información privilegiada del administrador.

**HU3 · Configurar parámetros generales**
- **Cómo:** Como administrador, quiero parametrizar períodos y franjas.
- **Criterios de Aceptación:**
  - Debe existir un CRUD de Períodos Académicos.
  - Configuración de franjas horarias y días laborables.
  - Registro de Tipos de Espacio para usarse luego como clasificación.

### 🏫 Fase Maestros: Ingreso de Datos Duros
**HU5 · Registrar salones disponibles**
- **Cómo:** Como administrador, quiero registrar salones con su capacidad y disponibilidad.
- **Criterios de Aceptación:** 
  - Registrar código, nombre, capacidad, tipo y sede del salón.
  - Validación de campos obligatorios y duplicados de código de salón.

**HU7 · Gestionar configuración de asignaturas**
- **Cómo:** Como administrador, quiero administrar lista de asignaturas (código, créditos).
- **Criterios de Aceptación:**
  - Permite crear Asignatura (código, nombre, tipo de clase, etc).
  - Prevenir asignaturas duplicadas.

### 📅 Fase Programación (Coordinadores)
**HU17 · Registrar docente responsable por asignatura**
- **Cómo:** Como coordinador, quiero enlazar un docente a la clase.
- **Criterios de Aceptación:** Se visualiza listado de docentes, se vincula y almacena, debe pasar a la tabla restrictiva del algoritmo.

**HU18 · Registrar número de estudiantes por asignatura**
- **Cómo:** Como coordinador, quiero indicar la cantidad (cupo).
- **Criterios de Aceptación:** Restricción obligatoria de ser número entero mayor a cero, que define la variable de capacidad para filtrar.

**HU19 · Definir día y franja horaria por asignatura**
- **Cómo:** Como coordinador, quiero agendar el día/hora teórica.
- **Criterios de Aceptación:** El coordinador puede elegir dentro de las franjas previamente hechas en HU3 y se debe validar que el cruce de hora fin es mayor a hora inicio.

### ⚙️ Fase Algoritmo y Generación
**HU9 · Validar inconsistencias antes del algoritmo**
- **Cómo:** Como administrador, quiero validar antes de darle ejecución al algoritmo genético pesado.
- **Criterios de Aceptación:** Listado e interrupción del proceso ante docentes cruzados en horas imposibles, franjas fuera de rango, cupos nulos o vacíos técnicos antes del POST a la API.

**HU10 · Ejecutar algoritmo de asignación de salones**
- **Cómo:** Como administrador quiero correr el servicio que hace la magia de cruces logísticos.
- **Criterios de Aceptación:** La aplicación llamará al motor Python informando parámetros si es necesario, captará el resultado óptimo donde Asignatura coincida en Franja contra Salón y se avisará del evento existoso arrojando además si hay fallas de limitación imposibles.

### 📢 Fase Visualización General
**HU11 · Visualizar horario generado en plantilla gráfica**
- **Cómo:** Como administrador quiero ver una grilla matricial.
- **Criterios de Aceptación:** Render general con días en X y horas/franjas en Y, coloreando o ubicando las "cards" en pantalla. Listar sin asignación las sobrantes.

**HU14 · Publicar horarios generados**
- **Cómo:** Como administrador quiero publicar el resultado para los alumnos y docentes.
- **Criterios de Aceptación:** Switch de estado (Borrador -> Publicado) para inhabilitar o habilitar su visibilidad desde los roles planos (estudiantes y profesores). 

**HU24 · Consultar horario por período académico**
- **Cómo:** Como usuario plano (docente o estud) quiero poder ver mis clases.
- **Criterios de Aceptación:** Selección de periodo. Si es publicado se avanza, si no hay aún bloquea y avisa pacíficamente.

**HU25 · Ver día, hora, sede y salón de cada clase**
- **Cómo:** Como usuario de a pie quiero detalles crudos y legibles visualmente.
- **Criterios de Aceptación:** La grilla renderizada final en el cliente expondrá explicitamente Hora Inicio-Fin, Localidad o Sede y el Alfanumérico del Salón en específico para evitar desinformación en los recintos.
