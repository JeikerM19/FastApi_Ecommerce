<p align="center">
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI Logo" width="320"/>
</p>

<h1 align="center">🛍️ FastAPI E-Commerce API</h1>

<p align="center">
  API RESTful completa para la gestión de un e-commerce, construida con <strong>FastAPI</strong>, <strong>JWT</strong>, <strong>SQLAlchemy</strong> y <strong>MySQL</strong>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/JWT-Auth-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white" alt="JWT"/>
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy"/>
  <img src="https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL"/>
  <img src="https://img.shields.io/badge/Pydantic-V2-E92063?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic"/>
  <img src="https://img.shields.io/badge/Alembic-Migrations-6BA81E?style=for-the-badge" alt="Alembic"/>
</p>

---

## ✨ Características Principales

| Característica | Descripción |
|---|---|
| 🔐 **Autenticación JWT** | Registro, login con OAuth2, tokens con expiración configurable y roles (usuario/admin) |
| 🛒 **Carrito de compras** | Agregar, eliminar productos y acumulación automática de cantidades |
| 📦 **Sistema de pedidos** | Confirmación de compra con descuento automático de stock y registro histórico |
| 📂 **Gestión de productos** | CRUD completo con control de stock e inventario (solo admins) |
| 🏷️ **Categorías** | Organización de productos por categorías con relaciones ORM |
| 🗃️ **Migraciones** | Evolución segura del esquema de BD con Alembic |
| 📖 **Docs interactivos** | Swagger UI auto-generado en `/docs` gracias a FastAPI + Pydantic |
| 🧪 **Tests** | Tests automatizados con `pytest` para autenticación y productos |

---

## 🏗️ Tech Stack

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENTE (Frontend)                       │
│              Swagger UI  ·  Postman  ·  cualquier app           │
└────────────────────────────────┬────────────────────────────────┘
                                 │ HTTP + JSON
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                     FastAPI  (Framework)                         │
│  ┌──────────┐  ┌───────────┐  ┌──────────┐  ┌───────────────┐  │
│  │ Uvicorn  │  │  Pydantic │  │  OAuth2  │  │   APIRouter   │  │
│  │ (ASGI)   │  │  (Valid.) │  │  (Auth)  │  │  (Routing)    │  │
│  └──────────┘  └───────────┘  └──────────┘  └───────────────┘  │
├─────────────────────────────────────────────────────────────────┤
│                     Capa de Seguridad                            │
│  ┌──────────────────────┐  ┌────────────────────────────────┐   │
│  │  python-jose (JWT)   │  │  passlib + bcrypt (Hashing)    │   │
│  └──────────────────────┘  └────────────────────────────────┘   │
├─────────────────────────────────────────────────────────────────┤
│                     Capa de Datos                                │
│  ┌──────────────────────┐  ┌────────────────────────────────┐   │
│  │  SQLAlchemy (ORM)    │  │  Alembic (Migraciones)         │   │
│  └──────────┬───────────┘  └────────────────────────────────┘   │
│             │ PyMySQL                                            │
│             ▼                                                    │
│  ┌──────────────────────┐                                       │
│  │   MySQL Database     │                                       │
│  └──────────────────────┘                                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### Prerrequisitos

- **Python 3.10+**
- **MySQL** (servidor corriendo)
- **Git**

### 1. Clonar el repositorio

```bash
git clone https://github.com/JeikerM19/FastApi_Ecommerce.git
cd FastApi_Ecommerce
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv venv
```

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

> 💡 Sabrás que el entorno está activo cuando veas `(venv)` al inicio de tu terminal.

### 3. Instalar dependencias

```bash
pip install fastapi uvicorn sqlalchemy pymysql passlib[bcrypt] python-jose[cryptography] python-multipart email-validator python-dotenv alembic pydantic-settings
```

### 4. Configurar variables de entorno

Crea un archivo **`.env`** en la **raíz del proyecto** con las siguientes variables:

