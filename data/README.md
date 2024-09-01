## Como Iniciar o Projeto

Para iniciar o ambiente de desenvolvimento utilizando Docker, siga os passos abaixo:

### 1. Construir a Imagem Docker

No diretório raiz do projeto (onde está localizado o Dockerfile), execute o seguinte comando para construir a imagem Docker:

```bash
docker build -t nome-da-imagem .
```

Substitua nome-da-imagem por um nome que você desejar para a imagem, por exemplo:
```
docker build -t genui-backend .
```
### 2. Executar o Container
Após construir a imagem, execute o container mapeando a porta 8080 do container para a porta 8080 da sua máquina local. Use o comando:

```
docker run -d -p 8080:8080 nome-da-imagem
```

Por exemplo:

```
docker run -d -p 8080:8080 genui-backend
```

### 3. Acessar a Aplicação
Agora, a aplicação estará em execução e você poderá acessá-la através do navegador ou de um cliente HTTP (como Postman ou curl) no seguinte endereço:
```
http://localhost:8080/orquestrador
```

Pronto! Agora você tem o ambiente configurado e a aplicação em execução.

Esse código inclui todas as etapas necessárias para iniciar o ambiente desenvolvido e pode ser copiado diretamente para o seu arquivo README.md.