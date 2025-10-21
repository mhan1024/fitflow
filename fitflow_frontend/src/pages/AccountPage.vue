<template>
    <div class="account-page">
        <h1>Account</h1>

        <h3>LOGIN</h3>
        <form @submit.prevent="handleAuth(1)">
            Email: <input v-model="loginForm.email" type="email" name="email" required/>
            <br>
            Password: <input v-model="loginForm.password" type="password" name="password" required/>
            <br>

            <button type="submit">Login</button>
        </form>

        <button v-on:click="handleAuth(2)">Google Login</button>
        <br>
        <button v-on:click="handleAuth(3)">Apple Login</button>

        <hr>

        <h3>SIGN UP</h3>
        <form @submit.prevent="handleAuth(0)">
            Display Name: <input v-model="signUpForm.displayName" type="text" name="displayName" required/>
            <br>
            Email: <input v-model="signUpForm.email" type="email" name="email" required/>
            <br>
            Password: <input v-model="signUpForm.password" type="password" name="password" required/>
            <br>

            <button type="submit">Create Account</button>
        </form>

        <hr>
        <button @:click="handleLogout">LOGOUT</button>


    </div>
</template>

<script setup>
import { reactive } from 'vue'
import { signUpForm, loginForm, handleAuth, handleLogout } from '../utils/AuthenticateUser.js'



</script>