from openai import OpenAI
from insight_generators.early_invoice.early_invoice import get_early_invoice_insight
import os
import json

class OrquestradorService:
    
    def __init__(self):
        # openai.api_key = 'your-api-key'
        # self.openai_client = OpenAI(api_key=os.environ.OPENAI_API_KEY)
        self.openai_client = OpenAI(api_key='chave-teste')
        
    def add_insight_to_file(self, insight):
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
        
        insight_early_invoice = await self.generate_insight(model_response_early_invoice)
        self.add_insight_to_file(insight_early_invoice)      
        
        raw_material = await self.get_raw_material()
        
          
        # chama .py 2
        # model_response_monthly_balance = get_monthly_balance_insight()
        # insight_monthly_balance = await self.generate_insight(model_response_possible_defaults)
        # self.add_insight_to_file(insight_monthly_balance)        
        
        # chama .py 3
        # model_response_possible_defaults = get_possible_defaults_insight()
        # insight_possible_defaults = await self.generate_insight(model_response_possible_defaults)
        # # escreve insight no bd para ser exibido no front / api
        # self.add_insight_to_file(insight_possible_defaults)        
        
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
        print("Eu vou delegar para o generate insight apropriado")
        
        flow_type = insight_object.get('type')
        if flow_type == 'early invoice':
            print("O generate_insight reconheceu que é para fluxo de early invoice")
            return await self.generate_early_invoice_insight(insight_object.get('content'))
        elif flow_type == 'possible defaults':
            print("O generate_insight reconheceu que é para fluxo de possible defaults")
            return await self.generate_possible_default_insight(insight_object)
        elif flow_type == 'monthly balance':
            print("O generate_insight reconheceu que é para fluxo de monthly balance")
            return await self.generate_monthly_balance_insight(insight_object)
            
    async def interact_gpt(self, prompt: str):
        completion = self.openai_client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="gpt-4o",
            response_format={ "type": "json_object"}
        )
        
        print(completion.choices[0].message.content)
        return json.loads(completion.choices[0].message.content)

    
    
    async def generate_early_invoice_insight(self, content):
        print("Esse é o content recebido no generate early invoice insight: ", content)
        
        prompt = "Você é um assistente focado em gerar insights para otimizar o controle financeiro de uma empresa. \nDado as informações exibidas abaixo, eu preciso que você gere uma resposta seguindo o seguinte objeto json: { description: <texto simples e objetivo que descreve sem omitir qualquer detalhe sobre as faturas que podem ser pagas antecipadamente e o valor economizado pelo pagamento antecipado>, reason: <caso aplicável, texto que justifica o racional em executar o pagamento antecipado>} "+ content + "O intuito é ser objetivo e claro sobre a instrução de como o usuário pode realizar os pagamentos antecipados e economizar o valor, justificando o valor da operação. O texto deve soar como uma sugestão assertiva."
        
        print(prompt)
        print(type(prompt))
        prompt = str(prompt)
        print(type(prompt))
        
        response = await self.interact_gpt(prompt)
        description = response.get('description')
        reason = response.get('reason')
        # invoice_ids = response.get('invoices_ids')

        return {
            'title': 'Pague antecipadamente',
            'description': description,
            'action': {
                'type': 'invoice early payment',
                # 'invoice_ids': invoice_ids
                },
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
        
    
    
    
    async def get_raw_material(self):
        
        # get db.json raw material for that user
        
        # identify how to search that info
        return 'carne bovina'
    
    async def search_raw_material_price(raw_material):
        return { 'carne bovina': '26.80/kg' }
    
    async def analyze_raw_material_relative_price():
        return { 
                'raw_material': 'carne bovina',
                'actual_price': '26.80/kg',
                'relative_price': {
                    'week': 0.98,
                    'month': 1.01,
                    'bimonthly': 1.78,
                    'semester': 1.97
                }
            }
    
    async def generate_raw_material_insight():
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
            'title': 'Oportunidade de Compra',
            'description': description,
            'action': None,
            'reason': reason
        }
        
    async def get_raw_material_insights():
        raw_materials = await self.get_raw_material()
        
        raw_materials_prices = []
        for raw_material in raw_materials:
            raw_material_price = await self.search_raw_material_price(raw_material)
            raw_materials_prices.append(raw_material_price)
        
        raw_material_relative = await self.analyze_raw_material_relative_price()
        
        return await self.generate_raw_material_insight()
        