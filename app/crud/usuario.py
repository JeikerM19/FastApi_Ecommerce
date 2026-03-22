from sqlalchemy.orm import Session
from schemas import UsuarioCreate
from models import Usuario
from core.security import hash_password
from sqlalchemy import or_

def obtener_usuario_por_email(db:Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()

def obtener_usuario_por_id(db:Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def crear_usuario(db:Session, usuario:UsuarioCreate):
    existe = db.query(Usuario).filter(
        or_(
            Usuario.email == usuario.email, 
            Usuario.nombre == usuario.nombre
            )
    ).first()
    if existe:
        raise ValueError("Ya existe un usuario con ese email o nombre")
    
    db_usuario = Usuario(
        nombre = usuario.nombre,
        email = usuario.email,
        hashed_password = hash_password(usuario.password),
        es_admin = usuario.es_admin
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario