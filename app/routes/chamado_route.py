from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from services import chamado_service

router = APIRouter(
    prefix='/chamado',
    tags=['Chamados']
)

class Chamado(BaseModel):
    cpf_usuario: str = Field(min_length=14, max_length=14)
    nome_grupo: str = Field(min_length=3, max_length=100)
    titulo: str = Field(min_length=3, max_length=100)
    descricao: str = Field(min_length=3, max_length=500)
    prioridade: str = Field(min_length=3, max_length=10)

class AtualizarChamado(BaseModel):
    titulo: str | None = Field(default=None, min_length=3, max_length=100)
    descricao: str | None = Field(default=None, min_length=3, max_length=500)
    status: str | None = Field(default=None, min_length=3, max_length=100)
    prioridade: str | None = Field(default=None, min_length=3, max_length=100)

@router.post('/', status_code=status.HTTP_201_CREATED)
def criar_chamado(chamado: Chamado):
    resultado = chamado_service.criar_chamado_service(chamado.cpf_usuario, chamado.nome_grupo, chamado.titulo, chamado.descricao, chamado.prioridade)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.get('/', status_code=status.HTTP_200_OK)
def listar_chamados():
    resultado = chamado_service.listar_chamados_service()

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/buscar', status_code=status.HTTP_200_OK)
def buscar_chamado(id_chamado: str | None = None, titulo: str | None = None):
    resultado = chamado_service.buscar_chamado_service(id_chamado, titulo)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )
    
    return resultado

@router.get('/pesquisar', status_code=status.HTTP_200_OK)
def pesquisar_chamados(id_usuario: int | None = None, id_tecnico: int | None = None, id_grupo_tecnico: int | None = None, titulo: str | None = None, descricao: str | None = None, status: str | None = None, prioridade: str | None = None):
    resultado = chamado_service.pesquisar_chamados_service(id_usuario, id_tecnico, id_grupo_tecnico, titulo, descricao, status, prioridade)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.put('/atualizar/{id_chamado}', status_code=status.HTTP_200_OK)
def atualizar_info_chamado(id_chamado: int, chamado: AtualizarChamado):
    resultado = chamado_service.atualizar_info_chamado_service(id_chamado, chamado.titulo, chamado.descricao, chamado.status, chamado.prioridade)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.put('/atribuir_tecnico/{id_chamado}', status_code=status.HTTP_200_OK)
def atribuir_tecnico(id_chamado: int, nome: str):
    resultado = chamado_service.atribuir_tecnico_service(id_chamado, nome)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado 

@router.put('/alterar_grupo_tecnico/{id_chamado}', status_code=status.HTTP_200_OK)
def alterar_grupo_tecnico(id_chamado: int, id_novo_grupo: int):
    resultado = chamado_service.alterar_grupo_tecnico_service(id_chamado, id_novo_grupo)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.put('/alterar_status_chamado/{id_chamado}', status_code=status.HTTP_200_OK)
def alterar_status_chamado(id_chamado: int, novo_status: str):
    resultado = chamado_service.alterar_status_chamado_service(id_chamado, novo_status)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.put('/alterar_prioridade_chamado/{id_chamado}', status_code=status.HTTP_200_OK)
def alterar_prioridade_chamado(id_chamado: int, nova_prioridade: str):
    resultado = chamado_service.alterar_prioridade_chamado_service(id_chamado, nova_prioridade)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.put('/solucionar_chamado/{id_chamado}', status_code=status.HTTP_200_OK)
def solucionar_chamado(id_chamado: int, motivo_solucao: str):
    resultado = chamado_service.solucionar_chamado_service(id_chamado, motivo_solucao)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.put('/reabrir_chamado/{id_chamado}', status_code=status.HTTP_200_OK)
def reabrir_chamado(id_chamado: int, motivo_reabrir: str):
    resultado = chamado_service.reabrir_chamado_service(id_chamado, motivo_reabrir)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

