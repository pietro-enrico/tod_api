# Responsabilidade única: criar o app, registrar configurações e incluir as rotas.


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes import router

# Cria a instância principal do FastAPI.
# É aqui que o uvicorn aponta quando você roda: uvicorn app.main:app
app = FastAPI(title="Tod-API", description="API de tarefas com FastAPI")


app.mount("/static", StaticFiles(directory="static"), name="static")

# Registra todas as rotas definidas no routes.py.
# O include_router conecta o APIRouter ao app principal.
app.include_router(router)
