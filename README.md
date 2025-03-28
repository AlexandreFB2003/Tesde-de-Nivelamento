# Tesde-de-Nivelamento

Este repositório é referente ao teste de nivelamento para a vaga de estágio na empresa Intuitive Care

Organização:
  A pasta Scraping_and_transformation é referente aos testes 1 e 2

  
    - O arquivo web_scraping.py faz o scraping da págna fornecida e realiza o dowload dos arquivos em uma pasta .zip chamada Anexos

    
    - O arquivo scriptDataTransformation.py utiliza a pasta Anexos, extrai os dados referente ao Anexo I e cria um arquivo CSV chamada Rol_de_procedimentos dentro de uma pasta .zip 
      chamada Teste_Alexandre

  A pasta Database é referente ao teste 3

  
    - A pasta Data contém todos os arquivos de dados fornecidos

    
    - A pasta sql_scripts contém os arquivos com os scripts sql compatíveis com o Banco de Dados PostgreSQL

    
    - O Arquivo database.py é um código em python que executa um dos scripts sql 

  A pasta Server e Interface é referente ao teste 4
    - A pasta Server é referente ao backend, utilizei o framework Flask e construí o servidor em uma arquitetura MVC. Possue uma API que faz a leitura do arquivo CSV fornecido e retorna 
      os registros baseados na query enviada como parâmetro. A pasta Postman contém a colection feita para teste.
    - A pasta Interface é referente a frontend, onde criei uma aplicação web com o framework vue.js, onde o usuário digita o nome desejado, a aplicação consome a API e retorna as 
      operadoras referentes ao nome digitado.


 Nas pastas contém imagens referentes aos testes realizados.

  
