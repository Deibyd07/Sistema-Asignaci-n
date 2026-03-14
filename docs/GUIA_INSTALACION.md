# Guía de Instalación y Ejecución del Proyecto

Sistema de Asignación de Salones

Esta guía explica cómo preparar el entorno de desarrollo y ejecutar el proyecto localmente, desde realizar un **fork del repositorio** hasta **levantar el frontend y backend en tu computador**.

---

## 1. Requisitos del sistema

Antes de comenzar, asegúrate de tener instalados los siguientes programas:

* Git
* Node.js
* Python 3.10 o superior
* npm (se instala con Node)

Puedes verificar que estén instalados ejecutando:

```bash
git --version
node -v
npm -v
python --version
```

---

## 2. Hacer Fork del repositorio

1. Ir al repositorio original del proyecto en GitHub.
2. Hacer clic en el botón **Fork** (arriba a la derecha).
3. GitHub creará una copia del repositorio en tu cuenta.

---

## 3. Clonar el repositorio en tu computador

Abre una terminal y ejecuta:

```bash
git clone https://github.com/TU-USUARIO/Sistema-Asignaci-n.git
```

Luego entra al proyecto:

```bash
cd Sistema-Asignaci-n
```

---

## 4. Estructura del proyecto

El proyecto está dividido en dos partes principales:

```
Sistema-Asignaci-n
│
├── backend   → API desarrollada con Django
├── frontend  → interfaz web desarrollada con Vite
├── docs      → documentación
└── infra     → archivos de infraestructura
```

---

## 5. Configurar el Backend

Entrar a la carpeta backend:

```bash
cd backend
```

---

### 5.1 Instalar dependencias de Python

Ejecutar:

```bash
pip install -r requirements.txt
```

Esto instalará todas las librerías necesarias del backend.

---

### 5.2 Crear archivo de variables de entorno

Copiar el archivo de ejemplo:

```bash
copy .env.example .env
```

Luego editar el archivo `.env` y comentar la línea de base de datos remota para usar SQLite local.

Buscar esta línea:

```
DATABASE_URL=postgresql://postgres:password@db.example.supabase.co:5432/postgres
```

y comentarla así:

```
# DATABASE_URL=postgresql://postgres:password@db.example.supabase.co:5432/postgres
```

Esto permitirá que el proyecto utilice una base de datos local SQLite.

---

### 5.3 Ejecutar migraciones

Desde la carpeta backend ejecutar:

```bash
python manage.py migrate
```

Esto creará las tablas necesarias en la base de datos.

---

### 5.4 Crear usuario administrador

Ejecutar:

```bash
python manage.py createsuperuser
```

Completar los datos solicitados:

```
Username
Email
Password
```

Este usuario servirá para acceder al panel de administración.

---

### 5.5 Ejecutar el servidor backend

Ejecutar:

```bash
python manage.py runserver
```

El servidor iniciará en:

```
http://127.0.0.1:8000
```

Panel de administración:

```
http://127.0.0.1:8000/admin
```

---

## 6. Configurar el Frontend

Abrir otra terminal y entrar al proyecto.

```bash
cd Sistema-Asignaci-n
```

Luego entrar a la carpeta frontend:

```bash
cd frontend
```

---

### 6.1 Instalar dependencias

Ejecutar:

```bash
npm install
```

Esto descargará todas las librerías necesarias del frontend.

---

### 6.2 Ejecutar el frontend

Ejecutar:

```bash
npm run dev
```

El servidor iniciará en:

```
http://localhost:5173
```

---

## 7. Ejecutar el sistema completo

Una vez ejecutados ambos servidores, el sistema funcionará así:

```
Frontend
http://localhost:5173

↓

Backend API
http://127.0.0.1:8000
```

El frontend consumirá la API del backend.

---

## 8. Flujo de trabajo recomendado

Cada vez que vayas a trabajar en el proyecto:

### Backend

```bash
cd backend
python manage.py runserver
```

### Frontend

```bash
cd frontend
npm run dev
```

---

## 9. Notas importantes

* El backend usa **Django**.
* El frontend usa **Vite**.
* La base de datos local usada para desarrollo es **SQLite**.
* En producción el sistema puede conectarse a una base de datos externa.

---

## 10. Problemas comunes

### Error de base de datos Supabase

Si aparece un error relacionado con:

```
db.example.supabase.co
```

significa que el archivo `.env` está intentando conectarse a una base de datos remota.

Solución:

Comentar la línea `DATABASE_URL` en el archivo `.env`.

---

## 11. Autor

Guía creada para el equipo de desarrollo del proyecto **Sistema de Asignación de Salones**.