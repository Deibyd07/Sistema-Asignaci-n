# Arquitectura propuesta

## Patrón elegido

Para este stack, la mejor decisión es **MVT en Django**, no MVC clásico.

### Por qué

- Django implementa MVT de forma nativa.
- Intentar forzarlo a MVC suele terminar en nombres artificiales y más fricción.
- Como la interfaz principal será React, el backend de Django debe centrarse en API, seguridad, reglas de negocio e integración con datos.

## Cómo se traduce en este proyecto

### Frontend

- React maneja la experiencia de usuario.
- Se organiza por componentes y, cuando el proyecto crezca, por features.
- Consume endpoints HTTP del backend.

### Backend

- `models.py`: entidades y persistencia.
- `views.py`: endpoints o vistas API del dominio.
- `services/`: reglas de negocio reutilizables para no recargar las vistas.
- `urls.py`: mapeo de rutas del dominio.
- `config/`: settings globales, URLs raíz y arranque del proyecto.

## Rol de Supabase

En este proyecto, Supabase se usa primero como **PostgreSQL administrado**.

También se deja preparado para poder sumar después:

- autenticación,
- storage,
- realtime.

## Estructura por capas

```text
React UI
   |
HTTP / JSON
   |
Django URLs -> Views -> Services -> Models -> Supabase PostgreSQL
```

## Convenciones recomendadas

- Crear apps Django por dominio, no por tipo técnico.
- Mantener la lógica de negocio en `services/`.
- Dejar `views.py` delgado: validación de entrada, llamada a servicio y respuesta.
- Usar Supabase como infraestructura de datos, no como lugar para duplicar reglas que ya viven en Django.
- Reservar Templates de Django para casos puntuales como admin, emails o paneles internos.

## Cuando crezca el proyecto

Puedes extender la misma base con:

- `apps/reservas/`
- `apps/salones/`
- `apps/horarios/`
- `apps/usuarios/`

Y en frontend:

- `src/features/reservas/`
- `src/features/salones/`
- `src/features/horarios/`
