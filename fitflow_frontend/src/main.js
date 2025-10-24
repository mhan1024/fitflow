import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

import './style.css'
import App from './App.vue'
import HomePage from './pages/HomePage.vue'
import AccountPage from './pages/AccountPage.vue'
import ExercisesPage from './pages/ExercisesPage.vue'
import BuildPlan from './pages/BuildPlan.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: HomePage },
        { path: '/account', component: AccountPage },
        { path: '/exercises', component: ExercisesPage },
        { path: '/build-plan', component: BuildPlan }
    ]
})

const app = createApp(App)
app.use(router)
app.mount('#app') 
