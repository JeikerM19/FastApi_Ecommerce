from fastapi import APIRouter
from api.api_v1 import auth, productos, categorias, carrito, pedido
api_router = APIRouter()

api_router.include_router(router=auth.api_router, prefix="/auth", tags=["auth"])
api_router.include_router(router=productos.api_router, prefix="/productos", tags=["productos"])
api_router.include_router(router=categorias.api_router, prefix="/categorias", tags=["categorias"])
api_router.include_router(router=carrito.api_router, prefix="/carrito", tags=["carritos"])
api_router.include_router(router=pedido.api_router, prefix="/pedido", tags=["pedidos"])
