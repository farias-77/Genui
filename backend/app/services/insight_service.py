from typing import List, Dict

def generate_insights() -> List[Dict]:
    """
    Função para gerar insights financeiros.
    """
    insights = [
        {
            "title": "Pague sua fatura",
            "description": "A fatura XYZ está atrasada.",
            "call_to_action": "Realize o pagamento agora"
        },
        {
            "title": "Análise de Despesas",
            "description": "Suas despesas estão 20% acima do esperado."
        }
    ]
    return insights
