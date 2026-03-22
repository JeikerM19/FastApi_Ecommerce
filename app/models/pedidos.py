from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime

class Carrito(Base):
    __tablename__="carritos"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    usuario = relationship("Usuario", back_populates="carrito", cascade="all, delete")

class ItemCarrito(Base):
    __tablename__ = "items_carrito"
    id = Column(Integer, primary_key=True,index=True)
    carrito_id = Column(Integer, ForeignKey("carritos.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer,default=1)
    carrito = relationship("Carrito", back_populates="items")
    producto = relationship("Producto")
    
class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True,index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    fecha = Column(DateTime, default=datetime.now)
    total = Column(Float)
    detalles = relationship("DetallePedido", back_populates="pedido")

class DetallePedido(Base):
    __tablename__ = "detalles_pedidos"
    id = Column(Integer, primary_key=True,index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer)
    subtotal =Column(Float)
    pedido = relationship("Producto")
