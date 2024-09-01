# main.py
import os
from fastapi import FastAPI
from orquestradorController import router as orquestrador_router

app = FastAPI()

# Registrando o router da OrquestradorController
app.include_router(orquestrador_router, prefix="/orquestrador")

if __name__ == "__main__":
    import uvicorn
    print("Executando...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
