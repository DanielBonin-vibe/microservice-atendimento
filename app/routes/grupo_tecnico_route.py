from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from services import grupo_tecnico_service

router = APIRouter(
    prefix = '/grupo_tecnico',
    tags=['Grupos Técnicos']
)

class GrupoTecnico(BaseModel):
    nome: str = Field(min_length=3, max_length=100)
    descricao: str = Field(min_lenght=3, max_lenght=500)

class GrupotecnicoAtualizacao(BaseModel):
    nome_novo: str | None = Field(default=None, min_length=3, max_length=100)
    descricao: str | None = Field(default=None, min_length=3, max_length=500)

@router.post('/', status_code=status.HTTP_201_CREATED)
def criar_grupo_tecnico(grupo: GrupoTecnico):
    resultado = grupo_tecnico_service.criar_grupo_tecnico_service(grupo.nome, grupo.descricao)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.get('/', status_code=status.HTTP_200_OK)
def listar_grupos_tecnicos():
    resultado = grupo_tecnico_service.listar_grupos_tecnicos_service()

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/buscar/{nome}', status_code=status.HTTP_200_OK)
def buscar_grupo_tecnico(nome: str):
    resultado = grupo_tecnico_service.buscar_grupo_tecnico_service(nome)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/pesquisar/', status_code=status.HTTP_200_OK)
def pesquisar_grupos_tecnicos(nome: str | None = None, descricao: str | None = None):
    resultado = grupo_tecnico_service.pesquisar_grupos_tecnicos_service(nome, descricao)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.put('/{nome_inicial}', status_code=status.HTTP_200_OK)
def atualizar_grupo_tecnico(nome_inicial: str, grupo: GrupotecnicoAtualizacao):
    resultado = grupo_tecnico_service.atualizar_grupo_tecnico_service(nome_inicial, grupo.nome_novo, grupo.descricao)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.delete('/{nome}', status_code=status.HTTP_200_OK)
def excluir_grupo_tecnico(nome):
    resultado = grupo_tecnico_service.excluir_grupo_tecnico_service(nome)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

