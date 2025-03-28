import { createRouter, createWebHistory } from 'vue-router'; // Use o Vue Router 4
import HomePage from '../views/HomePage.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage,  // Componente de página inicial
  },
];

const router = createRouter({
  history: createWebHistory(),  // Usar o history para navegação sem recarregar a página
  routes,
});

export default router;
