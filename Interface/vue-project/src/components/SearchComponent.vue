<template>
    <div>
      <h1>Pesquisar Operadora</h1>
      <input v-model="query" @input="search" placeholder="Digite o nome da operadora" />
      <ul>
        <li v-for="result in results" :key="result.Registro_ANS">
          <p><strong>{{ result.Razao_Social }}</strong></p>
          <p>{{ result.CNPJ }} | {{ result.Modalidade }}</p>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        query: '',
        results: []
      };
    },
    methods: {
      async search() {
        if (this.query.length > 2) {
          const response = await fetch(`http://127.0.0.1:5000/search?query=${this.query}`);
          const data = await response.json();
          this.results = data;
        } else {
          this.results = [];
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Estilos para o componente de busca */
  input {
    padding: 8px;
    margin-bottom: 10px;
    width: 200px;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    background-color: #f5f5f5;
    padding: 10px;
    margin: 5px 0;
  }
  </style>
  