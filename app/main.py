from fastapi import FastAPI
from api.api_v1.api import api_router

app = FastAPI(
    title="E-commercer API",
    description= """
        Api RESTful completa para la gestion de un E-commerce
        
        Incluye:
        - Autenteticacion con Jwt
        - Administracion de productos y categorias
        - Carrito de compras
        - Gestion de pedidos
    """,
    version="1.0.0",
    contact={
        "name":"Jeiker Dev - Equipo Backend",
        "url":"https://github.com/JeikerM19/FastApi_Ecommerce",
        "email":"contacto@gmail.com"
    }
)


app.include_router(api_router, prefix="/api/v1")


