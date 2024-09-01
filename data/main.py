# main.py
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from orquestradorController import router as orquestrador_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite apenas o frontend React
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Registrando o router da OrquestradorController
app.include_router(orquestrador_router, prefix="/orquestrador")

if __name__ == "__main__":
    import uvicorn
    print("Executando...")
    uvicorn.run(app, host="0.0.0.0", port=8080)
