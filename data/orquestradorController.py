# controller.py
import os
from fastapi import APIRouter
from orquestradorService import OrquestradorService

router = APIRouter()

class OrquestradorController:

    def __init__(self):
        self.service = OrquestradorService()

    async def init_flow_of_insights(self, mock_of_data: dict):
        print("Chegou na controller")
        print("Olha o body: ", mock_of_data)
        # Aqui você pode chamar o método genérico da service, por enquanto usando `generate_insight`
        return await self.service.init_flow_of_insights(mock_of_data)

# Instanciando o Controller
controller = OrquestradorController()

@router.post("/insight")
async def create_insight(insight_object: dict):
    return await controller.init_flow_of_insights(insight_object)
