# 🚀 Curso de Backend con FastAPI

Apuntes y proyecto práctico del curso de **Backend con Python y FastAPI**. Este repositorio documenta los conceptos fundamentales para construir APIs RESTful modernas, con un proyecto de e-commerce como referencia.

---

## 📋 Tabla de Contenidos

- [Fundamentos: API, REST, HTTP y JSON](#-fundamentos-api-rest-http-y-json)
- [Configuración del Entorno](#-configuración-del-entorno)
- [Variables de Entorno](#-variables-de-entorno)
- [Conceptos Básicos de FastAPI](#-conceptos-básicos-de-fastapi)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Base de Datos con SQLAlchemy](#-base-de-datos-con-sqlalchemy)
- [Modelos ORM](#-modelos-orm)
- [Schemas Pydantic](#-schemas-pydantic)
- [Operaciones CRUD](#-operaciones-crud)
- [Seguridad y Autenticación](#-seguridad-y-autenticación)
- [Sistema de Rutas con APIRouter](#-sistema-de-rutas-con-apirouter)
- [Dependencias](#-dependencias)
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

**JSON** (JavaScript Object Notation) es el **formato estándar** para intercambiar datos en APIs web. Es texto plano que tanto humanos como máquinas pueden leer fácilmente.

```json
{
    "nombre": "Laptop Gaming",
    "precio": 1299.99,
    "en_stock": true,
    "categorias": ["electrónica", "computadoras"],
    "detalles": {
        "marca": "ASUS",
        "ram": "16GB"
    }
}
```

#### Tipos de datos en JSON

| Tipo        | Ejemplo                          | Equivalente Python |
|-------------|----------------------------------|--------------------|
| **String**  | `"Laptop Gaming"`               | `str`              |
| **Number**  | `1299.99`, `42`                 | `float`, `int`     |
| **Boolean** | `true`, `false`                 | `True`, `False`    |
| **Array**   | `["a", "b", "c"]`              | `list`             |
| **Object**  | `{"clave": "valor"}`            | `dict`             |
| **Null**    | `null`                          | `None`             |

> 📝 JSON es el formato que FastAPI usa por defecto para recibir datos (`Request Body`) y enviar respuestas. Cuando defines un schema Pydantic, FastAPI convierte automáticamente entre JSON y objetos Python.

### ¿Cómo se conecta todo?

```
                    Protocolo HTTP
Cliente ─────────────────────────────────────► Servidor (FastAPI)
        ◄─────────────────────────────────────
        
El cliente envía:                 El servidor responde:
  • Método HTTP (GET, POST...)     • Código de estado (200, 404...)
  • URL del recurso                • Headers de respuesta
  • Headers (Auth, Content-Type)   • Body en formato JSON
  • Body en formato JSON (si aplica)
```

---

## 🛠 Configuración del Entorno

### 1. Crear y activar el entorno virtual

```bash
python -m venv venv
```

**Windows (PowerShell):**

```powershell
cd venv\Scripts
.\activate
```

> 💡 Sabrás que el entorno está activo cuando veas `(venv)` al inicio de tu terminal.

### 2. Instalar dependencias

```bash
pip install fastapi uvicorn sqlalchemy pymysql passlib[bcrypt] python-jose[cryptography] python-multipart email-validator python-dotenv
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

### 3. Ejecutar el servidor

```bash
uvicorn main:app --reload
```

| Parte      | Significado                                                   |
|------------|---------------------------------------------------------------|
| `main`     | Nombre del archivo Python (`main.py`)                         |
| `app`      | Nombre de la instancia de FastAPI dentro del archivo          |
| `--reload` | Reinicia el servidor al detectar cambios en el código         |

- **API:** http://127.0.0.1:8000
- **Documentación Swagger:** http://127.0.0.1:8000/docs

---

## 🔒 Variables de Entorno

Las credenciales sensibles (contraseñas de BD, claves secretas) **nunca** deben estar en el código fuente. Se guardan en un archivo `.env` que no se sube al repositorio.

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

### Cómo se cargan las variables

Usamos `pydantic-settings` para centralizar la carga del archivo `.env`. Creamos un archivo `app/core/config.py`:

```python
from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        # Busca el .env en la raíz del proyecto
        env_file = Path(__file__).resolve().parent.parent.parent / ".env"

# Instancia global para usar en el resto de la app
settings = Settings()
```

Ahora en cualquier archivo (como `database.py` o `security.py`), simplemente importamos `settings`:

```python
from core.config import settings

print(settings.DATABASE_URL)
```

> ⚠️ **Importante:** Asegúrate de agregar `.env` a tu `.gitignore` para que **nunca** se suba al repositorio. Las credenciales expuestas son un riesgo de seguridad grave.

### Formato de la URL de conexión

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

### ¿Qué es FastAPI?

Framework web moderno para Python que utiliza **type hints** para validación automática y generación de documentación. Incluye Swagger UI integrado.

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

- FastAPI hace **validación automática** de tipos.
- Parámetros con **valor por defecto** son opcionales; sin default, son obligatorios.

---

## 📁 Estructura del Proyecto

```
FASTAPI/
├── .env                           # Variables de entorno (NO se sube a git)
├── .gitignore                     # Archivos ignorados por git
├── Readme.md                      # Documentación del proyecto
└── app/
    ├── main.py                    # Punto de entrada de la aplicación
    ├── api/
    │   └── api_v1/
    │       ├── api.py             # Router principal (agrupa todos los sub-routers)
    │       ├── auth.py            # Endpoints de autenticación y usuarios
    │       ├── productos.py       # Endpoints de productos
    │       └── categorias.py      # Endpoints de categorías
    ├── core/
    │   ├── config.py              # Carga centralizada de variables de entorno (BaseSettings)
    │   └── security.py            # Hashing de contraseñas + JWT
    ├── crud/
    │   ├── __init__.py            # Re-exporta todas las funciones CRUD
    │   ├── producto.py            # CRUD de productos
    │   ├── categoria.py           # CRUD de categorías
    │   └── usuario.py             # CRUD de usuarios
    ├── db/
    │   ├── database.py            # Configuración de conexión a la BD
    │   └── init_db.py             # Script para crear las tablas
    ├── deps/
    │   └── deps.py                # Dependencias (get_db, autenticación, permisos)
    ├── models/
    │   ├── __init__.py            # Re-exporta todos los modelos
    │   ├── producto.py            # Modelo ORM de Producto
    │   ├── categoria.py           # Modelo ORM de Categoría
    │   └── usuario.py             # Modelo ORM de Usuario
    └── schemas/
        ├── __init__.py            # Re-exporta todos los schemas
        ├── producto.py            # Schemas de Producto
        ├── categoria.py           # Schemas de Categoría
        ├── usuario.py             # Schemas de Usuario
        └── token.py               # Schema de Token JWT
```

### Principio de separación de responsabilidades

Cada carpeta tiene una función específica:

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
| `SELECT * FROM productos WHERE id = 1`     | `db.query(Producto).get(1)`            |
| Errores detectados solo en ejecución       | Errores detectados por el IDE y Python |
| Atado a un motor de BD específico          | Puedes cambiar de motor fácilmente     |

### Conexión a la BD (`db/database.py`)

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

| Componente               | ¿Qué hace?                                                              |
|--------------------------|--------------------------------------------------------------------------|
| `settings.DATABASE_URL`  | Lee la URL de conexión desde `config.py`                                 |
| `create_engine(URL)`     | Crea el motor de conexión: puente entre Python y la BD                   |
| `declarative_base()`     | Genera la clase base de la que heredan todos los modelos                 |
| `sessionmaker(...)`      | Fábrica de sesiones: cada sesión es una "conversación" con la BD         |

| Parámetro de sessionmaker | Valor   | ¿Por qué?                                                     |
|---------------------------|---------|----------------------------------------------------------------|
| `autocommit`              | `False` | Tú decides cuándo hacer `commit()`, dándote control total      |
| `autoflush`               | `False` | No envía cambios pendientes antes de cada consulta             |
| `bind`                    | `engine`| Conecta la sesión al motor de BD                               |

### Creación de tablas (`db/init_db.py`)

```python
from db.database import engine, Base
from models import *  # Importa todos los modelos para que Base los registre

Base.metadata.create_all(bind=engine)
print("Tablas creadas correctamente")
```

> 📝 `create_all` solo crea tablas que **no existen**. No modifica tablas existentes. Para migraciones, se usa **Alembic**.

---

## 📊 Modelos ORM

Los modelos son **clases Python que representan tablas** en la base de datos. Cada atributo corresponde a una columna. Viven en `models/`.

### Modelo Producto (`models/producto.py`)

```python
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True)
    precio = Column(Float)
    en_stock = Column(Boolean, default=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    categorias = relationship("Categoria", back_populates="productos")
```

### Modelo Categoría (`models/categoria.py`)

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, index=True)
    productos = relationship("Producto", back_populates="categorias")
```

### Modelo Usuario (`models/usuario.py`)

```python
from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100))       # Contraseña hasheada, nunca texto plano
    es_admin = Column(Boolean, default=False)   # Rol del usuario
```

### Referencia rápida de columnas SQLAlchemy

| Tipo SQLAlchemy | SQL equivalente | Ejemplo de uso                    |
|-----------------|-----------------|-----------------------------------|
| `Integer`       | `INT`           | IDs, cantidades                   |
| `String(n)`     | `VARCHAR(n)`    | Nombres, emails                   |
| `Float`         | `FLOAT`         | Precios                           |
| `Boolean`       | `BOOLEAN`       | Flags como `en_stock`, `es_admin` |

| Parámetro de `Column`          | Descripción                                                 |
|-------------------------------|-------------------------------------------------------------|
| `primary_key=True`            | Clave primaria (identificador único de cada fila)           |
| `index=True`                  | Índice para búsquedas más rápidas                           |
| `unique=True`                 | No permite valores duplicados                               |
| `default=valor`               | Valor por defecto si no se especifica                       |
| `ForeignKey("tabla.columna")` | Clave foránea: vincula con otra tabla                       |

### Relaciones entre tablas

Una categoría tiene **muchos** productos, y cada producto pertenece a **una** categoría (relación uno-a-muchos):

```
┌──────────────┐          ┌──────────────────┐
│  Categorías  │          │    Productos     │
├──────────────┤          ├──────────────────┤
│ id (PK)      │◄────────┐│ id (PK)          │
│ nombre       │         ││ nombre           │
│              │         ││ precio           │
│              │         ││ en_stock         │
│              │         └│ categoria_id (FK)│
└──────────────┘          └──────────────────┘
     1                           Muchos
```

Se construye en 2 pasos:

1. **Clave foránea** en el modelo del lado "muchos":
   ```python
   categoria_id = Column(Integer, ForeignKey("categorias.id"))
   ```

2. **Relación bidireccional** con `relationship` en ambos modelos:
   ```python
   # En Producto:
   categorias = relationship("Categoria", back_populates="productos")
   # En Categoria:
   productos = relationship("Producto", back_populates="categorias")
   ```

> 💡 `back_populates` permite navegar en ambas direcciones: `producto.categorias` y `categoria.productos`.

### Re-exportación con `__init__.py`

`models/__init__.py` re-exporta todos los modelos para importarlos fácilmente:

```python
from .producto import Producto
from .categoria import Categoria
from .usuario import Usuario
```

Esto permite hacer `from models import Producto` desde cualquier parte del proyecto.

---

## 📝 Schemas Pydantic

### ¿Por qué necesito Schemas si ya tengo Models?

Hacen **trabajos completamente diferentes**:

| Aspecto          | Modelo SQLAlchemy (`models/`)        | Schema Pydantic (`schemas/`)        |
|------------------|--------------------------------------|-------------------------------------|
| **Propósito**    | Representar una tabla en la BD       | Validar datos de entrada/salida     |
| **Hereda de**    | `Base` (SQLAlchemy)                  | `BaseModel` (Pydantic)              |
| **Usado por**    | SQLAlchemy para operaciones de BD    | FastAPI para validación y docs      |

> 🔑 **Analogía:** El **modelo** es la cocina (cómo se almacenan los datos). El **schema** es el menú (qué puede pedir/recibir el cliente).

### Schemas de Producto (`schemas/producto.py`)

```python
from pydantic import BaseModel

class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    en_stock: bool
    categoria_id: int

class ProductoResponse(ProductoCreate):
    id: int
    class Config:
        from_attributes = True  # Permite leer datos de objetos SQLAlchemy
```

### Schemas de Categoría (`schemas/categoria.py`)

```python
from pydantic import BaseModel

class CategoriaBase(BaseModel):
    nombre: str

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaResponse(CategoriaBase):
    id: int
    class Config:
        orm_mode = True
```

### Schemas de Usuario (`schemas/usuario.py`)

```python
from pydantic import BaseModel, EmailStr

class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr              # Valida que sea un email real

class UsuarioCreate(UsuarioBase):
    password: str                # Texto plano (se hashea en el backend)
    es_admin: bool = False

class UsuarioResponse(UsuarioBase):
    id: int
    es_admin: bool
    class Config:
        from_attributes = True
    # ⚠️ NO incluye password ni hashed_password — nunca se devuelven
```

### Schema de Token (`schemas/token.py`)

```python
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
```

### ¿Por qué varios schemas por entidad?

Cada operación necesita datos diferentes:

```
CREATE (POST):  El usuario envía nombre, precio, etc. (NO envía id)
READ (GET):     La API devuelve id + nombre + precio, etc. (SÍ incluye id)
```

Por eso existen schemas separados: `XxxCreate` (entrada) y `XxxResponse` (salida).

### `orm_mode` / `from_attributes` — ¿Qué es?

SQLAlchemy devuelve **objetos** (con `.nombre`, `.precio`), no diccionarios. Pydantic por defecto lee diccionarios. Esta configuración le dice a Pydantic que lea **atributos** del objeto:

```python
class Config:
    from_attributes = True  # Pydantic v2
    # orm_mode = True       # Pydantic v1
```

> 📝 **Regla:** Todo schema que devuelva datos de la BD necesita `orm_mode = True` o `from_attributes = True`.

### `response_model` — Filtrando las respuestas

En los endpoints, `response_model` controla qué campos se devuelven:

```python
@router.post("/usuarios", response_model=schemas.UsuarioResponse)
```

Aunque el modelo tenga `hashed_password`, si `UsuarioResponse` no lo incluye, **nunca se envía al usuario**. Actúa como un filtro de seguridad.

---

## 🔧 Operaciones CRUD

Las funciones CRUD viven en `crud/` y son las únicas que interactúan directamente con la BD. Los endpoints **nunca** tocan la BD directamente.

### CRUD de Producto (`crud/producto.py`)

```python
from sqlalchemy.orm import Session
from schemas import ProductoCreate
from models import Producto

def obtener_productos(db: Session):
    return db.query(Producto).all()

def crear_producto(db: Session, producto: ProductoCreate):
    nuevo = Producto(
        nombre=producto.nombre,
        precio=producto.precio,
        en_stock=producto.en_stock,
        categoria_id=producto.categoria_id
    )
    db.add(nuevo)       # Pone en "sala de espera"
    db.commit()         # Ejecuta el INSERT real
    db.refresh(nuevo)   # Obtiene el id auto-generado
    return nuevo

def actualizar_producto(db: Session, producto_id: int, datos: ProductoCreate):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not producto:
        return None
    producto.nombre = datos.nombre
    producto.precio = datos.precio
    producto.en_stock = datos.en_stock
    producto.categoria_id = datos.categoria_id
    db.commit()
    db.refresh(producto)
    return producto

def eliminar_producto(db: Session, producto_id: int):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not producto:
        return None
    db.delete(producto)
    db.commit()
    return producto
```

### CRUD de Categoría (`crud/categoria.py`)

```python
def crear_categoria(db: Session, categoria: CategoriaCreate):
    db_categoria = Categoria(nombre=categoria.nombre)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def obtener_categorias(db: Session):
    return db.query(Categoria).all()
```

### CRUD de Usuario (`crud/usuario.py`)

```python
from sqlalchemy import or_
from core.security import hash_password

def obtener_usuario_por_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()

def obtener_usuario_por_id(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def crear_usuario(db: Session, usuario: UsuarioCreate):
    # Verifica que no exista duplicado por email O por nombre
    existe = db.query(Usuario).filter(
        or_(
            Usuario.email == usuario.email,
            Usuario.nombre == usuario.nombre
        )
    ).first()
    if existe:
        raise ValueError("Ya existe un usuario con ese email o nombre")

    db_usuario = Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        hashed_password=hash_password(usuario.password),  # Se hashea aquí
        es_admin=usuario.es_admin
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario
```

> 💡 `or_()` genera un `WHERE ... OR ...` en SQL. Sin él, `.filter()` combina condiciones con `AND`.

### Referencia rápida: ORM vs SQL

| Operación       | ORM (Python)                                      | SQL equivalente                      |
|-----------------|---------------------------------------------------|--------------------------------------|
| Listar todos    | `db.query(Producto).all()`                        | `SELECT * FROM productos`            |
| Buscar por ID   | `db.query(Producto).filter(Producto.id == 1).first()` | `SELECT * FROM productos WHERE id=1 LIMIT 1` |
| Insertar        | `db.add(nuevo)` + `db.commit()`                   | `INSERT INTO productos (...) VALUES (...)` |
| Actualizar      | Modificar atributos + `db.commit()`               | `UPDATE productos SET ... WHERE id=?` |
| Eliminar        | `db.delete(obj)` + `db.commit()`                  | `DELETE FROM productos WHERE id=?`   |

### Re-exportación con `__init__.py`

`crud/__init__.py` permite importar todas las funciones directamente:

```python
from .categoria import *
from .producto import *
from .usuario import *
```

Así puedes hacer `import crud` y luego `crud.crear_producto(...)`.

---

## 🔐 Seguridad y Autenticación

Todo el sistema de seguridad vive en `core/security.py`. Las claves sensibles se cargan desde variables de entorno.

### Hashing de contraseñas (bcrypt)

```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str):
    return pwd_context.verify(password, hashed)
```

| Función               | ¿Cuándo se usa?              | Ejemplo                                   |
|-----------------------|------------------------------|-------------------------------------------|
| `hash_password()`     | Al **registrar** un usuario  | `"MiClave123"` → `"$2b$12$xKj8fG..."`    |
| `verify_password()`   | Al hacer **login**           | Compara contraseña ingresada vs hash guardado |

> ⚠️ `verify_password` **no desencripta** el hash. Hashea la contraseña ingresada y compara los resultados. El hash es **irreversible**.

### Tokens JWT

```python
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from core.config import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

def crear_token(sub: str, es_admin: bool):
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data = {"sub": sub, "exp": expire, "es_admin": es_admin}
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
```

| Función             | ¿Cuándo se usa?               | Resultado                                  |
|---------------------|-------------------------------|---------------------------------------------|
| `crear_token()`     | Después de un login exitoso   | Genera un token JWT firmado                 |
| `verificar_token()` | En cada petición protegida    | Devuelve el payload o `None` si es inválido |

Un JWT tiene 3 partes: **Header** (algoritmo), **Payload** (datos + expiración) y **Firma** (verificación).

### Flujo completo de autenticación

```
1. REGISTRO  →  hash_password(password)  →  Se guarda hash en BD
2. LOGIN     →  verify_password(password, hash_guardado)
              →  Si coincide: crear_token(email, es_admin)  →  Devuelve token
3. RUTA PROTEGIDA  →  verificar_token(token)  →  Si válido: permite acceso
```

---

## 🗂 Sistema de Rutas con APIRouter

`APIRouter` permite dividir los endpoints en **múltiples archivos organizados por funcionalidad**, en vez de poner todo en `main.py`.

### Punto de entrada (`main.py`)

```python
from fastapi import FastAPI
from api.api_v1.api import api_router

app = FastAPI()
app.include_router(api_router, prefix="api/v1")
```

### Router principal (`api/api_v1/api.py`)

Agrupa todos los sub-routers bajo un mismo router:

```python
from fastapi import APIRouter
from api.api_v1 import auth, productos, categorias

api_router = APIRouter()

api_router.include_router(router=auth.api_router, prefix="/auth", tags=["auth"])
api_router.include_router(router=productos.api_router, prefix="/productos", tags=["productos"])
api_router.include_router(router=categorias.api_router, prefix="/categorias", tags=["categorias"])
```

### Cómo se construyen las URLs finales

El prefijo de `main.py` + el prefijo de `api.py` + la ruta del endpoint:

```
main.py prefix    api.py prefix     endpoint path     URL final
"api/v1"       + "/auth"         + "/login"         = api/v1/auth/login
"api/v1"       + "/productos"    + "/productos"     = api/v1/productos/productos
"api/v1"       + "/categorias"   + "/categorias"    = api/v1/categorias/categorias
```

Los **tags** agrupan visualmente los endpoints en la documentación Swagger.

---

## 🔗 Dependencias

Las dependencias viven en `deps/deps.py`. Se inyectan con `Depends()` en los endpoints.

### Sesión de Base de Datos (`get_db`)

```python
from db.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

`yield` (en vez de `return`) garantiza que la conexión se cierre **siempre**, incluso si hay errores.

### Autenticación (`get_current_user`)

```python
from fastapi.security import OAuth2PasswordBearer
from core.security import verificar_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    cred_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No autenticado",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = verificar_token(token)
        email = payload.get("sub")
        if email is None:
            raise cred_exc
    except JWTError:
        raise cred_exc

    user = crud.obtener_usuario_por_email(db, email)
    if user is None:
        raise cred_exc
    return user
```

`OAuth2PasswordBearer` le dice a FastAPI que espere un token en el header `Authorization: Bearer <token>`.

### Permisos de Admin (`requiere_admin`)

```python
def requiere_admin(current_user = Depends(get_current_user)):
    if not current_user.es_admin:
        raise HTTPException(status_code=403, detail="No autorizado, requiere admin")
```

Se usa como dependencia para endpoints que solo admins pueden ejecutar.

---

## 🌐 Endpoints de la API

### Auth (`api/api_v1/auth.py`)

| Método | Ruta                       | Descripción                    | Protegido         |
|--------|----------------------------|--------------------------------|-------------------|
| POST   | `/auth/usuarios`           | Registrar un nuevo usuario     | No                |
| POST   | `/auth/login`              | Login (devuelve JWT)           | No                |
| GET    | `/auth/usuarios/me`        | Ver perfil del usuario actual  | Sí (token)        |
| GET    | `/auth/admin/ping`         | Verificar permisos de admin    | Sí (solo admins)  |

### Productos (`api/api_v1/productos.py`)

| Método | Ruta                       | Descripción                    | Protegido         |
|--------|----------------------------|--------------------------------|-------------------|
| GET    | `/productos/productos`     | Listar todos los productos     | No                |
| POST   | `/productos/productos`     | Crear un producto              | Sí (solo admins)  |
| PUT    | `/productos/productos/{id}`| Actualizar un producto         | No                |
| DELETE | `/productos/productos/{id}`| Eliminar un producto           | No                |

### Categorías (`api/api_v1/categorias.py`)

| Método | Ruta                           | Descripción                  | Protegido |
|--------|--------------------------------|------------------------------|-----------|
| POST   | `/categorias/categorias`       | Crear una categoría          | No        |
| GET    | `/categorias/categorias`       | Listar todas las categorías  | No        |

> 📝 Todas las rutas llevan el prefijo `api/v1/` definido en `main.py`.

---

## 📚 Recursos Útiles

| Recurso                            | Enlace                                                                          |
|------------------------------------|---------------------------------------------------------------------------------|
| Documentación oficial de FastAPI   | [fastapi.tiangolo.com](https://fastapi.tiangolo.com)                            |
| Tutorial interactivo de FastAPI    | [fastapi.tiangolo.com/tutorial](https://fastapi.tiangolo.com/tutorial/)         |
| FastAPI + SQL Databases            | [fastapi.tiangolo.com/tutorial/sql-databases](https://fastapi.tiangolo.com/tutorial/sql-databases/) |
| Documentación de Pydantic          | [docs.pydantic.dev](https://docs.pydantic.dev/)                                |
| Documentación de SQLAlchemy        | [docs.sqlalchemy.org](https://docs.sqlalchemy.org/)                             |
| Documentación de Uvicorn           | [uvicorn.org](https://www.uvicorn.org/)                                         |
| Documentación de python-jose (JWT) | [python-jose.readthedocs.io](https://python-jose.readthedocs.io/)              |
| Documentación de passlib           | [passlib.readthedocs.io](https://passlib.readthedocs.io/)                      |

---

> 🚧 *Este README se actualizará a medida que avance el proyecto.*


MIGRACIONES, EVITAR PERDER DATOS AL AGREGAR UNA NUEVA COLUMNA, USAREMOS, alembic init alembic Contiene los scripts de migracion
alembic revision --autogenerate -m "crear tablas iniciales" HACE EL CAMBIO