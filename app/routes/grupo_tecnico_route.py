from fastapi import APIRouter, HTTPException, status
from app.services import grupo_tecnico_service
from app.schemas.grupo_tecnico import GrupoTecnicoCriacao, GrupoTecnicoAtualizacao

router = APIRouter(
    prefix = '/grupo_tecnico',
    tags=['Grupos Técnicos']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def criar_grupo_tecnico(grupo: GrupoTecnicoCriacao):
    resultado = grupo_tecnico_service.criar_grupo_tecnico(grupo.nome, grupo.descricao)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.get('/', status_code=status.HTTP_200_OK)
def listar_grupos_tecnicos():
    resultado = grupo_tecnico_service.listar_grupos_tecnicos()

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/buscar/{nome}', status_code=status.HTTP_200_OK)
def buscar_grupo_tecnico(nome: str):
    resultado = grupo_tecnico_service.buscar_grupo_tecnico(nome)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/pesquisar/', status_code=status.HTTP_200_OK)
def pesquisar_grupos_tecnicos(nome: str | None = None, descricao: str | None = None):
    resultado = grupo_tecnico_service.pesquisar_grupos_tecnicos(nome, descricao)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.put('/{nome_inicial}', status_code=status.HTTP_200_OK)
def atualizar_grupo_tecnico(nome_inicial: str, grupo: GrupoTecnicoAtualizacao):
    resultado = grupo_tecnico_service.atualizar_grupo_tecnico(nome_inicial, grupo.nome_novo, grupo.descricao)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.delete('/{nome}', status_code=status.HTTP_200_OK)
def excluir_grupo_tecnico(nome: str):
    resultado = grupo_tecnico_service.excluir_grupo_tecnico(nome)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado