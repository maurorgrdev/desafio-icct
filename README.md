<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Desafio ICCT - modificações pessoal</h3>


---


## 📝 Índice

- [Sobre Started](#about)
- [Getting Started](#getting_started)
- [Authors](#authors)

## 🧐 Sobre <a name = "about"></a>

Este branch é apenas para modificações pessoais, a branch que condiz com a solução para o desafio proposto, entregue no dia e horário limite é a master. Projeto desenvolvido para o desafio icct, consiste em desenvolver e implementar a feature de Cadastro de Usuários. O sistema contará com as seguintes camada: Interface (front-end), Regras de negócio (back-end) e Banco de Dados (Postgresql).

- Use validação nos campos;
- Salve em um banco de dados relacional (Preferência Postgresql);
- Documente a API;
- Os campos são nome, sobrenome, cpf, email, login e senha.

  
## 🏁 Getting Started <a name = "getting_started"></a>
Instruções para ter uma cópia do repositório.

### Pré-requisitos

-   **Run-time environment:** Docker

### Instalação

- Clone

O repositório onde se encontra o código fonte da aplicação está na branch **master**. Logo:

```bash
$ git clone https://github.com/maurorgrdev/desafio-icct.git
$ cd desafio-icct
$ git checkout development
```

## Arquivo de configuração (.env) 

Faça uma cópia do arquivo .env.exmaple e preeencha os dados conforme o seu cenário, caso necessário, uma vez que o ambiente docker será construído. 

### JWT Secret Key e Flask Secret Key

Para gerar suas chaves JWT_SECRET_KEY e SECRET_KEY: roder o seguinte comando:
```bash
$ python3 -c "import secrets; flask_secret_key = secrets.token_urlsafe(32); print('Flask SECRET_KEY:', flask_secret_key); jwt_secret_key = secrets.token_urlsafe(32); print('JWT SECRET_KEY:', jwt_secret_key)"
```

Copie as chaves geradas e as cole no arquivo .env

## Docker
### Construção e Execução

Para construir e executar os contêineres Docker, siga estas etapas:

1. Construa as imagens Docker: `docker-compose build`
2. Inicie os contêineres: `docker-compose up -d`

Isso iniciará os contêineres Docker para o backend, frontend e banco de dados PostgreSQL conforme definido no arquivo `docker-compose.yml`.

### Acesso

Depois de iniciar os contêineres, você poderá acessar a aplicação através do navegador da web em `http://localhost:9000` para o frontend e `http://localhost:5001` para o backend.

Rotas disponveis:
- http://localhost:9000/#/login
- http://localhost:9000/#/users
- http://localhost:9000/#/users/profile/:id
- http://localhost:9000/#/users/edit/:id
- http://localhost:9000/#/users/create

### Parar e Remover

Para parar e remover os contêineres Docker, você pode usar o seguinte comando:

```bash
$ docker-compose down
```
