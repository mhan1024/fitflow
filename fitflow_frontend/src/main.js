import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

import './style.css'
import App from './App.vue'
import HomePage from './pages/HomePage.vue'
import AccountPage from './pages/AccountPage.vue'
import BuildPlan from './pages/BuildPlan.vue'
import EditPlan from './pages/EditPlan.vue'
import ProgressPage from './pages/ProgressPage.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: HomePage },
        { path: '/account', component: AccountPage },
        { path: '/build-plan', component: BuildPlan },
        { path: '/edit-plan', component: EditPlan },
        { path: '/progress', component: ProgressPage }
    ]
})

const app = createApp(App)
app.use(router)
app.mount('#app') 
