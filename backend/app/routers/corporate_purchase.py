from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.models import CorporatePurchase
from app.database.corporate_purchase import get_corporate_purchases

router = APIRouter(
    prefix="/corporate-purchases",
    tags=["Corporate Purchases"]
)

@router.get("/", response_model=List[CorporatePurchase])
async def read_corporate_purchases(skip: int = Query(0, ge=0), limit: int = Query(1000, ge=1)):
    purchases = get_corporate_purchases(chunk_size=limit, skip_rows=skip)
    if not purchases:
        raise HTTPException(status_code=404, detail="Nenhum dado de compra corporativa encontrado")
    return purchases
