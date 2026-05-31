
# Define todas as rotas da aplicação.
# Cada rota é uma função que recebe uma requisição HTTP e retorna uma resposta.
# Usa APIRouter em vez de app diretamente — isso permite registrar as rotas no main.py de forma organizada.

import uuid
from fastapi import APIRouter, HTTPException, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from app.models import Task
from app.storage import read_tasks, save_tasks

# APIRouter é como um "mini app" — agrupa rotas relacionadas.
# No main.py vamos registrar esse router no app principal.
router = APIRouter()

# Jinja2Templates aponta para a pasta onde ficam os arquivos HTML.
templates = Jinja2Templates(directory="templates")


# --- ROTA PRINCIPAL ---

# Rota GET "/" — retorna a página HTML com todas as tarefas.
# response_class=HTMLResponse indica que a resposta é HTML, não JSON.
@router.get("/")
def home(request: Request):
    tasks = read_tasks()
    # TemplateResponse renderiza o index.html passando as tarefas como variável.
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"tasks": tasks}
    )


# --- ROTAS DA API ---

# Rota GET "/tasks" — retorna todas as tarefas em formato JSON.
# Útil para consumir a API de outros sistemas ou do Swagger.
@router.get("/tasks")
def get_tasks():
    return read_tasks()


# Rota POST "/tasks" — cria uma nova tarefa via formulário HTML.
# Form(...) indica que os dados vêm de um formulário, não de um JSON.
@router.post("/tasks")
def create_task(
    title: str = Form(...),
    description: str = Form(None)  # None = opcional
):
    tasks = read_tasks()

    # Monta o dicionário da nova tarefa com um ID único gerado pelo uuid4.
    new_task = {
        "id": str(uuid.uuid4()),  
        "title": title,
        "description": description,
        "done": False            
    }

    tasks.append(new_task)
    save_tasks(tasks)

    # Redireciona para a página inicial após salvar.
    # status_code=303 é o código HTTP correto para redirecionamento após POST.
    return RedirectResponse(url="/", status_code=303)


# Rota GET "/tasks/{task_id}/done" — alterna o status de concluído da tarefa.
# {task_id} é um parâmetro dinâmico capturado da URL.
@router.get("/tasks/{task_id}/done")
def toggle_done(task_id: str):
    tasks = read_tasks()

    for task in tasks:
        if task["id"] == task_id:
            # not inverte o valor: True vira False, False vira True
            task["done"] = not task["done"]

    save_tasks(tasks)
    return RedirectResponse(url="/", status_code=303)


# Rota GET "/tasks/{task_id}/delete" — remove uma tarefa pelo ID.
@router.get("/tasks/{task_id}/delete")
def delete_task(task_id: str):
    tasks = read_tasks()

    # List comprehension: cria uma nova lista sem a tarefa com o ID informado.
    updated = [task for task in tasks if task["id"] != task_id]

    save_tasks(updated)
    return RedirectResponse(url="/", status_code=303)
