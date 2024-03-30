<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Desafio ICCT</h3>


---


## 📝 Índice

- [Sobre Started](#about)
- [Getting Started](#getting_started)
- [Authors](#authors)

## 🧐 Sobre <a name = "about"></a>

Projeto desenvolvido para o desafio icct, consiste em desenvolver e implementar a feature de Cadastro de Usuários, software Web, com acesso a consulta de CEP de uma API externa. O sistema contará com as seguintes camada: Interface (front-end), Regras de negócio (back-end) e Banco de Dados.

- Use validação nos campos;
- Salve em um banco de dados relacional (Preferência Postgresql);
- Documente a API;
- Os campos são nome, sobrenome, cpf, email, login e senha.

- 
- ## 🏁 Getting Started <a name = "getting_started"></a>
Instruções para ter uma cópia do repositório.

### Pré-requisitos

-   **Python - Supported Versions:** >= 3.10
-   **Database:** MySQL
-   **Run-time environment:**: Flask, npm & Quasar Framework

### Instalação

- Clone

O repositório onde se encontra o código fonte da aplicação está na branch **master**. Logo:

```bash
$ git clone https://github.com/maurorgrdev/desafio-icct.git
$ cd desafio-icct
$ git checkout master
```

## Docker
### Construção e Execução

Para construir e executar os contêineres Docker, siga estas etapas:

1. Construa as imagens Docker: `docker-compose build`
2. Inicie os contêineres: `docker-compose up -d`

Isso iniciará os contêineres Docker para o backend, frontend e banco de dados PostgreSQL conforme definido no arquivo `docker-compose.yml`.

### Acesso

Depois de iniciar os contêineres, você poderá acessar a aplicação através do navegador da web em `http://localhost:9000` para o frontend e `http://localhost:5001` para o backend.

### Parar e Remover

Para parar e remover os contêineres Docker, você pode usar o seguinte comando:

```bash
$ docker-compose down
```




