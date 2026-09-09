from pydantic import BaseModel, Field

class ChamadoCriacao(BaseModel):
    cpf_usuario: str = Field(min_length=14, max_length=14)
    nome_grupo: str = Field(min_length=3, max_length=100)
    titulo: str = Field(min_length=3, max_length=100)
    descricao: str = Field(min_length=3, max_length=500)
    prioridade: str = Field(min_length=3, max_length=10)

class ChamadoAtualizacao(BaseModel):
    titulo: str | None = Field(default=None, min_length=3, max_length=100)
    descricao: str | None = Field(default=None, min_length=3, max_length=500)
    status: str | None = Field(default=None, min_length=3, max_length=100)
    prioridade: str | None = Field(default=None, min_length=3, max_length=100)