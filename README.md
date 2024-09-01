
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
