# CRUD Clientes em Python

Este é um projeto de CRUD (Create, Read, Update, Delete) desenvolvido em Python para o gerenciamento de clientes, utilizando conexão com o banco de dados MySQL.

## Funcionalidades
- Adicionar clientes
- Listar clientes
- Atualizar clientes
- Excluir clientes

## Requisitos
1. **Python 3.x** instalado no sistema.
2. **MySQL** configurado e em execução.
3. Biblioteca `mysql-connector-python` instalada:
   ```bash
   pip install mysql-connector-python
Configuração do Banco de Dados
Crie um banco de dados no MySQL com o nome crud_clientes:
sql

CREATE DATABASE crud_clientes;
Crie a tabela clientes:

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    telefone VARCHAR(50) NOT NULL
);
(Opcional) Insira registros fictícios na tabela:

INSERT INTO clientes (nome, email, telefone)
VALUES 
    ('Alice Santos', 'alice@email.com', '11987654321'),
    ('Bruno Oliveira', 'bruno@email.com', '11991234567'),
    ('Carla Souza', 'carla@email.com', '11993456789'),
    ('Diego Lima', 'diego@email.com', '11992345678'),
    ('Fernanda Costa', 'fernanda@email.com', '11998765432');


    
## Configuração do Projeto
No arquivo Python, configure os dados de conexão com o MySQL:


host="127.0.0.1",
user="root",
password="87654321",
database="crud_clientes"
Como Executar
Certifique-se de que o MySQL está em execução.

No terminal, execute o arquivo principal:


python crud_clientes.py
Navegue pelo menu para adicionar, listar, atualizar ou excluir clientes.

## Observações
Antes de postar o projeto em produção, implemente validações mais robustas no código.
Certifique-se de que os dados de conexão ao banco de dados estão protegidos em projetos reais.
