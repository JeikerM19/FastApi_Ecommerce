from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas
from deps.deps import get_db

api_router = APIRouter()


@api_router.post("/categorias", response_model=schemas.CategoriaResponse)
def crear_categoria(categoria:schemas.CategoriaCreate, db: Session = Depends(get_db)):
    return crud.crear_categoria(db, categoria)

@api_router.get("/categorias",response_model=list[schemas.CategoriaResponse])
def listar_categorias(db: Session = Depends(get_db)):
    return crud.obtener_categorias(db)
