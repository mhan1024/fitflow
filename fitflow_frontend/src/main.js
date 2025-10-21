import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

import './style.css'
import App from './App.vue'
import HomePage from './pages/HomePage.vue'
import AccountPage from './pages/AccountPage.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: HomePage },
        { path: '/account', component: AccountPage }
    ]
})

const app = createApp(App)
app.use(router)
app.mount('#app') 
