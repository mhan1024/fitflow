<template>
    <div class="edit-page">
        <h1>EDIT PLAN</h1>

        <button @click="getExercises">GET EXERCISES</button>

        <h3>STRENGTH</h3>
        <div v-if="userPlan.length != 0" v-for="strEx in userPlan.filter(e => e.category === 'strength')">
            {{ strEx.exercise_name }}
            <input type="number" :placeholder="strEx.weight_str" @change="handleInput(strEx, 'weight_str', $event.target.value)"/> 

            <select v-model="strEx.weight_unit_str" @change="handleInput(strEx, 'weight_unit_str', $event.target.value)">
                <option value="kilograms (kg)">kg</option>
                <option value="pounds (lbs)">lbs</option>
            </select>

            <input type="number" v-model="strEx.sets_str" :placeholder="strEx.sets_str" @change="handleInput(strEx, 'sets_str', $event.target.value)"/>
            x
            <input type="number" v-model="strEx.reps_str" :placeholder="strEx.reps_str" @change="handleInput(strEx, 'reps_str', $event.target.value)"/>

            <button @click="deleteExercise(strEx.id)">DELETE</button>
        </div>

        <h3>CARDIO</h3>
        <div v-if="userPlan.length != 0" v-for="carEx in userPlan.filter(e => e.category === 'cardio')">
            {{ carEx.exercise_name }}
            <input type="time" v-model="carEx.time_car" step="1" :placeholder="carEx.time_car" @change="handleInput(carEx, 'time_car', $event.target.value)"/>
            <input type="number" v-model="carEx.distance_car" :placeholder="carEx.distance_car" @change="handleInput(carEx, 'distance_car', $event.target.value)"/>
            <select v-model="carEx.dist_unit_car" @change="handleInput(carEx, 'dist_unit_car', $event.target.value)">
                <option value="miles">mi</option>
                <option value="kilometers">km</option>
                <option value="meters">m</option>                
            </select>
            <!-- INCLINE -->
            <input type="number" v-model="carEx.incline_car" :placeholder="carEx.incline_car" @change="handleInput(carEx, 'incline_car', $event.target.value)"/>

            <input type="number" v-model="carEx.speed_car" :placeholder="carEx.speed_car" @change="handleInput(carEx, 'speed_car', $event.target.value)"/>
            <select v-model="carEx.speed_unit_car" @change="handleInput(carEx, 'speed_unit_car', $event.target.value)">
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
            <input type="time" v-model="mobEx.duration_mob" :placeholder="mobEx.duration_mob" @change="handleInput(mobEx, 'duration_mob', $event.target.value)"/>
            <input type="number" v-model="mobEx.sets_mob" :placeholder="mobEx.sets_mob" @change="handleInput(mobEx, 'sets_mob', $event.target.value)"/>
            x
            <input type="number" v-model="mobEx.reps_mob" :placeholder="mobEx.reps_mob" @change="handleInput(mobEx, 'reps_mob', $event.target.value)"/>
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
let points = reactive([])

const getExercises = async () => {
    const email = auth.currentUser.email

    if (!email) throw new Error("No user is logged in")

    try {
        const response = await fetch(`http://localhost:8000/api/exercises/by_email/?user_email=${email}`, {
            method: "GET"
        })

        const data = await response.json()

        console.log(data)

        if (Array.isArray(data)){
            userPlan.splice(0, userPlan.length, ...data)
        } else {
            userPlan.splice(0, userPlan.length)
        }
        
        await getPoints()

    } catch (error) {
        console.error(error)
    }
}

const getPoints = async() => {
    try {
        const response = await fetch('http://localhost:8000/api/progress/', {
            method: "GET",
        })

        const data = await response.json()
        console.log("POINTS: ", data)

        if (Array.isArray(data)) {
            points.splice(0, points.length, ...data)
        } else {
            points.splice(0, points.length)
        }

    } catch (error) {
        console.error(error)
    }
}

const deleteExercise = async (exerciseId) => {
    const progress = points.find(p => p.user_exercise === exerciseId)

    try {
        const progressResponse = await fetch(`http://localhost:8000/api/progress/${progress.id}/`, {
            method: "DELETE",
        })

        if (!progressResponse.ok) console.log("PROGRESS DELET ERROR")
        
        const exerciseResponse = await fetch(`http://localhost:8000/api/exercises/${exerciseId}/`, {
            method: "DELETE",
        })

        if (!exerciseResponse.ok) console.log("ERROR")

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

const addProgressPoint = async (exerciseId, field, value) => {
    const today = new Date().toISOString().split('T')[0]

    const progress = points.find(p => p.user_exercise === exerciseId)

    console.log(progress)
    
    if (progress) {
        progress[field].push({
            x: today,
            y: parseFloat(value)
        })

        try {
            const response = await fetch(`http://localhost:8000/api/progress/${progress.id}/`, {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(progress)
            })

            if (!response.ok) console.error("failed to save progress point")

        } catch (error) {
            console.log(error)
        }
    }
    
}

const handleInput = (exercise, field, value) => {    

    if (field === 'weight_str' || field === 'time_car' || field === 'distance_car' || field === 'incline_car' || field === 'speed_car' || field === 'duration_mob') {
        addProgressPoint(exercise.id, field, value)
    }
    exercise[field] = value

}
</script>