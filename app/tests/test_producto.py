from fastapi.testclient import TestClient
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

client = TestClient(app)
token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbkBnbWFpbC5jb20iLCJleHAiOjE3NzQzOTk3MDYsImVzX2FkbWluIjp0cnVlfQ.uYFba_Nokp2QhdjjYpACK6sz0Ox1f4oeUKCbcgkxCYM"

def test_crear_producto_exitoso():
    data = {
        "nombre":"Producto prueba",
        "precio":20,
        "en_stock":True,
        "stock":300,
        "categoria_id":1
    }
    headers = {
        "Authorization": token
    }
    response = client.post('/api/v1/productos/productos', json=data, headers=headers)
    
    assert response.status_code == 200
    assert response.json()["nombre"] == data["nombre"]
    assert response.json()["precio"] == data["precio"]

def test_crear_producto_faltante_nombre():
    data = {
        "precio":20,
        "en_stock":True,
        "stock":300,
        "categoria_id":1
    }
    headers = {
        "Authorization": token
    }
    response = client.post('/api/v1/productos/productos', json=data, headers=headers)
    
    assert response.status_code == 422
    assert "nombre" in response.text
def test_listar_productos():
    response = client.get("/api/v1/productos/productos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)