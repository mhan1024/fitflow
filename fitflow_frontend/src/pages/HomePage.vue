<template>
    <div class="home-page">
        <h1>HOME</h1>

        <p v-if="displayName">Welcome {{ displayName }}</p>
        <p v-else>Welcome GUEST</p>

    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { auth } from '../utils/FirebaseConfig.js'

const displayName = ref('')

onMounted(() => {
    const user = auth.currentUser

    if (user) {
        displayName.value = user.displayName
    }
})
</script>