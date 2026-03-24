from sqlalchemy.orm import Session
from models import Producto
from models.pedidos import Carrito, DetallePedido, Pedido


def crear_pedido(db: Session, usuario_id: int):
    carrito = db.query(Carrito).filter_by(usuario_id=usuario_id).first()

    if not carrito or not carrito.items:
        raise ValueError("El carrito esta vacio")

    total = 0
    pedido = Pedido(usuario_id=usuario_id, total=0)
    db.add(pedido)
    db.commit()
    db.refresh(pedido)

    for item in carrito.items:
        producto = db.get(Producto, item.producto_id)

        # Saltar si no hay stock o el precio es inválido
        if not producto.stock or producto.precio <= 0:
            continue

        if 0 < item.cantidad <= producto.stock:
            subtotal = producto.precio * item.cantidad
            producto.stock -= item.cantidad
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

    # Eliminar items y el carrito vacío tras la compra
    for item in carrito.items:
        db.delete(item)
    db.delete(carrito)
    db.commit()

    return pedido