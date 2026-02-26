# BAKIFLOW - Ecommerce de Ropa Seminueva

**Concepto:** Dale vida a la ropa nuevamente

Plataforma web para comprar y vender ropa seminueva de calidad, dándole una segunda vida a las prendas.

---

## Contenido

- [Descripción](#descripción)
- [Tecnologías](#tecnologías)
- [Funcionalidades](#funcionalidades)
- [Requisitos Previos](#requisitos-previos)
- [Instalación y Configuración](#instalación-y-configuración)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Endpoints del API](#endpoints-del-api)
- [Base de Datos](#base-de-datos)

---

## Descripción

BAKIFLOW es una tienda en línea de ropa seminueva que permite a los usuarios:
- Explorar un catálogo de prendas de segunda mano
- Ver detalles de cada producto
- Agregar productos al carrito de compras
- Gestionar su carrito (agregar, eliminar, vaciar)

---

## Contenido del Proyecto

### Frontend
- **HTML5** - Estructura de las páginas
- **CSS3** - Estilos y diseño responsive
- **JavaScript (Vanilla)** - Lógica del cliente y fetch API

### Backend
- **Python 3.11** - Lenguaje de programación
- **Flask 3.0.0** - Framework web
- **Flask-CORS** - Manejo de peticiones cross-origin
- **psycopg2** - Conector de PostgreSQL

### Base de Datos
- **PostgreSQL 15** - Base de datos relacional
- **Docker** - Containerización
- **pgAdmin** - Interfaz web para administrar la BD

---

## Funcionalidades

### Funcionalidades Principales (2 requeridas)
1. **GET /productos** - Lista todos los productos disponibles
2. **GET /productos/:id** - Obtiene detalle de un producto específico

### Funcionalidades Adicionales (Vista nueva - Carrito)
3. **GET /carrito** - Ver productos en el carrito
4. **POST /carrito** - Agregar producto al carrito
5. **DELETE /carrito/:id** - Eliminar producto del carrito
6. **DELETE /carrito** - Vaciar todo el carrito

---

## Requisitos Previos

Requisitos:

- [x] **Docker Desktop** (para la base de datos)
  
- [x] **Python 3.10+** (recomendado 3.11)
  
- [x] **Conda** (opcional pero recomendado)

### Verificar instalaciones:

```bash
# Verificar Docker
docker --version

# Verificar Python
python --version

# Verificar Conda (si lo usas)
conda --version
```

---

## Instalación y Configuración

### Inicializar la Base de Datos

La base de datos corre en Docker con PostgreSQL y pgAdmin.

```bash
# Desde la carpeta raíz del proyecto
docker-compose up -d
```

**¿Qué hace esto?**
- Descarga las imágenes de PostgreSQL y pgAdmin por primera vez
- Crea y levanta 2 contenedores:
  - `bakiflow_db` - PostgreSQL en puerto 5432
  - `bakiflow_pgadmin` - pgAdmin en puerto 8080
- Ejecuta automáticamente el script `database/init.sql`
- Crea las tablas `productos` y `carrito`
- Inserta 5 productos de ejemplo

**Verificar que funciona:**

```bash
# Ver contenedores corriendo
docker ps

# Deberías ver:
# bakiflow_db       (postgres)
# bakiflow_pgadmin  (pgadmin)

# Ver logs
docker logs bakiflow_db
```

**Acceder a pgAdmin (opcional):**
1. Abre: http://localhost:8080
2. Login:
   - Email: `admin@bakiflow.com`
   - Password: `DinoBakiFlow`
3. Conecta al servidor:
   - Host: `postgres`
   - Port: `5432`
   - User: `bakiflow`
   - Password: `bakiflow123`

---

### Inicializar el Backend

El backend es un servidor Flask que conecta el frontend con la base de datos.

#### Con Conda

```bash
# Crear entorno virtual
conda create -n bakiflow python=3.11

# Activar entorno
conda activate bakiflow

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el backend
python backend.py
```

**Verificar que funciona:**

Debemos ver en la terminal:

```
Iniciando servidor BAKIFLOW...
Servidor corriendo en: http://localhost:3000
Endpoints disponibles:
   - GET    /productos
   - GET    /productos/<id>
   - GET    /carrito
   - POST   /carrito
   - DELETE /carrito/<id>
   - DELETE /carrito
```

**Probar el API:**

Abre en tu navegador: http://localhost:3000/productos

Deberías ver un JSON con los productos.

---

### Inicializar el Frontend

El frontend son páginas HTML estáticas que se sirven con un servidor HTTP simple.

#### Opción A: Con Python (recomendado)

```bash
# Abrir NUEVA TERMINAL (deja el backend corriendo)

# Ir a la carpeta del proyecto
cd bakiflow

# Iniciar servidor HTTP
python -m http.server 8000

# O con Python 3:
python3 -m http.server 8000
```

#### Opción B: Con Node.js (si lo tienes)

```bash
npx http-server -p 8000
```

#### Opción C: Con Live Server (VSCode)

1. Instala la extensión "Live Server"
2. Click derecho en `index.html`
3. "Open with Live Server"

**Verificar que funciona:**

Abre tu navegador en: http://localhost:8000

Deberías ver la tienda BAKIFLOW con los productos.

---

## Resumen de Comandos

Una vez todo configurado, este es el flujo diario:

```bash
# TERMINAL 1: Base de datos
docker-compose up -d

# TERMINAL 2: Backend
conda activate bakiflow  # o: source venv/bin/activate
python backend.py

# TERMINAL 3: Frontend
python -m http.server 8000

# NAVEGADOR:
# http://localhost:8000     → Tu aplicación
# http://localhost:3000     → API (pruebas)
# http://localhost:8080     → pgAdmin (administración BD)
```

---

## 📁 Estructura del Proyecto

```
bakiflow/
│
├── README.md                    # Este archivo
├── docker-compose.yml           # Configuración de Docker
├── requirements.txt             # Dependencias de Python
│
├── backend.py                   # Servidor Flask (Backend)
│
├── index.html                   # Página principal (Vista 1)
├── styles.css                   # Estilos de la página principal
│
├── carrito.html                 # Página del carrito (Vista 2 - NUEVA)
├── styles-carrito.css           # Estilos del carrito
│
└── database/
    └── init.sql                 # Script de inicialización de BD
```

---

## Endpoints del API

### 1. Obtener todos los productos

```http
GET /productos
```

**Respuesta:**
```json
{
  "success": true,
  "count": 5,
  "productos": [
    {
      "id": 1,
      "nombre": "Chamarra de Mezclilla Vintage",
      "precio": 450.00,
      "categoria": "Chamarras",
      "talla": "M",
      "stock": 3,
      ...
    }
  ]
}
```

---

### 2. Obtener producto por ID

```http
GET /productos/:id
```

**Ejemplo:** `GET /productos/1`

**Respuesta:**
```json
{
  "success": true,
  "producto": {
    "id": 1,
    "nombre": "Chamarra de Mezclilla Vintage",
    ...
  }
}
```

---

### 3. Ver carrito

```http
GET /carrito
```

**Respuesta:**
```json
{
  "success": true,
  "items": [
    {
      "carrito_id": 1,
      "producto_id": 1,
      "cantidad": 2,
      "nombre": "Chamarra...",
      "precio": 450.00,
      "subtotal": 900.00
    }
  ],
  "total": 900.00,
  "cantidad_items": 1
}
```

---

### 4. Agregar al carrito

```http
POST /carrito
Content-Type: application/json

{
  "producto_id": 1,
  "cantidad": 2
}
```

**Respuesta:**
```json
{
  "success": true,
  "message": "Producto agregado al carrito"
}
```

---

### 5. Eliminar del carrito

```http
DELETE /carrito/:id
```

**Ejemplo:** `DELETE /carrito/1`

---

### 6. Vaciar carrito

```http
DELETE /carrito
```

---

## Base de Datos

### Tabla: productos

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL | ID único (autoincremental) |
| nombre | VARCHAR(200) | Nombre de la prenda |
| descripcion | TEXT | Descripción detallada |
| categoria | VARCHAR(100) | Chamarras, Playeras, etc. |
| talla | VARCHAR(20) | S, M, L, 32, etc. |
| precio | DECIMAL(10,2) | Precio en MXN |
| condicion | VARCHAR(50) | Excelente, Muy Buena, Buena |
| imagen_url | VARCHAR(500) | URL de la imagen |
| disponible | BOOLEAN | Si está disponible para venta |
| stock | INTEGER | Cantidad disponible |
| creado_en | TIMESTAMP | Fecha de creación |

---

### Tabla: carrito

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL | ID único del item en carrito |
| producto_id | INTEGER | FK a productos(id) |
| cantidad | INTEGER | Cantidad de ese producto |
| agregado_en | TIMESTAMP | Cuándo se agregó |

**Relación:** carrito.producto_id → productos.id (FOREIGN KEY)

---

## Posibles complicaciones que se llegaron a tener

### Error: "No se pudo conectar a la base de datos"

**Causa:** Docker no está corriendo o el contenedor no inició.

**Solución:**
```bash
docker ps  # Ver si bakiflow_db está corriendo
docker logs bakiflow_db  # Ver errores
docker-compose restart  # Reiniciar contenedores
```

---

### Error: "Port 5432 is already in use"

**Causa:** Ya tienes PostgreSQL corriendo localmente.

**Solución:**
- Detén PostgreSQL local, o
- Cambia el puerto en `docker-compose.yml` y `backend.py`

---

### Error: "CORS policy blocked"

**Causa:** CORS no está habilitado en Flask.

**Solución:** Ya está incluido en `backend.py`:
```python
from flask_cors import CORS
CORS(app)
```

---

### Error: "Module 'flask' not found"

**Causa:** No instalaste las dependencias.

**Solución:**
```bash
conda activate bakiflow
pip install -r requirements.txt
```

---

## Autor

- **María Fernanda Maldonado Melendez** - Universidad Panamericana

---



**BAKIFLOW** - Segunda vida para tu estilo
