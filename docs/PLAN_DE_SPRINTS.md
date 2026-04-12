# 🏃‍♂️ Plan de Sprints: MVP - Sistema de Asignación de Salones

De acuerdo a las características y requerimientos establecidos para el Producto Mínimo Viable (MVP), se ha estructurado el desarrollo continuo en **5 Sprints**. 
Para optimizar el esfuerzo de un **equipo de 4 desarrolladores**, cada Sprint cuenta con una división de **Sub-tareas** enfocadas en Frontend, Backend, Lógica y QA/Infraestructura, asegurando una carga equitativa en cada etapa de la iteración.

---

## 🛠️ Sprint 1: Cimientos, Base de Datos y Control de Acceso
**Objetivo:** Establecer la infraestructura inicial del aplicativo, gestionar la autenticación y controlar los accesos basada en roles (administrador, coordinador y usuario visualizador).
**Historias Mapeadas:** HU1.

### 📋 Sub-tareas (Distribución recomendada para 4 personas)
*   **Dev 1 (Infra / DB):** Diseño del modelo Entidad-Relación Inicial, configuración del motor de la Base de Datos, variables de entorno y creación de la tabla de Roles y Usuarios.
*   **Dev 2 (Backend Auth):** Inicialización del servidor backend. Programación de los Endpoints de Login (Autenticación), manejo de seguridad (ej. contraseñas encriptadas) y generación de Tokens (JWT u otro) para las sesiones.
*   **Dev 3 (Frontend Base UI):** Inicialización del repositorio y framework Frontend. Configuración del sistema de diseño (CSS/Librerías). Maquetación de la pantalla de "Login" e interfaces base.
*   **Dev 4 (Frontend Integration & QA):** Configuración de rutas estáticas en Frontend y "Rutas Protegidas" dependientes del rol. Conexión del Login (Frontend) con la API (Backend), manejo de estados de error, y configuración inicial del flujo de control de versiones Git (CI/CD si aplica).

---

## 🏫 Sprint 2: Parametrización y Registros Maestros
**Objetivo:** Construir los catálogos y parámetros del sistema imperativos, sobre los cuales se fundamentan las reglas del entorno educativo y logístico.
**Historias Mapeadas:** HU3, HU5, HU7.

### 📋 Sub-tareas
*   **Dev 1 (Backend CRUDs Base):** Desarrollo de Endpoints y Querys a base de datos para HU3 (Períodos, franjas, días hábiles) y HU7 (CRUD de Asignaturas con configuración de créditos).
*   **Dev 2 (Frontend CRUDs Base):** Construcción de los paneles y formularios en Frontend para que el Admin consuma y llene los datos de HU3 y HU7.
*   **Dev 3 (Backend Lógica de Recintos):** Desarrollo de la lógica y modelo relacional en BD para HU5 (Salones, aforos, disponibilidad). Inclusión de validaciones lógicas (evitar códigos de salón repetidos, aforos negativos, etc).
*   **Dev 4 (Frontend Recintos):** Creación de las vistas e integración de la API para registrar, editar y listar los salones (HU5). Control de UI y feedback visual de éxito/error al usuario administrador, y pruebas de testeo en esta fase.

---

## 📅 Sprint 3: Programación Académica y Restricciones
**Objetivo:** Habilitar a los coordinadores para que establezcan las reglas y requisitos para los cruces de asignación; inyectar la carga transaccional que nutrirá al algoritmo.
**Historias Mapeadas:** HU17, HU18, HU19.

