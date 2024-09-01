# Use uma imagem base com Python 3.9 (ou outra versão que preferir)
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o requirements.txt e instala as dependências
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação para dentro do container
COPY . .

# Copia o arquivo .env para o container e garante que ele seja lido pelo FastAPI
COPY .env .env

# Expõe a porta que a aplicação irá rodar
EXPOSE 8080

# Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
