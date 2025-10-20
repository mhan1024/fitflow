<template>
    <div class="home-page">
        <h1>HOME</h1>
        
        <p v-if="user">{{ user.username }}</p>
        <p v-else>GUEST</p>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAuth } from '../composables/useAuth'

const { user, getCurrentUser } = useAuth()

onMounted(() => {
    getCurrentUser()
})

</script>