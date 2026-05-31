# Imagem base com Python 3.12 já instalado.
# slim = versão enxuta sem pacotes desnecessários, deixa a imagem final menor.
FROM python:3.12-slim

# Define /app como pasta de trabalho dentro do container.
# Todos os comandos seguintes rodam a partir desta pasta.
WORKDIR /app

# Copia o requirements.txt antes do código fonte.
COPY requirements.txt .

# Instala as dependências Python dentro do container.
RUN pip install -r requirements.txt

# Copia o código fonte e os arquivos necessários para dentro do container.
COPY ./app ./app
COPY ./dados ./dados
COPY ./templates ./templates
COPY ./static ./static

EXPOSE 8000

# Comando executado quando o container inicia.
# --host 0.0.0.0 permite conexões de fora do container.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
