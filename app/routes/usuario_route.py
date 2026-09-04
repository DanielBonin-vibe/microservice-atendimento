from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from services import usuario_service


router = APIRouter(
    prefix='/usuarios',
    tags=['Usuários)']
)

class Usuario(BaseModel):
    nome: str = Field(min_length=3, max_length=100)
    cpf_usuario = str = Field(min_length=14, max_length=14)
    email: str = Field(min_length=5, max_length=100)
    telefone: str = Field(min_length=10, max_length=15)

@router.post('/', status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario: Usuario):
    resultado = usuario_service.cadastro_usuario_service(
        usuario.nome, usuario.cpf_usuario, usuario.email, usuario.telefone)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado