# from openai import OpenAI
import openai
from insight_generators.early_invoice.early_invoice import get_early_invoice_insight
import os

class OrquestradorService:
    
    def __init__(self):
        openai.api_key = 'your-api-key'
        self.openai_client = openai
        
    def add_insight_to_file(insight):
        file_path='insights.json'
        # Verifica se o arquivo já existe
        if os.path.exists(file_path):
            # Carrega o conteúdo existente do arquivo
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        else:
            # Se o arquivo não existir, inicia com um array vazio
            data = []

        # Adiciona o novo insight ao array
        data.append(insight)

        # Escreve o array atualizado de volta ao arquivo
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    
    
    async def init_flow_of_insights(self, mock_of_data):
        print("Chegou na service")
        print("mock of data: " , mock_of_data)
        
        # chama early invoice model
        model_response_early_invoice = get_early_invoice_insight()
        print("gente: ", model_response_early_invoice)
        
        insight_early_invoice = self.generate_insight(model_response_early_invoice)
        self.add_insight_to_file(insight_early_invoice)      
          
        # chama .py 2
        model_response_monthly_balance = get_monthly_balance_insight()
        insight_monthly_balance = self.generate_insight(model_response_possible_defaults)
        self.add_insight_to_file(insight_monthly_balance)        
        
        # chama .py 3
        model_response_possible_defaults = get_possible_defaults_insight()
        insight_possible_defaults = self.generate_insight(model_response_possible_defaults)
        # escreve insight no bd para ser exibido no front / api
        self.add_insight_to_file(insight_possible_defaults)        
        
        if os.path.exists():
            file_path='insights.json'
            # Carrega o conteúdo existente do arquivo
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        else:
            # Se o arquivo não existir, inicia com um array vazio
            print("ERRO BOLADAO")

    
    async def generate_insight(self, insight_object):
        flow = insight_object.get('flow')
        if flow == 'early invoice':
            return await self.generate_early_invoice_insight(insight_object)
        elif flow == 'possible defaults':
            return await self.generate_possible_default_insight(insight_object)
        elif flow == 'monthly balance':
            return await self.generate_monthly_balance_insight(insight_object)
            
    async def interact_gpt(self, prompt: str):
        completion = await openai.ChatCompletion.create(
            messages=[{"role": "system", "content": prompt}],
            model="gpt-4"
        )
        
        print(completion.choices[0].message)
        return completion.choices[0].message

    
    
    async def generate_early_invoice_insight(self, insight_object):
        prompt = (
            "Você é um assistente focado em gerar insights para otimizar o controle financeiro de uma empresa. "
            "Dado as informações exibidas abaixo, eu preciso que você gere uma resposta seguindo o seguinte objeto json: blablabla\n"
            "O intuito é ser objetivo e claro sobre a instrução de como o usuário pode realizar os pagamentos antecipados "
            "e economizar o valor, justificando o valor da operação. O texto deve soar como uma sugestão assertiva."
        )
        response = await self.interact_gpt(prompt)
        description = response.get('description')
        reason = response.get('reason')

        return {
            'title': 'Pague antecipadamente',
            'description': description,
            'action': None,
            'reason': reason
        }

    
    async def generate_monthly_balance_insight():
        
        prompt = (
            "Você é um assistente focado em gerar insights para otimizar o controle financeiro de uma empresa. "
            "Dado as informações exibidas abaixo, eu preciso que você gere uma resposta seguindo o seguinte objeto json: blablabla\n"
            "O intuito é ser objetivo e claro sobre a instrução de como o usuário pode realizar os pagamentos antecipados "
            "e economizar o valor, justificando o valor da operação. O texto deve soar como uma sugestão assertiva."
        )
        response = await self.interact_gpt(prompt)
        description = response.get('description')
    
        return {
            'title': 'Balanço Mensal',
            'description': description,
            'action': None,
            'reason': None
        }
    
    
    async def generate_possible_default_insight():
        
        prompt = (
            "Você é um assistente focado em gerar insights para otimizar o controle financeiro de uma empresa. "
            "Dado as informações exibidas abaixo, eu preciso que você gere uma resposta seguindo o seguinte objeto json: blablabla\n"
            "O intuito é ser objetivo e claro sobre a instrução de como o usuário pode realizar os pagamentos antecipados "
            "e economizar o valor, justificando o valor da operação. O texto deve soar como uma sugestão assertiva."
        )
        response = await self.interact_gpt(prompt)
        description = response.get('description')
        reason = response.get('reason')
    
        return {
            'title': 'Possíveis inadimplências',
            'description': description,
            'action': None,
            'reason': reason
        }
    
   
   
    
    async def get_investment_possibilities(self):
        # chamada a uma api / bd para LLM entender as possibilidades de investimento
        return 
    
    async def get_financial_maneuvers():
        # lê bd para entender o caixa atual, 
        # lê faturas a serem pagas antecipadamente
        # lê faturas a serem antecipadas
        prompt = ''
        
        response = await self.interact_gpt(prompt)
        return response
    
    async def calc_profit_for_maneuver(object):
        
        # desmembra objeto em
        # tempo total
        # custo
        # retorno
        # lucro
        
        # gera string pra interação com gpt
        return
    
    async def trigger_financial_maneuvers():
        
        possibilities = await self.get_financial_maneuvers()
        
        maneuvers = []
        
        for possibility in possibilities:
            maneuver = await self.calc_profit_for_maneuver(possibility)
            maneuvers.append(maneuver)
            
        # ordena as manobras
        
        # manobra como insight 
        
    async def generate_financial_maneuvers_insight(self, insight_object):
        prompt = (
            "Você é um assistente focado em gerar insights para otimizar o controle financeiro de uma empresa. "
            "Dado as informações exibidas abaixo, eu preciso que você gere uma resposta seguindo o seguinte objeto json: blablabla\n"
            "O intuito é ser objetivo e claro sobre a instrução de como o usuário pode realizar manobras financeiras que consigam trazer lucro para a empresa"
            "e economizar o valor, justificando o valor da operação. O texto deve soar como uma sugestão assertiva."
        )
        response = await self.interact_gpt(prompt)
        title = response.get('title')
        description = response.get('description')
        reason = response.get('reason')

        return {
            'title': title,
            'description': description,
            'action': None,
            'reason': reason
        }
        