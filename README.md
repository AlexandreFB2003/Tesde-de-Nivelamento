# **Teste de Nivelamento**

Este repositório contém a solução do teste de nivelamento para a vaga de estágio na empresa **Intuitive Care**.

## **Organização do Repositório**

### 📌 **Scraping e Transformação de Dados (Testes 1 e 2)**

📂 **`Scraping_and_transformation/`**

- **`web_scraping.py`** → Realiza web scraping da página fornecida e faz o download dos arquivos em um diretório `.zip` chamado **Anexos**.
- **`scriptDataTransformation.py`** → Utiliza os arquivos da pasta **Anexos**, extrai os dados do **Anexo I** e gera um arquivo CSV chamado **Rol\_de\_procedimentos**, armazenado dentro de um `.zip` chamado **Teste\_Alexandre**.

### 🗄️ **Banco de Dados (Teste 3)**

📂 **`Database/`**

- **📂 `Data/`** → Contém todos os arquivos de dados fornecidos.
- **📂 `sql_scripts/`** → Scripts SQL compatíveis com PostgreSQL.
- **`database.py`** → Código Python que executa um dos scripts SQL no banco de dados.

### 🔌 **Servidor e Interface Web (Teste 4)**

📂 **`Server/`** → Backend desenvolvido com **Flask** seguindo a arquitetura **MVC**.

- Contém uma API que lê o arquivo **CSV** fornecido e retorna os registros com base na **query** enviada como parâmetro.
- A pasta **Postman/** contém a **collection** utilizada para testes.

📂 **`Interface/`** → Frontend desenvolvido com **Vue.js**.

- Aplicação web onde o usuário insere um nome, a aplicação consome a API e retorna as operadoras correspondentes.

📸 Dentro das pastas, há imagens referentes aos testes realizados.