### 📋 Sub-tareas
*   **Dev 1 (Backend Asociaciones):** Desarrollo de Endpoints para HU17 (listar docentes, vincular ID Docente con ID Asignatura) actualizando las tablas restrictivas del sistema.
*   **Dev 2 (Backend Restricciones):** Desarrollo de API y validaciones para la inyección de restricciones físicas y lógicas espaciales requeridas por el coordinador: HU18 (Capacidad puntual de alumnos para la materia) y HU19 (Vincular la franja y día deseado a la asignatura).
*   **Dev 3 (Frontend Interfaz Coordinador):** Diseño y desarrollo UI exclusivo que será visto por el rol "Coordinador" para el mapeo interactivo de materias ofertadas por el departamento vs catálogo general y visualización de recursos (docentes disponibles).
*   **Dev 4 (Frontend Agendamiento Manual):** Integración de formularios avanzados y listados desplegables que reúnan el consumo general (vincular en pantalla el profesor, escribir cantidad de cupos, y seleccionar el selector de franja requerida). Captura de errores al guardar restricciones cruzadas. 

---

## 🧠 Sprint 4: Inteligencia y Lógica Core (Algoritmo Genético)
**Objetivo:** Construir e integrar el "cerebro" del sistema, que consolidará los datos para proveer una solución espacial factible a los requerimientos preestablecidos.
**Historias Mapeadas:** HU9, HU10.

### 📋 Sub-tareas
*   **Dev 1 (Lógica Algoritmo A):** Programación y adaptación del Core del Algoritmo Genético (Python Script u otro lenguaje), configuración de Generaciones, Población, Mutaciones y la Función Objetivo (Aptitud/Fitness). 
*   **Dev 2 (Lógica Algoritmo B):** En la programación del Algoritmo, manejar el cumplimiento e inyección de los filtros estrictos y restricciones rígidas (capacidad de salón vs cupos solicitados, evitar choque del mismo profesor, restricciones de disponibilidad de salones de HU18 y HU19). 
*   **Dev 3 (Integrador Backend):** Creación del código (HU10) que interactúe entre el Backend genérico Node/PHP/Java y el entorno del algoritmo. Recibir el "Json" óptimo (matriz de asignación resuelta) y guardar finalmente estos cronogramas aprobados en la base de datos principal.
*   **Dev 4 (Validador de Datos - Backend / Front):** (HU9) Desarrollo completo de una sub-rutina de validación "Pre-Ejecución Algoritmo". Antes de gatillar ese script pesado, el código revisa inconsistencias lógicas en la base de datos. En el frontend, mostrar un modal bloqueante que enumere errores y bloquee la ejecución manual si encuentra fallas de integridad en los cupos.

---

## 📢 Sprint 5: Visualización, Publicación y Despliegue
**Objetivo:** Entregar la interfaz mediante la cual los roles correspondientes podrán interactuar con el resultado del algoritmo y consumir la información del sistema.
**Historias Mapeadas:** HU11, HU14, HU24, HU25.

### 📋 Sub-tareas
*   **Dev 1 (Backend de Lectura):** Construcción optimizada de Endpoints para la obtención y filtrado matriz final. Endpoint de publicación o cambio de la bandera booleana (estado de borrador a completado -> HU14).
*   **Dev 2 (Frontend Grilla Administrador):** (HU11) Maquetación y programación compleja visual para el usuario administrador: Interpretar el resultado JSON del algoritmo y renderizarlo en pantalla como si fuera un calendario tipo cronograma con bloques que avisan qué evento queda por asignar.
*   **Dev 3 (Frontend Grilla Público):** (HU24/HU25) Maquetación simple, mobile-friendly y accesible para usuarios básicos (profes / alumnos) donde se listen solo sus materias asignadas con el nombre de bloque, sede, salón, franja de hora y días concretos del semestre.
*   **Dev 4 (UI/UX - QA - Despliegue):** Refinamiento final y Responsive Design a nivel general de los módulos para que no se caigan en pantallas distintas. Control de calidad (test de pase). Despliegue en el entorno de producción (Hosting / VPS). Manejo del entregable con la doc oficial final y links públicos en el README.

---

> [!IMPORTANTE]
> Cada Sprint deberá contar con reuniones Daily o un seguimiento continuo y las historias deben probarse de inicio a fin para ser contadas como completadas a nivel de funcionalidad (**End-to-End**) según indique la **DOCUMENTACION_MVP.md**.
