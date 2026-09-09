from pydantic import BaseModel, Field, EmailStr

class UsuarioCriacao(BaseModel):
    nome: str = Field(min_length=3, max_length=100)
    cpf_usuario: str = Field(min_length=14, max_length=14)
    email: EmailStr
    telefone: str = Field(min_length=10, max_length=15)
    senha: str = Field(min_length=8, max_length=100)

class UsuarioAtualizacao(BaseModel):
    nome: str | None = Field(default=None, min_length=3, max_length=100)
    cpf_usuario_novo: str | None = Field(default=None, min_length=14, max_length=14)
    email: EmailStr | None = None
    telefone: str | None = Field(default=None, min_length=10, max_length=15)
    senha: str | None = Field(default=None, min_length=8, max_length=100)


class AlterarSenhaUsuario(BaseModel):
    senha_atual: str = Field(min_length=8, max_length=100)
    senha_nova: str = Field(min_length=8, max_length=100)