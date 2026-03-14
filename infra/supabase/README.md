# Supabase

Uso previsto en esta arquitectura:

- Base de datos PostgreSQL administrada.
- Posible uso futuro de autenticacion, storage y realtime.

## Integracion recomendada

### Opcion base

- Django se conecta a Supabase usando `DATABASE_URL`.
- React habla solo con Django.

Esta opcion deja un punto unico para permisos, validaciones y reglas de negocio.

### Opcion hibrida

- React puede usar Supabase directamente para auth o storage.
- Django sigue controlando la logica de negocio central.

Solo conviene cuando esa separacion este bien definida.

## Variables necesarias

- `DATABASE_URL`
- `SUPABASE_URL`
- `SUPABASE_KEY`
