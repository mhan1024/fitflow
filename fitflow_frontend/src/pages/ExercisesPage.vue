<template>
    <div class="exercise-page">
        <h1>EXERCISE</h1>

        <input v-model='searchForm.query' type='text' name='searchQuery' />
        <button @click='handleSearch'>Search</button>

        <ol v-if="resultsList.length != 0">
            <li v-for="(exercise, index) in resultsList" :key="index">
                {{ exercise }}
            </li>
        </ol>

        <button v-if="resultsList.length != 0" @click='loadMore'>Load More</button>

    </div>
</template>

<script setup>
import { reactive, ref } from 'vue'

const searchForm = reactive({
    query: ''
})

const resultsList = ref([])
const offset = ref(0)
const limit = 25
const hasMore = ref(true)


const handleSearch = async () => {
    resultsList.value = []
    offset.value = 0
    hasMore.value = true
    
    await getResults()
}

const getResults = async () => {

    try {
        const response = await fetch(`https://www.exercisedb.dev/api/v1/exercises?offset=${offset.value}&limit=25&search=${searchForm.query}&sortBy=name&sortOrder=asc`)

        const data = await response.json();
        const dataList = await data.data;

        dataList.forEach(result =>  {
            console.log(result)
            // exerciseId, name, gifUrl, targetMuscles, secondaryMuscles, equipments, instructions

            resultsList.value.push(result.name)
        })


        if (dataList.length < 25) {
            hasMore.value = false
        } else {
            offset.value += 25
        }

    } catch (error) {
        console.error(error)
    }

}

const loadMore = async () => {
    if (hasMore.value) {
        await getResults()
    }
}

</script>