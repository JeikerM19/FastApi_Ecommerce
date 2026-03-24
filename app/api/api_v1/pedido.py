from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud
from deps.deps import get_db, get_current_user

api_router = APIRouter()

@api_router.post("/confirmar",summary="Confirmar producto", response_description="Pedido creado correctamente")
def confirmar_pedido(db:Session = Depends(get_db), user = Depends(get_current_user)):
    try:
        pedido = crud.crear_pedido(db, user.id)
        return {
            "mensaje":"Pedido generado",
            "pedido_id":pedido.id,
            "total": pedido.total
            }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
