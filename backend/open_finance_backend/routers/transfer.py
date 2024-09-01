from fastapi import APIRouter, HTTPException, Query
from typing import List
from ..models import Transfer
from ..database import get_transfers  # Certifique-se de que esta importação está correta

router = APIRouter(
    prefix="/transfers",
    tags=["Transfers"]
)

@router.get("/", response_model=List[Transfer])
async def read_transfers(skip: int = Query(0, ge=0), limit: int = Query(1000, ge=1)):
    """
    Endpoint para ler dados de transferências com paginação.

    :param skip: Número de linhas a serem ignoradas do início do arquivo.
    :param limit: Número de linhas a serem lidas por requisição. Padrão é 1000.
    :return: Lista de transferências.
    """
    transfers = get_transfers(chunk_size=limit, skip_rows=skip)
    if not transfers:
        raise HTTPException(status_code=404, detail="Nenhum dado de transferência encontrado")
    return transfers
