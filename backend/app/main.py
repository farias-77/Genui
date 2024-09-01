from fastapi import FastAPI
from app.routers.corporate_purchase import router as corporate_purchase_router
from app.routers.transaction import router as transaction_router
from app.routers.transfer import router as transfer_router
from app.routers.invoice import router as invoice_router

app = FastAPI()

# Incluindo os routers para cada tipo de dado
app.include_router(corporate_purchase_router)
app.include_router(transaction_router)
app.include_router(transfer_router)
app.include_router(invoice_router)

@app.get("/")
def read_root():
    return {"message": "Open Finance Backend API is running"}
