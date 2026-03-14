# Sistema de asignación de salones

Plataforma para gestionar la asignación de salones, horarios, grupos y recursos académicos, con una interfaz web para operación por roles.

## Contexto del proyecto

Este proyecto nace para resolver el proceso de asignación académica de forma centralizada, trazable y con operación por roles.

El enfoque actual es definir una base técnica sólida mientras se termina de ajustar el detalle funcional final.

## Objetivo del proyecto

Centralizar y optimizar el proceso de asignación académica, permitiendo:

- control de usuarios por rol,
- registro y administración de recursos (grupos, profesores, salones),
- asignación automática y manual,
- detección de conflictos en tiempo real,
- trazabilidad y reportes para toma de decisiones.

## Roles del sistema

- Usuario
- Administrador
- Coordinador

## Alcance funcional inicial

- Autenticación y acceso según rol.
- Gestión de usuarios y parámetros generales del sistema.
- Administración de grupos, profesores, salones y disponibilidades.
- Asignación de salones automática (por reglas) y manual (interfaz visual).
- Detección de conflictos, alertas y sugerencias de ajuste.
- Consulta de horarios por rol y reportes de utilización.
- Historial de cambios para trazabilidad operativa.

## Arquitectura técnica

Se usa **MVT en Django** con frontend desacoplado en React.

En este proyecto, MVT se aplica en modo **API-first**: Django concentra modelos, vistas y lógica de negocio; React renderiza la interfaz principal; y los templates de Django quedan disponibles para usos puntuales (admin, correos o paneles internos).

- `frontend/`: React + Vite (UI y experiencia de usuario).
- `backend/`: Django (API, reglas de negocio y seguridad).
- `infra/supabase/`: integración con Supabase.
- `docs/`: decisiones técnicas y documentación de arquitectura.

Flujo base:

1. React consume la API de Django.
2. Django aplica reglas de negocio y orquesta datos.
3. Supabase provee PostgreSQL administrado (y potencial de auth/storage/realtime).

## Estructura del repositorio

```text
.
|-- backend/
|   |-- apps/
|   |   `-- core/
|   |       |-- migrations/
|   |       |-- services/
|   |       |-- apps.py
|   |       |-- models.py
|   |       |-- urls.py
|   |       `-- views.py
|   |-- config/
|   |-- .env.example
|   |-- manage.py
|   `-- requirements.txt
|-- docs/
|   `-- architecture.md
|-- frontend/
|   |-- public/
|   |-- src/
|   |   |-- App.jsx
|   |   |-- main.jsx
|   |   `-- styles.css
|   |-- .env.example
|   |-- index.html
|   |-- package.json
|   `-- vite.config.js
`-- infra/
    `-- supabase/
        `-- README.md
```

## Puesta en marcha local

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Variables de entorno principales

- `VITE_API_URL`: URL base del backend.
- `DJANGO_SECRET_KEY`: clave de seguridad de Django.
- `DJANGO_DEBUG`: modo de ejecución.
- `DJANGO_ALLOWED_HOSTS`: hosts permitidos por Django.
- `DATABASE_URL`: conexión a PostgreSQL de Supabase.
- `CORS_ALLOWED_ORIGINS`: orígenes permitidos para el frontend.
- `SUPABASE_URL`: URL del proyecto Supabase.
- `SUPABASE_KEY`: clave anon o service role según el caso.

## Documento complementario

Para más detalle técnico de arquitectura revisar: `docs/architecture.md`.