```env
# Base de Datos
DATABASE_URL=mysql+pymysql://usuario:contraseña@localhost:3306/nombre_bd

# JWT
SECRET_KEY=tu_clave_secreta_super_segura_aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> ⚠️ **Nunca subas el archivo `.env` al repositorio.** Ya está incluido en `.gitignore`.

### 5. Aplicar migraciones

```bash
cd app
alembic upgrade head
```

### 6. Ejecutar el servidor

```bash
uvicorn main:app --reload
```

| Recurso | URL |
|---|---|
| 🌐 **API** | http://127.0.0.1:8000 |
| 📖 **Swagger UI** | http://127.0.0.1:8000/docs |
| 📋 **ReDoc** | http://127.0.0.1:8000/redoc |

---

## 📁 Estructura del Proyecto

```
FASTAPI/
├── .env                           # Variables de entorno (excluido de git)
├── .gitignore
├── Readme.md
└── app/
    ├── main.py                    # Punto de entrada — FastAPI app + router /api/v1
    │
    ├── api/                       # 🌐 Endpoints (rutas HTTP)
    │   └── api_v1/
    │       ├── api.py             # Router principal — agrupa sub-routers
    │       ├── auth.py            # POST /registro, /login, GET /me, /admin/ping
    │       ├── productos.py       # CRUD de productos (admin)
    │       ├── categorias.py      # CRUD de categorías
    │       ├── carrito.py         # Carrito de compras del usuario
    │       └── pedido.py          # Confirmación de pedido
    │
    ├── core/                      # 🔐 Seguridad
    │   ├── config.py              # Carga de .env con pydantic-settings
    │   └── security.py            # bcrypt hashing + JWT encode/decode
    │
    ├── crud/                      # 🔧 Operaciones de base de datos
    │   ├── __init__.py            # Re-exporta todas las funciones CRUD
    │   ├── producto.py
    │   ├── categoria.py
    │   ├── usuario.py
    │   ├── carrito.py
    │   └── pedido.py
    │
    ├── db/                        # 🗄️ Conexión a la BD
    │   └── database.py            # Engine, SessionLocal, Base
    │
    ├── deps/                      # 🔗 Dependencias inyectables
    │   └── deps.py                # get_db, get_current_user, requiere_admin
    │
    ├── models/                    # 📊 Modelos ORM (tablas)
    │   ├── __init__.py
    │   ├── producto.py            # Producto
    │   ├── categoria.py           # Categoria
    │   ├── usuario.py             # Usuario
    │   └── pedidos.py             # Carrito, ItemCarrito, Pedido, DetallePedido
    │
    ├── schemas/                   # 📝 Schemas Pydantic (validación)
    │   ├── __init__.py
    │   ├── producto.py
    │   ├── categoria.py
    │   ├── usuario.py
    │   └── token.py
    │
    ├── tests/                     # 🧪 Tests automatizados
    │   ├── test_auth.py
    │   └── test_producto.py
    │
    └── alembic/                   # 🗃️ Migraciones de BD
        ├── env.py
        └── versions/
```

### Separación de responsabilidades

| Capa | Carpeta | Responsabilidad |
|---|---|---|
| **Presentación** | `api/` | Endpoints HTTP, validación de entrada/salida |
| **Seguridad** | `core/` | Hashing de contraseñas, gestión de tokens JWT |
| **Negocio** | `crud/` | Lógica de negocio y operaciones en la BD |
| **Infraestructura** | `db/` | Motor de conexión y sesiones SQLAlchemy |
| **Inyección** | `deps/` | Dependencias reutilizables (`Depends()`) |
| **Dominio** | `models/` | Modelos ORM — representan las tablas MySQL |
| **Contratos** | `schemas/` | Schemas Pydantic — validación y serialización |

---

## 🔐 Autenticación y Seguridad

### Flujo de autenticación JWT

```
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│   1. REGISTRO                                                        │
│   POST /api/v1/auth/usuarios                                         │
│   { "nombre", "email", "password" }                                  │
│           │                                                          │
│           ▼                                                          │
│   bcrypt.hash(password) ──► Se guarda hash en BD                     │
│   (nunca el texto plano)                                             │
│                                                                      │
│   2. LOGIN                                                           │
│   POST /api/v1/auth/login                                            │
│   { "username" (email), "password" }                                 │
│           │                                                          │
│           ▼                                                          │
│   bcrypt.verify(password, hash) ──► ¿Coincide?                       │
│           │                            │                             │
│          NO ── 401 Unauthorized       SÍ                             │
│                                        │                             │
│                                        ▼                             │
│                          jwt.encode({ sub: email,                    │
│                                       es_admin: bool,                │
│                                       exp: datetime })               │
│                                        │                             │
│                                        ▼                             │
│                          { "access_token": "eyJ...",                 │
│                            "token_type": "bearer" }                  │
│                                                                      │
│   3. PETICIONES PROTEGIDAS                                           │
│   Header: Authorization: Bearer <token>                              │
│           │                                                          │
│           ▼                                                          │
│   get_current_user() ──► jwt.decode(token)                           │
│           │                  │                                       │
│       Inválido ── 401    Válido ── devuelve usuario                  │
│                                                                      │
│   4. RUTAS DE ADMIN                                                  │
│   requiere_admin() ──► ¿es_admin == True?                            │
│           │                  │                                       │
│          NO ── 403       SÍ ── acceso concedido                      │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

