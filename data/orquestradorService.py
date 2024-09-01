from openai import OpenAI
from insight_generators.early_invoice.early_invoice import get_early_invoice_insight
from insight_generators.default_analysis.default_analysis import get_default_insight
from insight_generators.receivables.receivables import get_receivables
from scrapper.scrapper_meat import fetch_and_format_meat_data
import os
import json
from dotenv import load_dotenv

_ = load_dotenv()

class OrquestradorService:
    
    def __init__(self):
        self.openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        # self.openai_client = OpenAI(api_key='chave-teste')

    def add_insight_to_file(self, insight):
        file_path='insights.json'
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        else:
            data = []

        data.append(insight)

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
        model_response_receivables = get_receivables()
        insight_buy_opportunity = await self.generate_insight(model_response_receivables)
        self.add_insight_to_file(insight_buy_opportunity)        
        
        # chama .py 3
        model_response_possible_defaults = get_default_insight()
        insight_possible_defaults = await self.generate_insight(model_response_possible_defaults)
        # escreve insight no bd para ser exibido no front / api
        self.add_insight_to_file(insight_possible_defaults)        
        
        file_path='insights.json'
        if os.path.exists(file_path):
            # Carrega o conteúdo existente do arquivo
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        else:
            # Se o arquivo não existir, inicia com um array vazio
            print("ERRO BOLADAO")

    
    async def generate_insight(self, insight_object):
        print("Eu vou delegar para o generate insight apropriado")
        print("O insight object é: ")
        print(insight_object)
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
        elif flow_type == 'buy opportunity':
            print(f"O generate_insight reconheceu que é para o fluxo de raw material")
            return await self.generate_buy_opportunity_insight(insight_object)
            
    async def interact_gpt(self, prompt: str):
        completion = self.openai_client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="gpt-4o",
            response_format={ "type": "json_object"}
        )
        
        print("Resposta do GPT: ")
        print(completion.choices[0].message.content)
        response_to_json = json.loads(completion.choices[0].message.content)
        print("Converted JSON")
        return response_to_json

    
    
    async def generate_early_invoice_insight(self, content):
        print("Esse é o content recebido no generate early invoice insight: ", content)
        
        prompt = "Você é um assistente focado em gerar insights para otimizar o controle financeiro de uma empresa. \nDado as informações exibidas abaixo, eu preciso que você gere uma resposta seguindo o seguinte objeto json: { description: <texto simples e objetivo que descreve sem omitir qualquer detalhe sobre as faturas que podem ser pagas antecipadamente e o valor economizado pelo pagamento antecipado>, reason: <caso aplicável, texto que justifica o racional em executar o pagamento antecipado>} "+ content + "O intuito é ser objetivo e claro sobre a instrução de como o usuário pode realizar os pagamentos antecipados e economizar o valor, justificando o valor da operação. O texto deve soar como uma sugestão assertiva."
        
        prompt = str(prompt)
        
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
    
    async def generate_possible_default_insight(self, content):

        print("Cheguei na função de gerar insight de inadimplência.")

        
        prompt = (
            f"""
            Você é um assistente focado em gerar insights para otimizar o controle financeiro de uma empresa.
            Quero gerar um insight financeiro, em formato de JSON, para pequenas e médias empresas, alertando-as sobre a necessidade de planejar seu fluxo de caixa para a próxima semana, considerando o risco de inadimplência de certos clientes.
            Segue abaixo o input, que é um texto que lista os clientes com maior risco de inadimplência, juntamente com o número de registros de atraso de cada um.

            '''
            {content}
            '''

            {{ description: <texto que descreve de maneira bem contextualizada do risco de inadimplencia>, reason: <caso aplicável, texto que justifica o racional para ficar atento ao fluxo de caixa>}}
            """
        )

        print(f"O prompt é: {prompt}")

        response = await self.interact_gpt(prompt)
        print(response)
        print("Cheguei até aqui.")
        description = response.get('description')
        reason = response.get('reason')
        print("Peguei o description e o reason.")

        return {
            'title': 'Atenção ao Fluxo de Caixa para a Próxima Semana',
            'description': description,
            'action': {
                'type': 'plan cash flow',
            },  
            'reason': reason
        }
    
   
    
    async def get_investment_possibilities(self):
        # chamada a uma api / bd para LLM entender as possibilidades de investimento
        return [
            {
                'title': 'renda fixa com ativos imobiliários',
                'minimum_amount': 1000,
                'rentability': 0.0125,
                'deadline': '3 months'
            },
            {
                'title': 'renda fixa com ativos imobiliários',
                'minimum_amount': 1000,
                'rentability': 0.0165,
                'deadline': '6 months'
            },
            {
                'title': 'renda fixa com ativos imobiliários',
                'minimum_amount': 1000,
                'rentability': 0.0155,
                'deadline': '4 months'
            },
            {
                'title': 'cryptoativos de alta volatilidade ',
                'minimum_amount': 10000,
                'rentability': 0.0225,
                'deadline': '12 months'
            },
            
        ]
    
    async def get_financial_maneuvers():
        # lê bd para entender o caixa atual, 
        investment_possibilities = await self.get_investment_possibilities()
        # lê faturas a serem pagas antecipadamente
        early_invoices = await get_early_invoice_insight()
        # lê faturas a serem antecipadas
        early_receivements = await get_early_receivements()
        
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
        
    async def trigger_financial_maneuvers():
        
        possibilities = await self.get_financial_maneuvers()
        
        maneuvers = []
        
        for possibility in possibilities:
            maneuver = await self.calc_profit_for_maneuver(possibility)
            maneuvers.append(maneuver)
            
        # ordena as manobras
        
        # manobra como insight 
        return await self.generate_financial_maneuvers_insight()
    
    
    async def get_raw_material(self):
        return 'patinho_bovino'
    
    async def search_raw_material_price(raw_material):
        raw_material_pricing_mapping = fetch_and_format_meat_data("https://www.extracarne.com.br/carnes-bovinas")
        return { raw_material: raw_material_pricing_mapping }
    
    async def analyze_raw_material_relative_price(actual_price):
        return { 
                'raw_material': 'patinho_bovino',
                'actual_price': actual_price,
                'relative_price': {
                    'week': 1.05,
                    'month': 1.10,
                    'bimonthly': 1.78,
                    'semester': 1.97
                }
            }
    
    async def generate_buy_opportunity_insight(self, receivables):
        print("Cheguei no generate_buy_opportunity_insight")
        relative_price = self.get_raw_material_insights()
        print("Peguei o preço relativo corretamente.")

        prompt = f"""
            Você é um assistente focado em gerar insights para otimizar o controle financeiro de um restaurante. 
            Sua comunicação deve ser como se você estivesse falando diretamente para o restaurante, como um assistente dele.

            Suponha que o restaurante tem alguns pagamentos a receber em um mês de vales refeição. A ideia é que ele
            antecipe esses recebíveis, pagando uma taxa para a operadora, pois foi identificado que o preço da carne 
            teve uma queda momentânea.

            Você receberá como input um texto descrevendo os recebíveis que o restaurante tem, além de receber um json que 
            compara o preço atual da carne com o seu histórico. Os valores presentes em "week", "month", "bimonthly" e "semester", se referem
            valor da carne em relação ao preço atual nessas datas.

            Recebíveis
            ###
            {receivables}
            ###

            Comparação de preços
            ###
            {relative_price}
            ###

            Quero gerar um insight em formato de JSON, com os campos abaixo
            {{ description: <texto que descreve de maneira bem contextualizada da oportunidade de compra pela queda de preço da carne e da existência dos recebíveis>, reason: <caso aplicável, texto que justifica o racional para ficar esse insight>}}
            
        """
        response = await self.interact_gpt(prompt)
        description = response.get('description')
        reason = response.get('reason')

        return {
            'title': 'Oportunidade de Compra',
            'description': description,
            'action': None,
            'reason': reason
        }
        
    async def get_raw_material_insights(self):
        raw_material = await self.get_raw_material()
        raw_material_price = await self.search_raw_material_price()
        raw_material_relative = await self.analyze_raw_material_relative_price(raw_material_price)
        return raw_material_relative
        
        