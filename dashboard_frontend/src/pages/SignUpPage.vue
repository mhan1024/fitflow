<template>
    <div class="signup-page">
        <h1>SIGN UP</h1>

        <form @submit.prevent="handleCreateAccount">
            <label for="create-first-name">First Name: </label>
            <input v-model="firstName" id="create-first-name" required/>
            <br>

            <label for="create-last-name">Last Name: </label>
            <input v-model="lastName" id="create-last-name" required/>
            <br>

            <label for="create-email">Email: </label>
            <input v-model="email" id="create-email" required />
            <br>

            <label for="create-username">Username: </label>
            <input v-model="username" id="create-username" required />
            <br>

            <label for="create-password">Password: </label>
            <input v-model="password" id="create-password" required />
            <br>

            <button type="submit">Create Account</button>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuth } from '../composables/useAuth'

const { createAccount, user } = useAuth
const firstName = ref('')
const lastName = ref('')
const email = ref('')
const username = ref('')
const password = ref('')

const handleCreateAccount = async () => {
    const result = await createAccount(firstName.value, lastName.value, email.value, username.value, password.value)

    if (result) console.log("SUCCESSFUL CREATION: ", user.value)
}

</script>