### Tecnologías de seguridad utilizadas

| Componente | Librería | Función |
|---|---|---|
| **Hashing** | `passlib` + `bcrypt` | Hash irreversible de contraseñas — nunca se guarda texto plano |
| **Tokens** | `python-jose` | Creación y verificación de tokens JWT con algoritmo HS256 |
| **OAuth2** | `fastapi.security` | Esquema `OAuth2PasswordBearer` para extraer tokens del header |
| **Config** | `pydantic-settings` | Carga segura de `SECRET_KEY`, `ALGORITHM` y `ACCESS_TOKEN_EXPIRE_MINUTES` desde `.env` |

### Estructura de un token JWT

```
 Header              Payload                          Signature
┌─────────┐   ┌────────────────────────┐   ┌──────────────────────┐
│ alg:HS256│   │ sub: "user@email.com"  │   │ HMACSHA256(          │
│ typ:JWT  │ . │ es_admin: false        │ . │   header + payload,  │
│          │   │ exp: 1714567890        │   │   SECRET_KEY         │
└─────────┘   └────────────────────────┘   │ )                    │
                                            └──────────────────────┘

eyJhbGciOi...  .  eyJzdWIiOi...  .  SflKxwRJSMeKKF2QT4fw...
```

---

## 🗄️ Base de Datos y Modelos

### Diagrama del esquema relacional

```
┌──────────────┐       ┌──────────────┐       ┌─────────────────┐
│  categorias  │       │  productos   │       │  items_carrito  │
├──────────────┤       ├──────────────┤       ├─────────────────┤
│ id       PK  │◄──┐   │ id       PK  │◄──────┤ id          PK  │
│ nombre       │   └───┤ nombre       │       │ carrito_id  FK  │──┐
└──────────────┘       │ precio       │       │ producto_id FK  │  │
                       │ en_stock     │       │ cantidad        │  │
                       │ stock        │       └─────────────────┘  │
                       │ categoria_id │FK                          │
                       └──────┬───────┘                            │
                              │                                    │
                              │                     ┌──────────────┤
┌──────────────┐              │    ┌────────────┐   │              │
│  usuarios    │              │    │  carritos   │◄──┘              │
├──────────────┤              │    ├────────────┤                   │
│ id       PK  │◄─────────┐  │    │ id      PK │                   │
│ nombre       │          │  │    │ usuario_id │FK                 │
│ email        │          │  │    └────────────┘                   │
│ hashed_pass  │          │  │                                     │
│ es_admin     │          │  │    ┌─────────────────┐              │
└──────┬───────┘          │  └────┤detalles_pedidos │              │
       │                  │       ├─────────────────┤              │
       │                  │       │ id          PK  │              │
       │    ┌──────────┐  │       │ pedido_id   FK  │──┐           │
       └────┤ pedidos  │  │       │ producto_id FK  │  │           │
            ├──────────┤  │       │ cantidad        │  │           │
            │ id    PK │◄─┼───────┤ subtotal        │  │           │
            │ usuario_id│FK│       └─────────────────┘  │           │
            │ fecha    │  │                             │           │
            │ total    │  │                             │           │
            └──────────┘  └─────────────────────────────┘           │
```

### Modelos ORM principales

<details>
<summary><strong>📦 Producto</strong></summary>

```python
class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True)
    precio = Column(Float)
    en_stock = Column(Boolean, default=True)    # ¿Disponible para venta?
    stock = Column(Integer, default=0)          # Unidades en inventario
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    categorias = relationship("Categoria", back_populates="productos")
```

> 📝 `en_stock` (Boolean) ≠ `stock` (Integer). `en_stock` permite desactivar manualmente un producto; `stock` se descuenta automáticamente al confirmar un pedido.

</details>

<details>
<summary><strong>👤 Usuario</strong></summary>

```python
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100))
    es_admin = Column(Boolean, default=False)
    carrito = relationship("Carrito", back_populates="usuario",
                           uselist=False, cascade="all, delete-orphan")
    pedidos = relationship("Pedido", back_populates="usuario",
                           cascade="all, delete-orphan")
```

