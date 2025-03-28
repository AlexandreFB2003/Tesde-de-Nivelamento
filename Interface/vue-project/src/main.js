import { createApp } from 'vue';   // Importe o createApp do Vue 3
import App from './App.vue';        // Importe o componente App
import router from './routers';     // Importe o router corretamente

const app = createApp(App);        // Crie a aplicação com o App
app.use(router);                   // Use o Vue Router
app.mount('#app');                 // Monte a aplicação no #app
