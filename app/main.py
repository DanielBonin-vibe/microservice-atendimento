from fastapi import FastAPI
from app.routes import usuario_route, tecnico_route, grupo_tecnico_route, chamado_route, auth_route

app = FastAPI(
    title='API de Atendimento',
    version='1.0.0'
    )

app.include_router(usuario_route.router)
app.include_router(grupo_tecnico_route.router)
app.include_router(tecnico_route.router)
app.include_router(chamado_route.router)
app.include_router(auth_route.router)

@app.get('/')
def inicio():
    return {
        'mensagem': 'API do Sistema de Atendimento funcionando.'
    }