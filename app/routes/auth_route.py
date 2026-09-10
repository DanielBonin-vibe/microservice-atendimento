from fastapi import APIRouter, HTTPException, status
from app.services import auth_service
from app.schemas.auth import Login

router = APIRouter(
    prefix='/auth',
    tags=['Autenticação']
)

@router.post('/login', status_code=status.HTTP_200_OK)
def login(dados: Login):
    resultado = auth_service.login_service(dados.cpf, dados.senha)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=resultado
        )

    return resultado