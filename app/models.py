# O Pydantic valida automaticamente se os dados recebidos estão corretos.


from pydantic import BaseModel

# BaseModel é a classe base do Pydantic.
# Toda classe que herdar dela ganha validação automática de tipos.
class Task(BaseModel):
    title: str               
    description: str | None  
    done: bool = False      
