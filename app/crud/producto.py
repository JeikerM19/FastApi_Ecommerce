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
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
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
