from pydantic import BaseModel, Field, EmailStr

class TecnicoCriacao(BaseModel):
    id_grupo_tecnico: int = Field(gt=0)
    nome: str = Field(min_length=3, max_length=100)
    cpf_tecnico: str = Field(min_length=14, max_length=14)
    email: EmailStr

class TecnicoAtualizacao(BaseModel):
    nome: str | None = Field(default=None ,min_length=3, max_length=100)
    cpf_tecnico: str | None = Field(default=None, min_length=14, max_length=14)
    email: EmailStr | None = None