from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from services import usuario_service


router = APIRouter(
    prefix='/usuarios',
    tags=['Usuários']
)

class Usuario(BaseModel):
    nome: str = Field(min_length=3, max_length=100)
    cpf_usuario: str = Field(min_length=14, max_length=14)
    email: str = Field(min_length=5, max_length=100)
    telefone: str = Field(min_length=10, max_length=15)

class UsuarioAtualizacao(BaseModel):
    nome: str | None = Field(default=None, min_length=3, max_length=100)
    cpf_usuario_novo: str | None = Field(default=None, min_length=14, max_length=14)
    email: str | None = Field(default=None, min_length=5, max_length=100)
    telefone: str | None = Field(default=None, min_length=10, max_length=15)

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

@router.get('/', status_code=status.HTTP_200_OK)
def listar_usuario():
    resultado = usuario_service.listar_usuario_service()

    if isinstance(resultado, str):
        raise HTTPException (
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/buscar/{busca}', status_code=status.HTTP_200_OK)
def buscar_usuario(busca):
    resultado = usuario_service.buscar_usuario_service(busca)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/pesquisar', status_code=status.HTTP_200_OK)
def pesquisar_usuarios(nome: str | None = None, cpf_usuario: str | None = None, email: str | None = None, telefone: str | None = None):

    resultado = usuario_service.pesquisar_usuarios_service(nome, cpf_usuario, email, telefone)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado 

@router.put('/{cpf_usuario_inicial}', status_code=status.HTTP_200_OK)
def atualizar_usuario(cpf_usuario_inicial: str, usuario: UsuarioAtualizacao):
    resultado = usuario_service.atualizar_usuario_service(
        cpf_usuario_inicial,
        usuario.nome,
        usuario.cpf_usuario_novo,
        usuario.email,
        usuario.telefone
    )

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.delete('/{cpf_usuario}', status_code=status.HTTP_200_OK)
def excluir_usuario(cpf_usuario: str):
    resultado = usuario_service.excluir_usuario_service(cpf_usuario)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado