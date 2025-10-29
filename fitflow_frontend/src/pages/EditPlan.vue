<template>
    <div class="edit-page">
        <h1>EDIT PLAN</h1>

        <button @click="getExercises">GET EXERCISES</button>

        <h3>STRENGTH</h3>
        <div v-if="userPlan.length != 0" v-for="strEx in userPlan.filter(e => e.category === 'strength')">
            {{ strEx.exercise_name }}
            <input type="number"  :placeholder="strEx.weight_str" @change="handleInput($event, strEx)"/> 

            <select v-model="strEx.weight_unit_str">
                <option value="kilograms (kg)">kg</option>
                <option value="pounds (lbs)">lbs</option>
            </select>
            <input type="number" v-model="strEx.sets_str" :placeholder="strEx.sets_str" />
            x
            <input type="number" v-model="strEx.reps_str" :placeholder="strEx.reps_str" />
            <button @click="deleteExercise(strEx.id)">DELETE</button>
        </div>

        <h3>CARDIO</h3>
        <div v-if="userPlan.length != 0" v-for="carEx in userPlan.filter(e => e.category === 'cardio')">
            {{ carEx.exercise_name }}
            <input type="time" v-model="carEx.time_car" step="1" :placeholder="carEx.time_car"/>
            <input type="number" v-model="carEx.distance_car" :placeholder="carEx.distance_car"/>
            <select v-model="carEx.dist_unit_car">
                <option value="miles">mi</option>
                <option value="kilometers">km</option>
                <option value="meters">m</option>                
            </select>
            <!-- INCLINE -->
            <input type="number" v-model="carEx.incline_car" :placeholder="carEx.incline_car"/>

            <input type="number" v-model="carEx.speed_car" :placeholder="carEx.speed_car"/>
            <select v-model="carEx.speed_unit_car">
                <option value="mph">mph</option>
                <option value="km/h">km/h</option>
                <option value="min/mile">min/mile</option>
                <option value="min/km">min/km</option>
            </select>
            <button @click="deleteExercise(carEx.id)">DELETE</button>
        </div>

        <h3>MOBILITY</h3>
        <div v-if="userPlan.length != 0" v-for="mobEx in userPlan.filter(e => e.category === 'mobility')">
            {{ mobEx.exercise_name }}
            <input type="time" v-model="mobEx.duration_mob" :placeholder="mobEx.duration_mob" />
            <input type="number" v-model="mobEx.sets_mob" :placeholder="mobEx.sets_mob" />
            x
            <input type="number" v-model="mobEx.reps_mob" :placeholder="mobEx.reps_mob" />
            <button @click="deleteExercise(mobEx.id)">DELETE</button>
        </div>
        
        <br>
        <button @click="updateExercises()">SAVE CHANGES</button>

    </div>

</template>

<script setup>
import { reactive } from 'vue'
import { auth } from '../utils/FirebaseConfig.js'

let userPlan = reactive([])

const getExercises = async () => {
    const email = auth.currentUser.email

    if (!email) throw new Error("No user is logged in")

    try {
        const response = await fetch(`http://localhost:8000/api/exercises/by_email/?user_email=${email}`, {
            method: "GET"
        })

        const data = await response.json()

        console.log(data)

        userPlan.splice(0, userPlan.length, ...data)

    } catch (error) {
        console.error(error)
    }
}

const deleteExercise = async (exerciseId) => {
    try {
        const response = await fetch(`http://localhost:8000/api/exercises/${exerciseId}/`, {
            method: "DELETE",
        })

        if (!response.ok) console.log("ERROR")

        await getExercises()

    } catch (error) {
        console.error(error)
    }
}

const updateExercises = async () => {
    try {
        for (const ex in userPlan) {

            const response = await fetch(`http://localhost:8000/api/exercises/${userPlan[ex].id}/`, {
                method: "PUT", 
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(userPlan[ex])
            })

            if (!response.ok) console.log("ERROR")

        }

    } catch (error) {
        console.error(error)
    }
    
}

const handleInput = (e, strEx) => {
    const oldValue = strEx.weight_str
    const newValue = e.target.value

    console.log("Old:", oldValue, "New:", newValue)
    console.log("HANDLE INPUT DATE: ", strEx.date)
}
</script>