from fastapi import APIRouter, HTTPException, Query
from typing import List
from ..models import Transaction
from ..database.transaction import get_transactions

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

@router.get("/", response_model=List[Transaction])
async def read_transactions(skip: int = Query(0, ge=0), limit: int = Query(1000, ge=1)):
    transactions = get_transactions(chunk_size=limit, skip_rows=skip)
    if not transactions:
        raise HTTPException(status_code=404, detail="Nenhum dado de transação encontrado")
    return transactions
