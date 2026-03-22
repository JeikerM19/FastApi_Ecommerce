from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from deps.deps import requiere_admin, get_db

api_router = APIRouter()

@api_router.get("/productos", response_model=list[schemas.ProductoResponse])
def listar_productos(db:Session = Depends(get_db)):
    return crud.obtener_productos(db)

@api_router.post("/productos", response_model=schemas.ProductoCreate,dependencies=[Depends(requiere_admin)])
def agregar_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.crear_producto(db, producto)

@api_router.put("/productos/{id}", response_model=schemas.ProductoCreate)
def actualizar_producto(producto_id: int, datos: schemas.ProductoCreate, db: Session = Depends(get_db)):
    producto = crud.actualizar_producto(db, producto_id, datos)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@api_router.delete("/productos/{id}")
def eliminar_producto(producto_id: int, db:Session = Depends(get_db)):
    producto = crud.eliminar_producto(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje":"producto eliminado"}