> 📝 `uselist=False` en `carrito` → un usuario tiene **un solo** carrito activo.

</details>

<details>
<summary><strong>🛒 Carrito, ItemCarrito, Pedido, DetallePedido</strong></summary>

```python
class Carrito(Base):
    __tablename__ = "carritos"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    items = relationship("ItemCarrito", back_populates="carrito",
                         cascade="all, delete-orphan")

class ItemCarrito(Base):
    __tablename__ = "items_carrito"
    id = Column(Integer, primary_key=True, index=True)
    carrito_id = Column(Integer, ForeignKey("carritos.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer, default=1)

class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    fecha = Column(DateTime, default=datetime.now)
    total = Column(Float)
    detalles = relationship("DetallePedido", back_populates="pedido")

class DetallePedido(Base):
    __tablename__ = "detalles_pedidos"
    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer)
    subtotal = Column(Float)
```

</details>

---

## 🌐 Endpoints de la API

> Todas las rutas llevan el prefijo **`/api/v1/`** definido en `main.py`.

### 🔑 Auth — `/api/v1/auth`

| Método | Ruta | Descripción | Acceso |
|---|---|---|---|
| `POST` | `/auth/usuarios` | Registrar un nuevo usuario | 🌍 Público |
| `POST` | `/auth/login` | Login — devuelve JWT | 🌍 Público |
| `GET` | `/auth/usuarios/me` | Ver perfil del usuario actual | 🔒 Token |
| `GET` | `/auth/admin/ping` | Verificar permisos de admin | 🛡️ Admin |

### 📦 Productos — `/api/v1/productos`

| Método | Ruta | Descripción | Acceso |
|---|---|---|---|
| `GET` | `/productos/` | Listar todos los productos | 🌍 Público |
| `POST` | `/productos/` | Crear un producto | 🛡️ Admin |
| `PUT` | `/productos/{id}` | Actualizar un producto | 🛡️ Admin |
| `DELETE` | `/productos/{id}` | Eliminar un producto | 🛡️ Admin |

### 🏷️ Categorías — `/api/v1/categorias`

| Método | Ruta | Descripción | Acceso |
|---|---|---|---|
| `POST` | `/categorias/` | Crear una categoría | 🌍 Público |
| `GET` | `/categorias/` | Listar todas las categorías | 🌍 Público |

### 🛒 Carrito — `/api/v1/carrito`

| Método | Ruta | Descripción | Acceso |
|---|---|---|---|
| `GET` | `/carrito/` | Ver carrito del usuario | 🔒 Token |
| `POST` | `/carrito/agregar/{id}` | Agregar producto al carrito | 🔒 Token |
| `DELETE` | `/carrito/eliminar/{id}` | Eliminar item del carrito | 🔒 Token |

### 📦 Pedidos — `/api/v1/pedido`

| Método | Ruta | Descripción | Acceso |
|---|---|---|---|
| `POST` | `/pedido/confirmar` | Confirmar compra (carrito → pedido) | 🔒 Token |

---

## 🛒 Flujo de Compra E-Commerce

```
  ┌─────────────────────────────────────────────────────────────────┐
  │                    FLUJO COMPLETO DE COMPRA                     │
  └─────────────────────────────────────────────────────────────────┘

  1️⃣  POST /auth/usuarios          → Crear cuenta
  2️⃣  POST /auth/login             → Obtener token JWT
  3️⃣  POST /carrito/agregar/{id}    → Agregar productos (con token)
      ↳ Si el producto ya está en el carrito → acumula cantidad
      ↳ Si es nuevo → crea un ItemCarrito
  4️⃣  GET  /carrito/               → Revisar carrito
  5️⃣  POST /pedido/confirmar       → Confirmar compra
      ↳ Valida stock disponible
      ↳ Descuenta stock del inventario
      ↳ Crea Pedido + DetallePedido (registro permanente)
      ↳ Elimina el carrito (temporal)
      ↳ Devuelve el pedido con total calculado
```

---

## 🗃️ Migraciones con Alembic

Alembic gestiona la evolución del esquema de BD de forma segura, sin perder datos.

### Comandos principales

```bash
# Desde la carpeta app/

# Generar migración automática a partir de cambios en los modelos
alembic revision --autogenerate -m "descripcion del cambio"

# Aplicar todas las migraciones pendientes
alembic upgrade head

# Ver estado actual
alembic current

# Ver historial completo
alembic history
```

