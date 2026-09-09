from pydantic import BaseModel, Field

class GrupoTecnicoCriacao(BaseModel):
    nome: str = Field(min_length=3, max_length=100)
    descricao: str = Field(min_lenght=3, max_lenght=500)

class GrupoTecnicoAtualizacao(BaseModel):
    nome_novo: str | None = Field(default=None, min_length=3, max_length=100)
    descricao: str | None = Field(default=None, min_length=3, max_length=500)