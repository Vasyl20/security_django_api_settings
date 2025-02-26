import { createRouter, createWebHistory } from 'vue-router';
import UserLogin from '@/views/UserLogin.vue';
import UserHome from '@/views/UserHome.vue';

const routes = [
  { path: '/login', component: UserLogin },
  { path: '/home', component: UserHome }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