### ¿Cuándo se necesita una migración?

| Cambio | ¿Requiere migración? |
|---|---|
| Agregar una columna nueva | ✅ Sí |
| Cambiar el tipo de una columna | ✅ Sí |
| Agregar una nueva tabla | ✅ Sí |
| Agregar/modificar un `relationship` | ❌ No (es solo ORM) |

---

## 🧪 Tests

El proyecto incluye tests automatizados con `pytest`:

```bash
cd app
pytest tests/ -v
```

| Archivo | Cobertura |
|---|---|
| `test_auth.py` | Registro, login, credenciales inválidas |
| `test_producto.py` | CRUD de productos, permisos de admin |

---

## 📦 Dependencias

| Paquete | Versión | Propósito |
|---|---|---|
| **fastapi** | 0.100+ | Framework web async de alto rendimiento con type hints |
| **uvicorn** | — | Servidor ASGI ultrarrápido |
| **sqlalchemy** | — | ORM para interactuar con MySQL usando objetos Python |
| **pymysql** | — | Driver de conexión Python ↔ MySQL |
| **passlib[bcrypt]** | — | Hashing seguro e irreversible de contraseñas |
| **python-jose[cryptography]** | — | Creación y verificación de tokens JWT (HS256) |
| **python-multipart** | — | Soporte para `OAuth2PasswordRequestForm` |
| **email-validator** | — | Validación de emails con `EmailStr` de Pydantic |
| **python-dotenv** | — | Carga de variables desde `.env` |
| **alembic** | — | Migraciones versionadas del esquema de BD |
| **pydantic-settings** | — | Configuración centralizada con validación de tipos |
| **pytest** | — | Framework de testing |

---

## 📖 Apuntes y Conceptos del Curso

<details>
<summary><strong>🌍 Fundamentos: API, REST, HTTP y JSON</strong></summary>

### ¿Qué es una API?

Una **API** (Application Programming Interface) es un conjunto de reglas que permite que dos programas se comuniquen entre sí.

```
┌──────────┐         ┌──────────┐         ┌──────────────┐
│ Cliente  │  ────►  │   API    │  ────►  │  Servidor /  │
│ (App,    │  ◄────  │ (mesero) │  ◄────  │  Base de     │
│ Browser) │         │          │         │  Datos       │
└──────────┘         └──────────┘         └──────────────┘
```

### ¿Qué es REST?

**REST** (Representational State Transfer) es un estilo de arquitectura para diseñar APIs:

| Principio | Significado |
|---|---|
| **Cliente-Servidor** | Independientes, evolucionan por separado |
| **Sin estado (Stateless)** | Cada petición contiene toda la info necesaria |
| **Recursos con URL** | Cada recurso tiene una URL única |
| **Métodos HTTP estándar** | GET, POST, PUT, DELETE |
| **JSON** | Formato estándar de intercambio |

### Métodos HTTP (CRUD)

| Método | Operación | ¿Lleva Body? |
|---|---|---|
| **GET** | Read | No |
| **POST** | Create | Sí |
| **PUT** | Update | Sí |
| **DELETE** | Delete | No |

### Códigos de estado HTTP

| Código | Significado | Cuándo aparece |
|---|---|---|
| **200** | OK | Petición exitosa |
| **201** | Created | Recurso creado |
| **400** | Bad Request | Datos incorrectos |
| **401** | Unauthorized | Token faltante o inválido |
| **403** | Forbidden | Sin permisos suficientes |
| **404** | Not Found | Recurso no existe |
| **422** | Unprocessable Entity | Validación fallida |
| **500** | Internal Server Error | Error del servidor |

</details>

<details>
<summary><strong>⚡ Conceptos de FastAPI</strong></summary>

### Instancia y endpoints

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido a mi API"}
```

- `FastAPI()` crea la instancia central de la aplicación.
- Los **decoradores** (`@app.get`, `@app.post`, etc.) asocian funciones con rutas HTTP.

### Parámetros de ruta y query

```python
# Parámetro de ruta — valor dinámico en la URL
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# Parámetros de query — después del ? en la URL
@app.get("/items/")
def list_items(skip: int = 0, limit: int = 10):
    return get_items(skip, limit)
# Uso: GET /items/?skip=0&limit=5
```

### APIRouter — Modularización de rutas

```python
# main.py — prefix global
app.include_router(api_router, prefix="/api/v1")

