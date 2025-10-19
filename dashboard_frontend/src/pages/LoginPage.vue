<template>
    <div>
        <h1>LOGIN</h1>

        <form>
            <p>
                Email: <input v-model="form.email" required/>
            </p>
            <p>
                Password: <input v-model="form.password" required/>
            </p>
        </form>
        
    </div>
</template>

<script setup>
import { reactive } from 'vue';

const form = reactive({
    email: '',
    password: ''
});
</script>