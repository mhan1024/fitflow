<template>
    <div class="login-page">
        <h1>LOGIN</h1>

        <form @submit.prevent="handleLogin">
            <label for="login-username">Username: </label>
            <input v-model="username" id="login-username" required/>
            <br>

            <label for="login-password">Password: </label>
            <input v-model="password" id="login-password" required/>
            <br>

            <button type="submit">Login</button>
        </form>

        <button v-on:click="handleLogout">Logout</button>
        
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuth } from '../composables/useAuth'

const { login, user, logout } = useAuth()
const username = ref('')
const password = ref('')

const handleLogin = async () => {
    const result = await login(username.value, password.value)
    if (result) console.log("SUCCESSFUL LOGIN: ", user.value)
}

const handleLogout = async () => {
    const result = await logout()
    if (result) console.log("LOGOUT SUCCESS")
}
</script>