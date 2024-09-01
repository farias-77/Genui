from fastapi import APIRouter, HTTPException
from app.services.open_finance_service import get_mock_data

router = APIRouter(
    prefix="/open-finance",
    tags=["Open Finance"]
)

@router.get("/mock-data")
async def get_mock_data():
    """
    Endpoint para retornar dados mockados de Open Finance.
    """
    try:
        data = get_mock_data()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
