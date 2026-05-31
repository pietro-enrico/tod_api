# Tod-API

API REST de tarefas (to-do list) construída com **FastAPI**, com interface web simples em HTML/CSS e persistência em arquivo JSON. Totalmente containerizada com **Docker**.

---

## Funcionalidades

- Criar, listar, editar, concluir e deletar tarefas
- Interface web com formulário de entrada
- Separação visual entre tarefas pendentes e concluídas
- Contador de tarefas concluídas
- Persistência dos dados em arquivo JSON

---

## Tecnologias

- **Python 3.12**
- **FastAPI** — framework web
- **Uvicorn** — servidor ASGI
- **Pydantic** — validação de dados
- **Jinja2** — motor de templates HTML
- **Docker** + **Docker Compose** — containerização

---

## Estrutura do projeto

```
tod-api/
├── app/
│   ├── __init__.py
│   ├── main.py        # Ponto de entrada: cria o app e registra rotas
│   ├── models.py      # Modelo Pydantic da tarefa
│   ├── storage.py     # Funções de leitura/escrita no JSON
│   └── routes.py      # Definição de todas as rotas
├── dados/
│   └── task.json      # Armazenamento das tarefas
├── static/
│   └── style.css      # Estilização da interface
├── templates/
│   ├── index.html     # Página principal
│   └── edit.html      # Formulário de edição de tarefa
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## Como rodar

### Opção 1 — Docker (recomendado)

```bash
docker compose up --build
```

Acesse `http://localhost:8000`.

### Opção 2 — Localmente sem Docker

```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

---

## Endpoints da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Página HTML com a lista de tarefas |
| GET | `/tasks` | Retorna todas as tarefas em JSON |
| POST | `/tasks` | Cria uma nova tarefa |
| GET | `/tasks/{id}/edit` | Exibe o formulário de edição |
| POST | `/tasks/{id}/edit` | Atualiza título e descrição da tarefa |
| GET | `/tasks/{id}/done` | Alterna o status de concluída |
| GET | `/tasks/{id}/delete` | Remove uma tarefa |
| GET | `/docs` | Documentação interativa (Swagger) |

