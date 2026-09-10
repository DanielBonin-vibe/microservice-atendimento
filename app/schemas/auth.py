from pydantic import BaseModel, Field

class Login(BaseModel):
    cpf: str = Field(min_length=14, max_length=14)
    senha: str = Field(min_length=1, max_length=100)