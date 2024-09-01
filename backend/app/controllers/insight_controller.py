from fastapi import APIRouter, HTTPException
from app.services.insight_service import generate_insights

router = APIRouter(
    prefix="/insights",
    tags=["Insights"]
)

@router.get("/")
async def get_insights():
    """
    Endpoint para retornar a lista de insights gerados pelo CFO as a Service.
    """
    try:
        insights = generate_insights()
        return insights
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
