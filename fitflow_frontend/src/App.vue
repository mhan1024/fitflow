<template>
  <div>
    <router-link to="/">HOME</router-link>
    <br>
    <router-link to="/account">ACCOUNT</router-link>
    <br>
    <router-link to="/exercises">EXERCISES</router-link>
    <br>
    <router-link to="/build-plan">BUILD PLAN</router-link>
    <br>
    <router-link to="/edit-plan">EDIT PLAN</router-link>

    <router-view></router-view>
  </div>
</template>

<script setup>
  import HomePage from './pages/HomePage.vue'
  import AccountPage from './pages/AccountPage.vue'
  import ExercisesPage from './pages/ExercisesPage.vue'
  import BuildPlan from './pages/BuildPlan.vue'
  import EditPlan from './pages/EditPlan.vue'
</script>


<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
