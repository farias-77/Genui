from fastapi import FastAPI
from app.controllers import insight_controller, open_finance_controller

app = FastAPI()

# Registrando os controladores
app.include_router(insight_controller.router)
app.include_router(open_finance_controller.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
