import { createRouter, createWebHistory } from 'vue-router'
import LogInView from '../views/LogInView.vue';
import SignUpView from '../views/SignUpView.vue';
import HomeView from '../views/HomeView.vue';


const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'LogIn',
    component: LogInView
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUpView
  },

];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;