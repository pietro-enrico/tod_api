# storage.py
# Responsável por toda a comunicação com o arquivo JSON.
# Isola a lógica de persistência do restante da aplicação.


import json
import os

# Caminho do arquivo onde as tarefas são armazenadas
DATA_FILE = os.path.join("dados", "task.json")


def read_tasks() -> list:
    # Verifica se o arquivo existe antes de tentar abrir.
    # Retorna lista vazia se o arquivo ainda não foi criado.
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)  # lê o JSON e converte para lista Python


def save_tasks(tasks: list) -> None:
    # Sobrescreve o arquivo com a lista atualizada.
    # indent=2 formata o JSON com indentação para ficar legível.
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=2)
