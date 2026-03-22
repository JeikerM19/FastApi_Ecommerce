from pydantic import BaseModel, EmailStr

class UsuarioBase(BaseModel):
    nombre:str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    password: str
    es_admin: bool = False
    
class UsuarioResponse(UsuarioBase):
    id: int
    es_admin:bool
    
    class Config:
        from_attributes = True
        
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"