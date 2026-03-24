# 🚀 Curso de Backend con FastAPI — E-Commerce API

Apuntes y proyecto práctico del curso de **Backend con Python y FastAPI**. Este repositorio documenta los conceptos fundamentales para construir APIs RESTful modernas, con un proyecto de e-commerce real como referencia.

El proyecto ha evolucionado desde una API básica hasta un sistema completo con autenticación JWT, carrito de compras, sistema de pedidos, control de stock y migraciones de base de datos con Alembic.

---

## 📋 Tabla de Contenidos

- [Fundamentos: API, REST, HTTP y JSON](#-fundamentos-api-rest-http-y-json)
- [Configuración del Entorno](#-configuración-del-entorno)
- [Variables de Entorno](#-variables-de-entorno)
- [Conceptos Básicos de FastAPI](#-conceptos-básicos-de-fastapi)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Base de Datos con SQLAlchemy](#-base-de-datos-con-sqlalchemy)
- [Modelos ORM](#-modelos-orm)
- [Relaciones entre Modelos](#-relaciones-entre-modelos)
- [Schemas Pydantic](#-schemas-pydantic)
- [Operaciones CRUD](#-operaciones-crud)
- [Seguridad y Autenticación](#-seguridad-y-autenticación)
- [Sistema de Rutas con APIRouter](#-sistema-de-rutas-con-apirouter)
- [Dependencias](#-dependencias)
- [Migraciones con Alembic](#-migraciones-con-alembic)
- [Sistema de Carrito de Compras](#-sistema-de-carrito-de-compras)
- [Sistema de Pedidos](#-sistema-de-pedidos)
- [Endpoints de la API](#-endpoints-de-la-api)
- [Recursos Útiles](#-recursos-útiles)

---

## 🌍 Fundamentos: API, REST, HTTP y JSON

### ¿Qué es una API?

Una **API** (Application Programming Interface) es un conjunto de reglas que permite que dos programas se comuniquen entre sí. Es como un **mesero en un restaurante**: tú (el cliente) no vas a la cocina directamente, le dices al mesero qué quieres y él te trae la comida.

```
┌──────────┐         ┌──────────┐         ┌──────────────┐
│ Cliente  │  ────►  │   API    │  ────►  │  Servidor /  │
│ (App,    │  ◄────  │ (mesero) │  ◄────  │  Base de     │
│ Browser) │         │          │         │  Datos       │
└──────────┘         └──────────┘         └──────────────┘
   Pide datos        Traduce y           Procesa y
   o acciones        entrega             responde
```

**Ejemplos reales de APIs:**
- Tu app del clima consulta una API meteorológica para obtener la temperatura.
- Un botón de "Iniciar sesión con Google" usa la API de Google.
- Una tienda online consulta una API de pagos (Stripe, PayPal) para procesar compras.

### ¿Qué es una API REST?

**REST** (Representational State Transfer) es un **estilo de arquitectura** — un conjunto de reglas para diseñar APIs. Una API que sigue estas reglas se llama **API RESTful**.

Las reglas principales de REST son:

| Principio                | Significado                                                                |
|--------------------------|----------------------------------------------------------------------------|
| **Cliente-Servidor**     | El cliente y el servidor son independientes. Cada uno evoluciona por separado. |
| **Sin estado (Stateless)** | Cada petición contiene **toda** la info necesaria. El servidor no recuerda peticiones anteriores. |
| **Recursos con URL**     | Cada "cosa" (usuario, producto, categoría) tiene una URL única que la identifica. |
| **Métodos HTTP estándar** | Se usan GET, POST, PUT, DELETE para las operaciones (no inventamos verbos nuevos). |
| **Respuestas en formato estándar** | Normalmente se usa **JSON** como formato de intercambio de datos. |

**Ejemplo REST en la práctica:**

```
Recurso: Productos de una tienda

GET    /productos       → Obtener todos los productos
GET    /productos/5     → Obtener el producto con id 5
POST   /productos       → Crear un nuevo producto
PUT    /productos/5     → Actualizar el producto con id 5
DELETE /productos/5     → Eliminar el producto con id 5
```

> 💡 En REST, las URLs representan **sustantivos** (recursos: `/productos`, `/usuarios`), y los métodos HTTP representan **verbos** (acciones: GET, POST, PUT, DELETE).

### ¿Qué es HTTP?

**HTTP** (HyperText Transfer Protocol) es el **protocolo de comunicación** que usan los navegadores y servidores para intercambiar información. Es el "idioma" que hablan el cliente y el servidor.

#### Anatomía de una petición HTTP

```
┌─────────────────────────────────────────────────┐
│ POST /api/v1/auth/login HTTP/1.1                │  ← Línea de petición (método + ruta)
│ Host: localhost:8000                            │  ← Headers
│ Content-Type: application/json                  │
│ Authorization: Bearer eyJhbGciOi...             │
│                                                 │
│ {"email": "carlos@gmail.com", "password": "..."} │  ← Body (cuerpo)
└─────────────────────────────────────────────────┘
```

| Parte          | Descripción                                               |
|----------------|-----------------------------------------------------------|
| **Método**     | La acción a realizar (GET, POST, PUT, DELETE)             |
| **Ruta (URL)** | El recurso al que se dirige la petición                   |
| **Headers**    | Metadatos: tipo de contenido, autenticación, etc.         |
| **Body**       | Los datos que se envían (solo en POST y PUT, generalmente) |

#### Códigos de estado HTTP

Cada respuesta del servidor incluye un **código numérico** que indica qué pasó:

| Código | Significado              | Cuándo aparece                           |
|--------|--------------------------|------------------------------------------|
| **200** | OK                      | La petición fue exitosa                  |
| **201** | Created                 | Se creó un recurso nuevo (registro exitoso) |
| **400** | Bad Request             | El cliente envió datos incorrectos       |
| **401** | Unauthorized            | No autenticado (falta token o es inválido) |
| **403** | Forbidden               | Autenticado pero sin permisos suficientes |
| **404** | Not Found               | El recurso no existe                     |
| **422** | Unprocessable Entity    | Los datos no pasaron la validación       |
| **500** | Internal Server Error   | Error interno del servidor               |

#### Los 4 métodos HTTP principales (CRUD)

| Método     | Operación | Descripción                   | ¿Lleva Body? |
|-----------|-----------|-------------------------------|--------------| 
| **GET**    | Read      | Obtener recursos              | No           |
| **POST**   | Create    | Crear un nuevo recurso        | Sí           |
| **PUT**    | Update    | Actualizar un recurso existente | Sí         |
| **DELETE** | Delete    | Eliminar un recurso existente | No (usualmente) |

> 🔑 **Clave:** GET y DELETE solo envían información en la URL. POST y PUT envían datos en el **body** de la petición.

### ¿Qué es JSON?

**JSON** (JavaScript Object Notation) es el **formato estándar** para intercambiar datos en APIs web.

```json
{
    "nombre": "Laptop Gaming",
    "precio": 1299.99,
    "en_stock": true,
    "stock": 15,
    "categorias": ["electrónica", "computadoras"]
}
```

| Tipo        | Ejemplo                          | Equivalente Python |
|-------------|----------------------------------|--------------------|
| **String**  | `"Laptop Gaming"`               | `str`              |
| **Number**  | `1299.99`, `42`                 | `float`, `int`     |
| **Boolean** | `true`, `false`                 | `True`, `False`    |
| **Array**   | `["a", "b", "c"]`              | `list`             |
| **Object**  | `{"clave": "valor"}`            | `dict`             |
| **Null**    | `null`                          | `None`             |

---

## 🛠 Configuración del Entorno

### 1. Crear y activar el entorno virtual

```bash
python -m venv venv
```

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

> 💡 Sabrás que el entorno está activo cuando veas `(venv)` al inicio de tu terminal.

### 2. Instalar dependencias

```bash
pip install fastapi uvicorn sqlalchemy pymysql passlib[bcrypt] python-jose[cryptography] python-multipart email-validator python-dotenv alembic pydantic-settings
```

| Paquete                        | Descripción                                                                |
|--------------------------------|----------------------------------------------------------------------------|
| **fastapi**                    | Framework moderno para crear APIs con Python, basado en type hints         |
| **uvicorn**                    | Servidor ASGI ultrarrápido para ejecutar la aplicación                     |
| **sqlalchemy**                 | ORM para interactuar con la base de datos usando objetos Python            |
| **pymysql**                    | Driver para conectar Python con MySQL                                      |
| **passlib[bcrypt]**            | Hashing seguro de contraseñas con bcrypt                                   |
| **python-jose[cryptography]**  | Creación y verificación de tokens JWT                                      |
| **python-multipart**           | Necesario para recibir datos de formularios (login con `OAuth2PasswordRequestForm`) |
| **email-validator**            | Validación automática de emails en schemas con `EmailStr`                  |
| **python-dotenv**              | Carga variables de entorno desde un archivo `.env`                         |
| **alembic**                    | Herramienta de migraciones de base de datos para SQLAlchemy                |
| **pydantic-settings**          | Carga centralizada de configuración desde `.env` con validación Pydantic   |

### 3. Ejecutar el servidor

```bash
# Desde la carpeta app/
cd app
uvicorn main:app --reload
```

- **API:** http://127.0.0.1:8000
- **Documentación Swagger:** http://127.0.0.1:8000/docs

---

## 🔒 Variables de Entorno

Las credenciales sensibles **nunca** deben estar en el código fuente. Se guardan en un archivo `.env` que **no se sube al repositorio** (está en `.gitignore`).

### Archivo `.env`

Crea un archivo `.env` en la **raíz del proyecto** (`FASTAPI/`) con las siguientes variables:

```env
# Base de Datos
DATABASE_URL=mysql+pymysql://usuario:contraseña@localhost:3306/nombre_bd

# JWT
SECRET_KEY=tu_clave_secreta_aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Cómo se cargan las variables (`core/config.py`)

```python
from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = Path(__file__).resolve().parent.parent.parent / ".env"

settings = Settings()
```

### Formato de la URL de conexión MySQL

```
mysql+pymysql://usuario:contraseña@localhost:3306/nombre_bd
│     │         │       │           │         │    └── Nombre de la BD
│     │         │       │           │         └── Puerto
│     │         │       │           └── Host del servidor
│     │         │       └── Contraseña
│     │         └── Usuario
│     └── Driver de Python
└── Dialecto (tipo de BD)
```

---

## ⚡ Conceptos Básicos de FastAPI

### Instancia y endpoints

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido a mi API"}
```

- `FastAPI()` crea la instancia central de la aplicación.
- Los **decoradores** (`@app.get`, `@app.post`, etc.) asocian funciones Python con rutas HTTP.
- Un **endpoint** es una URL que ejecuta una función cuando recibe una petición.

### Parámetros de Ruta y Query

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

---

## 📁 Estructura del Proyecto

```
FASTAPI/
├── .env                           # Variables de entorno (NO se sube a git)
├── .gitignore
├── Readme.md
└── app/
    ├── main.py                    # Punto de entrada: registra el api_router con prefix /api/v1
    ├── alembic/                   # Migraciones de base de datos
    │   ├── env.py                 # Configuración de Alembic (conecta con la BD y los modelos)
    │   └── versions/              # Scripts de migración autogenerados
    ├── api/
    │   └── api_v1/
    │       ├── api.py             # Router principal (agrupa todos los sub-routers)
    │       ├── auth.py            # Endpoints de registro y login
    │       ├── productos.py       # Endpoints de productos
    │       ├── categorias.py      # Endpoints de categorías
    │       ├── carrito.py         # Endpoints del carrito de compras
    │       └── pedido.py          # Endpoint de confirmación de pedido
    ├── core/
    │   ├── config.py              # Carga centralizada de variables de entorno
    │   └── security.py            # Hashing de contraseñas + generación/verificación de JWT
    ├── crud/
    │   ├── __init__.py            # Re-exporta todas las funciones CRUD
    │   ├── producto.py            # CRUD de productos
    │   ├── categoria.py           # CRUD de categorías
    │   ├── usuario.py             # CRUD de usuarios
    │   ├── carrito.py             # Lógica del carrito (obtener, agregar, eliminar items)
    │   └── pedido.py              # Lógica para confirmar un pedido desde el carrito
    ├── db/
    │   └── database.py            # Configuración del motor y sesión de SQLAlchemy
    ├── deps/
    │   └── deps.py                # Dependencias: get_db, get_current_user, requiere_admin
    ├── models/
    │   ├── __init__.py
    │   ├── producto.py            # Modelo ORM: Producto
    │   ├── categoria.py           # Modelo ORM: Categoria
    │   ├── usuario.py             # Modelo ORM: Usuario
    │   └── pedidos.py             # Modelos ORM: Carrito, ItemCarrito, Pedido, DetallePedido
    └── schemas/
        ├── __init__.py
        ├── producto.py
        ├── categoria.py
        ├── usuario.py
        └── token.py
```

### Principio de separación de responsabilidades

| Carpeta      | Responsabilidad                                          |
|-------------|----------------------------------------------------------|
| `api/`       | Definir los **endpoints** (rutas HTTP)                   |
| `core/`      | Lógica de **seguridad** (hashing, JWT)                   |
| `crud/`      | **Operaciones en la BD** (insertar, consultar, actualizar, eliminar) |
| `db/`        | **Conexión** y configuración de la base de datos         |
| `deps/`      | **Dependencias** reutilizables (sesión de BD, autenticación) |
| `models/`    | **Modelos ORM** (representan las tablas de la BD)        |
| `schemas/`   | **Schemas Pydantic** (validación de datos de entrada/salida) |

---

## 🗄 Base de Datos con SQLAlchemy

### ¿Qué es un ORM?

Un **ORM** (Object-Relational Mapping) permite interactuar con la base de datos usando **objetos Python** en lugar de SQL directo.

| Sin ORM (SQL puro)                         | Con ORM (SQLAlchemy)                   |
|--------------------------------------------|----------------------------------------|
| `SELECT * FROM productos WHERE id = 1`     | `db.get(Producto, 1)`                  |
| Errores detectados solo en ejecución       | Errores detectados por el IDE y Python |
| Atado a un motor de BD específico          | Puedes cambiar de motor fácilmente     |

### Conexión a la BD (`db/database.py`)

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

| Componente               | ¿Qué hace?                                                              |
|--------------------------|--------------------------------------------------------------------------|
| `create_engine(URL)`     | Crea el motor de conexión: puente entre Python y la BD                   |
| `declarative_base()`     | Genera la clase base de la que heredan todos los modelos                 |
| `sessionmaker(...)`      | Fábrica de sesiones: cada sesión es una "conversación" con la BD         |

| Parámetro de sessionmaker | Valor   | ¿Por qué?                                                     |
|---------------------------|---------|----------------------------------------------------------------|
| `autocommit`              | `False` | Tú decides cuándo hacer `commit()`, dándote control total      |
| `autoflush`               | `False` | No envía cambios pendientes antes de cada consulta             |

### Operaciones de sesión

| Método            | ¿Qué hace?                                              |
|-------------------|---------------------------------------------------------|
| `db.add(obj)`     | Marca el objeto para ser insertado (aún no va a la BD)  |
| `db.commit()`     | Ejecuta el INSERT/UPDATE/DELETE real en la BD            |
| `db.refresh(obj)` | Recarga el objeto desde la BD (útil para obtener el `id` autogenerado) |
| `db.delete(obj)`  | Marca el objeto para eliminarse en el próximo commit     |

---

## 📊 Modelos ORM

Los modelos son **clases Python que representan tablas** en la base de datos. Cada atributo corresponde a una columna.

### Modelo Producto

```python
class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True)
    precio = Column(Float)
    en_stock = Column(Boolean, default=True)   # ¿Está disponible para venta?
    stock = Column(Integer, default=0)         # Cantidad disponible en inventario
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    categorias = relationship("Categoria", back_populates="productos")
```

> ⚠️ **Importante:** `en_stock` (Boolean) y `stock` (Integer) son campos distintos. `en_stock` indica si el producto está activo/disponible para venta (se puede desactivar manualmente un producto). `stock` indica cuántas unidades físicas quedan en inventario y se descuenta automáticamente al confirmar un pedido.

### Modelo Usuario

```python
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100))
    es_admin = Column(Boolean, default=False)
    carrito = relationship("Carrito", back_populates="usuario", uselist=False, cascade="all, delete-orphan")
    pedidos = relationship("Pedido", back_populates="usuario", cascade="all, delete-orphan")
```

> 💡 `uselist=False` en `carrito` indica que la relación devuelve **un solo objeto** (no una lista), porque un usuario solo tiene un carrito activo a la vez.

### Modelos de Pedidos (`models/pedidos.py`)

```python
class Carrito(Base):
    __tablename__ = "carritos"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    usuario = relationship("Usuario", back_populates="carrito")
    items = relationship("ItemCarrito", back_populates="carrito", cascade="all, delete-orphan")

class ItemCarrito(Base):
    __tablename__ = "items_carrito"
    id = Column(Integer, primary_key=True, index=True)
    carrito_id = Column(Integer, ForeignKey("carritos.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer, default=1)
    carrito = relationship("Carrito", back_populates="items")
    producto = relationship("Producto")

class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    fecha = Column(DateTime, default=datetime.now)
    total = Column(Float)
    detalles = relationship("DetallePedido", back_populates="pedido")
    usuario = relationship("Usuario", back_populates="pedidos")

class DetallePedido(Base):
    __tablename__ = "detalles_pedidos"
    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer)
    subtotal = Column(Float)
    pedido = relationship("Pedido", back_populates="detalles")
```

### Referencia rápida de columnas

| Tipo SQLAlchemy | SQL equivalente | Ejemplo de uso                    |
|-----------------|-----------------|-----------------------------------|
| `Integer`       | `INT`           | IDs, cantidades, stock            |
| `String(n)`     | `VARCHAR(n)`    | Nombres, emails                   |
| `Float`         | `FLOAT`         | Precios, totales                  |
| `Boolean`       | `TINYINT(1)`    | Flags como `en_stock`, `es_admin` |
| `DateTime`      | `DATETIME`      | Fechas de pedidos                 |

| Parámetro de `Column`          | Descripción                                                 |
|-------------------------------|-------------------------------------------------------------|
| `primary_key=True`            | Clave primaria (identificador único de cada fila)           |
| `index=True`                  | Índice para búsquedas más rápidas                           |
| `unique=True`                 | No permite valores duplicados                               |
| `default=valor`               | Valor por defecto si no se especifica                       |
| `ForeignKey("tabla.columna")` | Clave foránea: vincula con otra tabla                       |

---

## 🔗 Relaciones entre Modelos

El proyecto implementa varias relaciones uno-a-muchos usando `relationship` y `back_populates`. Entender cómo funcionan es crítico para evitar errores.

### Diagrama de la base de datos

```
usuarios ──────────── carritos ──────────── items_carrito ──── productos
    │                                                               │
    └───────────────── pedidos ──────────── detalles_pedidos ──────┘
                          │
                      categorias
```

### Reglas del `cascade`

El parámetro `cascade` determina qué pasa con los registros hijos cuando se borra el padre:

```python
# ✅ CORRECTO: el cascade siempre va del PADRE al HIJO
# Si borro un usuario, se borran su carrito y sus pedidos
carrito = relationship("Carrito", cascade="all, delete-orphan")
pedidos = relationship("Pedido", cascade="all, delete-orphan")

# ❌ INCORRECTO: el carrito NO debe borrar al usuario (su padre)
usuario = relationship("Usuario", cascade="all, delete")  # ← esto borra al usuario al borrar el carrito
```

> ⚠️ Un error muy común es agregar `cascade` en la dirección equivocada. En la relación `Carrito → Usuario`, el carrito es el hijo y **nunca debe tener un cascade que afecte al padre**.

### `back_populates` vs `backref`

Ambos crean la relación bidireccional, pero `back_populates` es más explícito y es la forma recomendada en SQLAlchemy moderno:

```python
# En Usuario:
carrito = relationship("Carrito", back_populates="usuario")

# En Carrito (debe coincidir con el nombre en Usuario):
usuario = relationship("Usuario", back_populates="carrito")
```

---

## 📝 Schemas Pydantic

### ¿Por qué necesito Schemas si ya tengo Models?

| Aspecto          | Modelo SQLAlchemy (`models/`)        | Schema Pydantic (`schemas/`)        |
|------------------|--------------------------------------|-------------------------------------|
| **Propósito**    | Representar una tabla en la BD       | Validar datos de entrada/salida     |
| **Hereda de**    | `Base` (SQLAlchemy)                  | `BaseModel` (Pydantic)              |
| **Usado por**    | SQLAlchemy para operaciones de BD    | FastAPI para validación y docs      |

> 🔑 **Analogía:** El **modelo** es la cocina (cómo se almacenan los datos). El **schema** es el menú (qué puede pedir/recibir el cliente).

### Schemas típicos por entidad

```python
class ProductoCreate(BaseModel):    # Para POST: lo que envía el cliente
    nombre: str
    precio: float
    en_stock: bool
    stock: int
    categoria_id: int

class ProductoResponse(ProductoCreate):  # Para GET: lo que devuelve la API
    id: int
    class Config:
        from_attributes = True  # Permite leer atributos de objetos SQLAlchemy
```

### `orm_mode` / `from_attributes`

SQLAlchemy devuelve **objetos** Python (con `.nombre`, `.precio`), no diccionarios. Pydantic por defecto solo lee diccionarios. Esta configuración lo soluciona:

```python
class Config:
    from_attributes = True  # Pydantic v2
    # orm_mode = True       # Pydantic v1
```

> 📝 **Regla:** Todo schema que devuelva datos de la BD necesita `from_attributes = True`.

### `response_model` — Filtrando las respuestas

```python
@router.post("/usuarios", response_model=schemas.UsuarioResponse)
```

Aunque el modelo tenga `hashed_password`, si `UsuarioResponse` no lo incluye, **nunca se envía al cliente**. Es un filtro de seguridad automático.

---

## 🔧 Operaciones CRUD

Las funciones CRUD viven en `crud/` y son las únicas que interactúan directamente con la BD. Los endpoints **nunca** tocan la BD directamente.

### Referencia rápida: ORM vs SQL

| Operación       | ORM (Python)                                        | SQL equivalente                        |
|-----------------|-----------------------------------------------------|----------------------------------------|
| Listar todos    | `db.query(Producto).all()`                          | `SELECT * FROM productos`              |
| Buscar por ID   | `db.get(Producto, 1)`                               | `SELECT * FROM productos WHERE id=1`   |
| Filtrar         | `db.query(Producto).filter_by(en_stock=True).all()` | `SELECT * FROM productos WHERE ...`    |
| Insertar        | `db.add(nuevo)` + `db.commit()`                     | `INSERT INTO productos (...) VALUES (...)` |
| Actualizar      | Modificar atributos + `db.commit()`                 | `UPDATE productos SET ... WHERE id=?`  |
| Eliminar        | `db.delete(obj)` + `db.commit()`                    | `DELETE FROM productos WHERE id=?`     |

### `filter` vs `filter_by`

SQLAlchemy ofrece dos formas de filtrar:

```python
# filter → para condiciones complejas (comparaciones, OR, LIKE, etc.)
db.query(Producto).filter(Producto.precio > 100).all()
db.query(Producto).filter(Producto.id == 1, Producto.en_stock == True).first()

# filter_by → para igualdades simples (más legible)
db.query(ItemCarrito).filter_by(carrito_id=1, producto_id=5).first()
# Equivale a: WHERE carrito_id = 1 AND producto_id = 5
```

> ⚠️ Con `filter`, **debes** usar el prefijo del modelo (`Producto.precio`). Sin él, estás comparando variables de Python entre sí, no columnas de la BD.

---

## 🔐 Seguridad y Autenticación

### Hashing de contraseñas (bcrypt)

```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)
```

| Función               | ¿Cuándo se usa?              |
|-----------------------|------------------------------|
| `hash_password()`     | Al **registrar** un usuario  |
| `verify_password()`   | Al hacer **login**           |

> ⚠️ `verify_password` **no desencripta** el hash. Hashea la contraseña ingresada y compara. El hash es **irreversible**.

### Tokens JWT

```python
def crear_token(sub: str, es_admin: bool) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data = {"sub": sub, "exp": expire, "es_admin": es_admin}
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return None
```

Un JWT tiene 3 partes: **Header** (algoritmo) · **Payload** (datos + expiración) · **Firma** (verificación).

### Flujo completo de autenticación

```
1. REGISTRO   → hash_password(password) → Se guarda hash en BD (nunca el texto plano)
2. LOGIN      → verify_password(password, hash_guardado)
               → Si coincide: crear_token(email, es_admin) → Devuelve token JWT
3. PETICIÓN   → El cliente envía: Authorization: Bearer <token>
4. VALIDACIÓN → get_current_user() llama verificar_token() → Si válido: devuelve el usuario
```

---

## 🗂 Sistema de Rutas con APIRouter

`APIRouter` permite dividir los endpoints en **múltiples archivos organizados por funcionalidad**.

### Punto de entrada (`main.py`)

```python
from fastapi import FastAPI
from api.api_v1.api import api_router

app = FastAPI()
app.include_router(api_router, prefix="/api/v1")
```

### Router principal (`api/api_v1/api.py`)

```python
api_router = APIRouter()
api_router.include_router(auth.api_router,      prefix="/auth",      tags=["auth"])
api_router.include_router(productos.api_router,  prefix="/productos",  tags=["productos"])
api_router.include_router(categorias.api_router, prefix="/categorias", tags=["categorias"])
api_router.include_router(carrito.api_router,    prefix="/carrito",    tags=["carritos"])
api_router.include_router(pedido.api_router,     prefix="/pedido",     tags=["pedidos"])
```

### Cómo se construyen las URLs

```
main.py prefix  +  api.py prefix  +  endpoint path  =  URL final
"/api/v1"       +  "/auth"        +  "/login"        =  /api/v1/auth/login
"/api/v1"       +  "/carrito"     +  "/agregar/3"    =  /api/v1/carrito/agregar/3
```

---

## 🔗 Dependencias

Las dependencias viven en `deps/deps.py` y se inyectan con `Depends()` en los endpoints.

### Sesión de Base de Datos (`get_db`)

```python
def get_db():
    db = SessionLocal()
    try:
        yield db       # ← FastAPI inyecta la sesión en el endpoint
    finally:
        db.close()     # ← Se ejecuta SIEMPRE, aunque ocurra un error
```

`yield` garantiza que la conexión se cierre **siempre**, incluso si hay excepciones.

### Autenticación (`get_current_user`)

```python
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verificar_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="No autenticado")
    email = payload.get("sub")
    user = crud.obtener_usuario_por_email(db, email)
    if user is None:
        raise HTTPException(status_code=401, detail="No autenticado")
    return user
```

`OAuth2PasswordBearer` le dice a FastAPI que espere un token en el header `Authorization: Bearer <token>`.

### Permisos de Admin (`requiere_admin`)

```python
def requiere_admin(current_user = Depends(get_current_user)):
    if not current_user.es_admin:
        raise HTTPException(status_code=403, detail="No autorizado, requiere admin")
```

---

## 🗃 Migraciones con Alembic

### ¿Por qué Alembic?

`Base.metadata.create_all()` solo crea tablas que **no existen**. Si agregas una columna nueva a un modelo, **no modifica la tabla existente**. Alembic detecta los cambios y genera scripts SQL para aplicarlos sin perder datos.

### Configuración inicial

```bash
cd app
alembic init alembic
```

Esto crea la carpeta `alembic/` con `env.py` y `alembic.ini`. El archivo `env.py` debe configurarse para apuntar a la BD y a los modelos:

```python
# En alembic/env.py
from core.config import settings
from db.database import Base
from models import *  # Importar todos los modelos para que Alembic los detecte

config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)
target_metadata = Base.metadata
```

### Flujo de trabajo de Alembic

```bash
# 1. Detecta cambios en los modelos y genera un script de migración
alembic revision --autogenerate -m "descripcion del cambio"

# 2. Aplica todas las migraciones pendientes
alembic upgrade head

# 3. Ver el estado actual
alembic current

# 4. Ver historial de migraciones
alembic history
```

### ¿Cuándo se necesita una migración?

| Cambio                              | ¿Requiere migración? |
|-------------------------------------|----------------------|
| Agregar una columna nueva           | ✅ Sí               |
| Cambiar el tipo de una columna      | ✅ Sí               |
| Agregar una nueva tabla             | ✅ Sí               |
| Agregar/modificar un `relationship` | ❌ No (es ORM, no BD) |
| Cambiar el nombre de un `relationship` | ❌ No            |

> 💡 Los `relationship` de SQLAlchemy son **solo Python**: no generan columnas ni tablas en la BD. Por eso Alembic no los detecta y las migraciones de solo-relaciones quedan vacías (`pass`).

---

## 🛒 Sistema de Carrito de Compras

El carrito es una entidad **temporal** que almacena los productos que el usuario quiere comprar antes de confirmar el pedido.

### Flujo del carrito

```
1. obtener_carrito(usuario_id) → Si no existe, se crea automáticamente
2. agregar_item(carrito_id, producto_id, cantidad)
   - Si el producto ya está en el carrito → suma la cantidad
   - Si no está → crea un nuevo ItemCarrito
3. eliminar_item(item_id) → Borra un producto específico del carrito
```

### CRUD del carrito (`crud/carrito.py`)

```python
def obtener_carrito(db: Session, usuario_id: int):
    carrito = db.query(Carrito).filter(Carrito.usuario_id == usuario_id).first()
    if not carrito:
        carrito = Carrito(usuario_id=usuario_id)
        db.add(carrito)
        db.commit()
        db.refresh(carrito)
    return carrito

def agregar_item(db: Session, carrito_id: int, producto_id: int, cantidad: int = 1):
    item = db.query(ItemCarrito).filter_by(carrito_id=carrito_id, producto_id=producto_id).first()
    if item:
        item.cantidad += cantidad   # Ya existe → solo suma
    else:
        item = ItemCarrito(carrito_id=carrito_id, producto_id=producto_id, cantidad=cantidad)
        db.add(item)
    db.commit()
    db.refresh(item)
    return item
```

### ¿Cómo sabe el sistema de qué usuario es el carrito?

El endpoint de carrito usa `Depends(get_current_user)`. FastAPI decodifica el JWT del header `Authorization` y devuelve el objeto `usuario`. Con `user.id` se busca el carrito:

```python
@api_router.get("/")
def ver_carrito(db = Depends(get_db), user = Depends(get_current_user)):
    return crud_carrito.obtener_carrito(db, user.id)
```

---

## 📦 Sistema de Pedidos

El pedido es el **registro permanente** de una compra. Se crea a partir del carrito y no desaparece cuando el carrito se vacía.

### Diferencia entre Carrito y Pedido

| Aspecto      | Carrito (`carritos` + `items_carrito`) | Pedido (`pedidos` + `detalles_pedidos`) |
|-------------|----------------------------------------|-----------------------------------------|
| **Duración** | Temporal — desaparece al confirmar     | Permanente — historial de compras       |
| **Contenido**| Items que el usuario *quiere* comprar  | Items que el usuario *compró*           |
| **Referencia**| Apunta a `productos` (directo)        | Apunta a `productos` (directo)          |
| **Total**    | No tiene total                         | Tiene total calculado                   |

> 💡 Tanto `items_carrito` como `detalles_pedidos` apuntan directamente a `productos` (no el uno al otro). Esto es correcto: los detalles del pedido son un registro histórico independiente del carrito. Si el carrito se borrara y los detalles apuntaran a `items_carrito`, se borrría el historial del pedido.

### Lógica de confirmación de pedido (`crud/pedido.py`)

```python
def crear_pedido(db: Session, usuario_id: int):
    carrito = db.query(Carrito).filter_by(usuario_id=usuario_id).first()

    if not carrito or not carrito.items:
        raise ValueError("El carrito esta vacio")

    total = 0
    pedido = Pedido(usuario_id=usuario_id, total=0)
    db.add(pedido)
    db.commit()
    db.refresh(pedido)  # Necesario para obtener el id generado

    for item in carrito.items:
        producto = db.get(Producto, item.producto_id)

        if not producto.stock or producto.precio <= 0:
            continue  # Saltar productos sin stock o precio inválido

        if 0 < item.cantidad <= producto.stock:
            subtotal = producto.precio * item.cantidad
            producto.stock -= item.cantidad  # Descontar del inventario
            detalle = DetallePedido(
                pedido_id=pedido.id,
                producto_id=producto.id,
                cantidad=item.cantidad,
                subtotal=subtotal
            )
            db.add(detalle)
            total += subtotal

    pedido.total = total
    db.commit()

    # Limpiar el carrito tras la compra
    for item in carrito.items:
        db.delete(item)
    db.delete(carrito)
    db.commit()

    return pedido
```

### Flujo completo del e-commerce

```
1. POST /auth/registro        → Crear usuario
2. POST /auth/login           → Obtener JWT token
3. POST /carrito/agregar/{id} → Agregar producto al carrito (requiere token)
4. GET  /carrito/             → Ver contenido del carrito (requiere token)
5. POST /pedido/confirmar     → Convertir carrito en pedido (requiere token)
                                → Stock se descuenta, carrito se elimina
```

---

## 🌐 Endpoints de la API

> Todas las rutas llevan el prefijo `/api/v1/` definido en `main.py`.

### Auth

| Método | Ruta                 | Descripción                    | Protegido         |
|--------|----------------------|--------------------------------|-------------------|
| POST   | `/auth/usuarios`     | Registrar un nuevo usuario     | No                |
| POST   | `/auth/login`        | Login (devuelve JWT)           | No                |
| GET    | `/auth/usuarios/me`  | Ver perfil del usuario actual  | Sí (token)        |
| GET    | `/auth/admin/ping`   | Verificar permisos de admin    | Sí (solo admins)  |

### Productos

| Método | Ruta                   | Descripción                    | Protegido         |
|--------|------------------------|--------------------------------|-------------------|
| GET    | `/productos/`          | Listar todos los productos     | No                |
| POST   | `/productos/`          | Crear un producto              | Sí (solo admins)  |
| PUT    | `/productos/{id}`      | Actualizar un producto         | Sí (solo admins)  |
| DELETE | `/productos/{id}`      | Eliminar un producto           | Sí (solo admins)  |

### Categorías

| Método | Ruta              | Descripción                  | Protegido |
|--------|-------------------|------------------------------|-----------|
| POST   | `/categorias/`    | Crear una categoría          | No        |
| GET    | `/categorias/`    | Listar todas las categorías  | No        |

### Carrito

| Método | Ruta                       | Descripción                              | Protegido |
|--------|----------------------------|------------------------------------------|-----------|
| GET    | `/carrito/`                | Ver carrito del usuario autenticado      | Sí        |
| POST   | `/carrito/agregar/{id}`    | Agregar un producto al carrito           | Sí        |
| DELETE | `/carrito/eliminar/{id}`   | Eliminar un item del carrito             | Sí        |

### Pedidos

| Método | Ruta                | Descripción                                         | Protegido |
|--------|---------------------|-----------------------------------------------------|-----------|
| POST   | `/pedido/confirmar` | Confirmar la compra → convierte el carrito en pedido | Sí        |

---

## 📚 Recursos Útiles

| Recurso                            | Enlace                                                                          |
|------------------------------------|---------------------------------------------------------------------------------|
| Documentación oficial de FastAPI   | [fastapi.tiangolo.com](https://fastapi.tiangolo.com)                            |
| FastAPI + SQL Databases            | [fastapi.tiangolo.com/tutorial/sql-databases](https://fastapi.tiangolo.com/tutorial/sql-databases/) |
| Documentación de Pydantic          | [docs.pydantic.dev](https://docs.pydantic.dev/)                                |
| Documentación de SQLAlchemy        | [docs.sqlalchemy.org](https://docs.sqlalchemy.org/)                             |
| Documentación de Alembic           | [alembic.sqlalchemy.org](https://alembic.sqlalchemy.org/)                       |
| Documentación de python-jose (JWT) | [python-jose.readthedocs.io](https://python-jose.readthedocs.io/)              |
| Documentación de passlib           | [passlib.readthedocs.io](https://passlib.readthedocs.io/)                      |