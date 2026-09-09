from fastapi import APIRouter, HTTPException, status
from app.services import tecnico_service
from app.schemas.usuario import TecnicoCriacao, TecnicoAtualizacao

router = APIRouter(
    prefix='/tecnico',
    tags=['Técnicos']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def criar_tecnico(tecnico: TecnicoCriacao):
    resultado = tecnico_service.criar_tecnico_service(tecnico.id_grupo_tecnico, tecnico.nome, tecnico.cpf_tecnico, tecnico.email)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.get('/', status_code=status.HTTP_200_OK)
def listar_tecnicos():
    resultado = tecnico_service.listar_tecnicos_service()

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/buscar/{cpf_tecnico}', status_code=status.HTTP_200_OK)
def buscar_tecnico(cpf_tecnico: str):
    resultado = tecnico_service.buscar_tecnico_service(cpf_tecnico)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/pesquisar', status_code=status.HTTP_200_OK)
def pesquisar_tecnicos(nome: str | None = None, id_grupo_tecnico: int | None = None):
    resultado = tecnico_service.pesquisar_tecnicos_service(nome, id_grupo_tecnico)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.put('/atualizar/{cpf_tecnico_inicial}', status_code=status.HTTP_200_OK)
def atualizar_tecnico(cpf_tecnico_inicial: str, tecnico: TecnicoAtualizacao):
    resultado = tecnico_service.atualizar_tecnico_service(tecnico.cpf_tecnico_inicial, tecnico.nome, tecnico.cpf_tecnico, tecnico.email)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.delete('/{cpf_tecnico}', status_code=status.HTTP_200_OK)
def excluir_tecnico(cpf_tecnico: str):
    resultado = tecnico_service.excluir_tecnico_service(cpf_tecnico)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado
