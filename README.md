Tesde-de-Nivelamento
Este repositório contém a implementação do teste de nivelamento para a vaga de estágio na Intuitive Care.

Organização do Projeto
📂 Scraping_and_transformation (Testes 1 e 2)
web_scraping.py → Realiza o scraping da página fornecida e faz o download dos arquivos em uma pasta .zip chamada Anexos.

scriptDataTransformation.py → Usa os arquivos da pasta Anexos, extrai os dados referentes ao Anexo I e gera um arquivo .csv chamado Rol_de_procedimentos dentro de uma pasta .zip chamada Teste_Alexandre.

📂 Database (Teste 3)
Data/ → Contém os arquivos de dados fornecidos.

sql_scripts/ → Scripts SQL compatíveis com o banco de dados PostgreSQL.

database.py → Script Python que executa um dos scripts SQL.

📂 Server e Interface (Teste 4)
📂 Server (Backend)

Desenvolvido com Flask em arquitetura MVC.

API que lê o arquivo .csv fornecido e retorna os registros baseados na query enviada como parâmetro.

📂 Postman/ → Contém a collection para testes.

📂 Interface (Frontend)

Aplicação web feita com Vue.js.

Permite buscar operadoras pelo nome digitado e exibe os resultados consumindo a API do backend.

🚀 Como Rodar o Projeto
🔧 Pré-requisitos
Certifique-se de ter instalados:

Python 3

Node.js

PostgreSQL

Git

⚙️ Configuração do Backend (Server)
Instale as dependências:

sh
Copiar
Editar
pip install flask flask-cors
Execute o servidor:

sh
Copiar
Editar
python app.py
O backend estará rodando em:

arduino
Copiar
Editar
http://localhost:5000
🎨 Configuração do Frontend (Interface)
Acesse a pasta do frontend:

sh
Copiar
Editar
cd Interface/vue-project
Instale as dependências:

sh
Copiar
Editar
npm install
Execute o frontend:

sh
Copiar
Editar
npm run serve
A interface estará disponível em:

arduino
Copiar
Editar
http://localhost:8080
Caso tenha dúvidas ou precise de mais detalhes, sinta-se à vontade para entrar em contato! 🚀