# Construcción de URLs:
# /api/v1  +  /auth  +  /login  =  /api/v1/auth/login
```

### Dependencias con Depends()

```python
def get_db():
    db = SessionLocal()
    try:
        yield db       # Se inyecta en el endpoint
    finally:
        db.close()     # Se cierra SIEMPRE
```

</details>

<details>
<summary><strong>🗄️ SQLAlchemy y ORM</strong></summary>

### ¿Qué es un ORM?

| Sin ORM (SQL puro) | Con ORM (SQLAlchemy) |
|---|---|
| `SELECT * FROM productos WHERE id = 1` | `db.get(Producto, 1)` |
| Atado a un motor de BD específico | Cambias de motor fácilmente |

### Operaciones de sesión

| Método | ¿Qué hace? |
|---|---|
| `db.add(obj)` | Marca para inserción |
| `db.commit()` | Ejecuta el cambio en la BD |
| `db.refresh(obj)` | Recarga desde la BD (ej: obtener `id` autogenerado) |
| `db.delete(obj)` | Marca para eliminación |

### Referencia CRUD: ORM vs SQL

| Operación | ORM | SQL |
|---|---|---|
| Listar | `db.query(Model).all()` | `SELECT * FROM tabla` |
| Buscar | `db.get(Model, id)` | `SELECT ... WHERE id=?` |
| Filtrar | `.filter_by(campo=val).all()` | `WHERE campo = val` |
| Insertar | `db.add(obj)` + `commit()` | `INSERT INTO ...` |
| Actualizar | `obj.campo = val` + `commit()` | `UPDATE ... SET ...` |
| Eliminar | `db.delete(obj)` + `commit()` | `DELETE FROM ... WHERE ...` |

### `filter` vs `filter_by`

```python
# filter → condiciones complejas (>, <, OR, LIKE)
db.query(Producto).filter(Producto.precio > 100).all()

# filter_by → igualdades simples (más legible)
db.query(ItemCarrito).filter_by(carrito_id=1, producto_id=5).first()
```

### Cascade y relaciones

```python
# ✅ Cascade del PADRE al HIJO
carrito = relationship("Carrito", cascade="all, delete-orphan")

# ❌ NUNCA cascade del HIJO al PADRE
usuario = relationship("Usuario", cascade="all, delete")  # ← INCORRECTO
```

</details>

<details>
<summary><strong>📝 Pydantic y Schemas</strong></summary>

### ¿Por qué Schemas si ya tengo Models?

| Aspecto | Modelo SQLAlchemy | Schema Pydantic |
|---|---|---|
| **Propósito** | Representar tabla en BD | Validar entrada/salida |
| **Hereda de** | `Base` | `BaseModel` |
| **Usado por** | SQLAlchemy (BD) | FastAPI (validación + docs) |

> 🔑 El **modelo** es la cocina. El **schema** es el menú.

### `from_attributes` (orm_mode)

```python
class ProductoResponse(BaseModel):
    id: int
    nombre: str
    class Config:
        from_attributes = True  # Pydantic v2
```

### `response_model` como filtro de seguridad

```python
@router.post("/usuarios", response_model=schemas.UsuarioResponse)
# UsuarioResponse NO incluye hashed_password → nunca se envía al cliente
```

</details>

---

## 📚 Recursos Útiles

| Recurso | Enlace |
|---|---|
| 📖 Documentación de FastAPI | [fastapi.tiangolo.com](https://fastapi.tiangolo.com) |
| 🗄️ FastAPI + SQL Databases | [Tutorial oficial](https://fastapi.tiangolo.com/tutorial/sql-databases/) |
| ✅ Documentación de Pydantic | [docs.pydantic.dev](https://docs.pydantic.dev/) |
| 🔧 Documentación de SQLAlchemy | [docs.sqlalchemy.org](https://docs.sqlalchemy.org/) |
| 🗃️ Documentación de Alembic | [alembic.sqlalchemy.org](https://alembic.sqlalchemy.org/) |
| 🔐 Documentación de python-jose | [python-jose.readthedocs.io](https://python-jose.readthedocs.io/) |
| 🔒 Documentación de passlib | [passlib.readthedocs.io](https://passlib.readthedocs.io/) |
| 🐱 Códigos de estado HTTP | [http.cat](https://http.cat/) |

---

<p align="center">
  Desarrollado por <strong><a href="https://github.com/JeikerM19">Jeiker Dev</a></strong> · 
  <a href="https://github.com/JeikerM19/FastApi_Ecommerce">⭐ Ver en GitHub</a>
</p>