from fastapi import FastAPI
from open_finance_backend.routers.corporate_purchase import router as corporate_purchase_router
from open_finance_backend.routers.transaction import router as transaction_router
from open_finance_backend.routers.transfer import router as transfer_router
from open_finance_backend.routers.invoice import router as invoice_router

app = FastAPI()

# Incluindo os routers para cada tipo de dado
app.include_router(corporate_purchase_router)
app.include_router(transaction_router)
app.include_router(transfer_router)
app.include_router(invoice_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("open_finance_backend.main:app", host="0.0.0.0", port=8001, reload=True)