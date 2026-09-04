from fastapi import FastAPI
from routes import usuario_route, tecnico_route, grupo_tecnico_route, chamado_route

app = FastAPI(title='API de Atendimento')

app.incluide_router(usuario_route.router)