
<p align="center">
    <img src="./assets/fundobranco.png" alt="GenUI"/>
</p>

[Visite a documentação oficial da Genui](https://noymaxx.gitbook.io/genui-1)

# The Problem 📊

No mercado financeiro das pequenas e médias empresas (PMEs), um dos desafios mais significativos é a complexidade e a falta de clareza na gestão financeira. Muitos empresários carecem de ferramentas adequadas para entender e gerenciar seu fluxo de caixa, prever crises de liquidez, e tomar decisões estratégicas. Isso leva a uma má gestão financeira, perda de oportunidades e, em muitos casos, ao fracasso empresarial devido a decisões financeiras mal informadas.

# Our Solution 💡

**GenUI** transforma a gestão financeira de PMEs, atuando como um CFO digital que utiliza inteligência artificial para fornecer análises financeiras automatizadas e insights estratégicos em tempo real. Ao coletar e integrar dados financeiros de múltiplas fontes, o GenUI facilita o controle financeiro, melhora a previsão de fluxo de caixa, e ajuda as empresas a identificar e aproveitar oportunidades de crescimento.

## How It Works

1. **Data Collection**: GenUI integra dados financeiros de múltiplas fontes bancárias e de contabilidade usando um backend de simulação de open finance.
2. **AI-Driven Analysis**: Modelos de machine learning processam os dados coletados para prever riscos de inadimplência, antecipar pagamentos vantajosos, e projetar o fluxo de caixa futuro.
3. **Orchestrator (CFO Digital)**: O orquestrador central, ou CFO digital, agrega os insights dos modelos de IA e os integra com dados externos de mercado para gerar recomendações financeiras personalizadas.
4. **User Interface (Generative UI)**: A interface adaptativa da GenUI se ajusta às necessidades específicas de cada tipo de negócio, oferecendo uma experiência de usuário personalizada com insights acionáveis e recomendações estratégicas.

## Advantages of GenUI

- **Real-Time Financial Insights**: GenUI fornece análises financeiras e previsões de fluxo de caixa em tempo real, permitindo que os empresários tomem decisões rápidas e informadas.
- **Automated Financial Management**: A plataforma automatiza processos complexos de gestão financeira, reduzindo a necessidade de intervenção manual e minimizando o risco de erros.
- **Personalized Experience**: A interface generativa adaptativa se ajusta dinamicamente para fornecer informações e insights relevantes para cada tipo de negócio, desde restaurantes até clínicas médicas.
- **AI-Powered Predictions**: GenUI utiliza algoritmos de IA para prever riscos financeiros e identificar oportunidades de otimização de fluxo de caixa, melhorando a saúde financeira geral do negócio.

Ao alinhar os interesses das PMEs com uma solução de gestão financeira eficiente e personalizada, **GenUI** aborda uma dor crítica no mercado financeiro. Nossa solução restaura a confiança na gestão financeira, permitindo que empresários tomem decisões baseadas em dados concretos e estratégicos.

# Roadmap 🗺️

Nossa visão para o GenUI é ambiciosa e estamos comprometidos com a melhoria contínua e expansão da plataforma. Aqui está o que planejamos para o futuro do GenUI:

### Short Term Goals

- **Adicionar Novos Algoritmos de Machine Learning**: Desenvolver e integrar novos algoritmos de machine learning para fornecer informações financeiras ainda mais valiosas e precisas para os usuários, ajudando-os a tomar decisões estratégicas mais informadas.
- **User Feedback Incorporation**: Recolher e integrar feedback dos usuários para ajustar a interface e a experiência do usuário, tornando o GenUI ainda mais intuitivo e acessível para PMEs de diferentes setores.

### Mid Term Goals

- **Expand Data Integration**: Melhorar a integração com outras plataformas financeiras e de contabilidade para expandir o alcance dos dados coletados, garantindo uma visão financeira mais abrangente para os usuários.
- **Análise de Mercado Mais Robusta**: Introduzir múltiplos agentes de análise que avaliem o cenário macroeconômico, tendências de mercado, e riscos externos, oferecendo uma visão ainda mais completa e estratégica para as PMEs.

### Long Term Goals

- **Integration with External Financial Ecosystems**: Expandir as capacidades de integração para incluir parcerias com bancos e outras instituições financeiras, permitindo que o GenUI ofereça uma gama mais ampla de serviços financeiros.
- **Global Expansion**: Após estabelecer uma base sólida no Brasil, pretendemos expandir o GenUI para outros mercados com desafios financeiros similares, adaptando nossa solução para atender às necessidades locais e regulamentos.
- **Se Consolidar como um Hub de Gestão Financeira para PMEs no Brasil**: Tornar-se o principal ponto de referência para a gestão financeira de PMEs no Brasil, oferecendo uma plataforma completa que abrange todas as necessidades financeiras de uma empresa em crescimento.

Seguindo este roadmap, o GenUI continuará a fortalecer a gestão financeira das PMEs, capacitando os empresários a tomar decisões informadas e seguras.

---

Este README atualizado reflete os objetivos ajustados para o curto, médio e longo prazo, destacando como o GenUI planeja evoluir e expandir para melhor atender seus usuários e se consolidar como líder no mercado de gestão financeira para PMEs.


## Estrutura de Pastas

Abaixo está a descrição da estrutura de pastas do projeto para o componente backend, que é responsável por simular a camada de integração com serviços bancários, orquestrar insights e realizar scrapping de dados externos.


### `docs/`

- **`Explicação da Solução.md`**: Este documento detalha toda a solução e os componentes desenvolvidos. Para uma visão mais aprofundada sobre a arquitetura, componentes, e decisões de design, consulte este arquivo.


### `backend/app/`

Este diretório é o núcleo da aplicação backend e simula a camada de integração com os serviços bancários. Ele contém:

- **`database/`**: Contém os datasets fornecidos para o evento. Esses datasets são utilizados para simular o armazenamento de dados bancários e informações associadas.
  
- **`routers/`**: Armazena as rotas da aplicação, que simulam o acesso aos dados em serviços externos. Aqui estão implementadas as diferentes endpoints que interagem com os datasets do diretório `database/`.

### `data/`

Este diretório armazena os arquivos relacionados à camada de orquestração dos insights e outras funções auxiliares:

- **`insight_generators/`**: Contém os componentes responsáveis pela utilização de Machine Learning (ML) para gerar insights importantes. Aqui, os dados são processados e analisados para gerar informações valiosas para os usuários.
  
- **`scrapper/`**: Inclui scripts que viabilizam a hipótese de consulta a fontes externas para análise de insumos. Este componente é essencial para enriquecer as análises de mercado e insumos que integram os insights gerados.
  
- **`insights.json`**: Simula o banco de dados de insights, armazenando as informações geradas especificamente para cada usuário.



### `frontend/src/`

O diretório `src` contém todos os arquivos relacionados à interface do usuário e a lógica do frontend. Abaixo estão os detalhes de cada subdiretório:

- **`assets/`**: Contém as imagens utilizadas no produto. Essas imagens são utilizadas para a composição visual da interface, garantindo uma apresentação consistente e de alta qualidade.

- **`components/`**: Este diretório armazena as duas principais estruturas de interface disponíveis no produto. Os componentes são construídos para oferecer flexibilidade nas interações e manter uma experiência de usuário coesa.

  - **`Content/`**: Contém a primeira estrutura de interface, voltada para a apresentação principal de conteúdos.
  - **`Content2/`**: Contém a segunda estrutura de interface, que oferece uma variação na apresentação do conteúdo.
  - **`Sidebar/`**: A `Sidebar` é um componente comum às duas interfaces, garantindo a consistência na navegação e assegurando que a dinamicidade das interfaces não interfira negativamente na usabilidade.

- **`pages/Home/`**: Armazena os componentes da página inicial, incluindo o `index.js` e os estilos relacionados.

- **`routes/`**: Contém as definições das rotas utilizadas na aplicação, gerenciando a navegação entre diferentes páginas e componentes.

- **`styles/`**: Contém os arquivos de estilos globais utilizados na aplicação, assegurando uma aparência uniforme em todas as interfaces.
