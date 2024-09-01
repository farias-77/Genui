from fastapi import APIRouter, HTTPException, Query
from typing import List
from ..models import Invoice
from ..database.invoice import get_invoices

router = APIRouter(
    prefix="/invoices",
    tags=["Invoices"]
)

@router.get("/", response_model=List[Invoice])
async def read_invoices(skip: int = Query(0, ge=0), limit: int = Query(1000, ge=1)):
    invoices = get_invoices(chunk_size=limit, skip_rows=skip)
    if not invoices:
        raise HTTPException(status_code=404, detail="Nenhum dado de fatura encontrado")
    return invoices
