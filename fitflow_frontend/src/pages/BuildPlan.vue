<template>
    <div class='build-plan'>
        <h1>BUILD A Plan</h1>

        <div class="goal-selection">
            <h3>Goal Selection</h3>
            <input v-model="selectedGoals" type="checkbox" name="strength" value="strength"/> Strength Training 
            <br>
            <input v-model="selectedGoals" type="checkbox" name="endurance" value="endurance"/> Endurance & Cardio
            <br>
            <input v-model="selectedGoals" type="checkbox" name="mobility" value="mobility"/> Mobility & Flexibility
            <br>

            <p v-if="selectedGoals.length != 0">Selected Goals: {{ selectedGoals }}</p>
        </div>

        <hr>

        <div v-if="selectedGoals.includes('strength')" class="muscle-groups">
            <h3>Muscle Group Selection</h3>
            <input v-model="muscleGroups" type="checkbox" name="muscleGroups" value="chest"/> Chest
            <br>

            <input v-model="muscleGroups" type="checkbox" name="muscleGroups" value="back"/> Back
            <br>

            <input v-model="muscleGroups" type="checkbox" name="muscleGroups" value="legs"/> Legs
            <br>

            <input v-model="muscleGroups" type="checkbox" name="muscleGroups" value="shoulders"/> Shoulders
            <br>

            <input v-model="muscleGroups" type="checkbox" name="muscleGroups" value="arms"/> Arms
            <br>

            <input v-model="muscleGroups" type="checkbox" name="muscleGroups" value="abs"/> Abs
            <br>
            
            <p v-if="muscleGroups.length != 0">Selected Muscle Groups: {{ muscleGroups }}</p>

            <hr>
        </div>

        <div v-if="muscleGroups.length != 0" class="muscle-exercises">
            <h3>EXERCISE SELECTION</h3>

            <ul>
                <li v-for="(muscleGroup, index) in muscleGroups" :key="index">
                    {{ muscleGroup }}
                    <br>

                    <button @click="fetchExercises(muscleGroup, null)"> CHOOSE EXERCISES</button>
                    <br>

                    <ul>
                        <li v-for="(exercise) in muscleExercises[muscleGroup]">
                            {{ exercise.name }}
                            <button @click="addExercise(muscleGroup, exercise)">+</button>
                        </li>
                    </ul>
                    <br>

                    <input v-model="muscleSearch[muscleGroup]" type="text" placeholder="Search..." />
                    <button @click="fetchExercises(muscleGroup, muscleSearch[muscleGroup])">Search</button>
                    <br>

                    <ul>
                        <li v-for="(exercise) in muscleExercises[muscleGroup + 'Query']">
                            {{ exercise.name }}
                            <button @click="addExercise(muscleGroup, exercise)">+</button>
                        </li>
                    </ul>
                    <br>
                </li>
            </ul>

            <hr>
        </div>

        <div v-if="selectedGoals.includes('endurance')" class="endurance-section">
            <h3>Endurance</h3>

            <button @click="fetchExercises('cardio', null)"> CHOOSE CARDIO</button>
            <br>

            <ul>
                <li v-for="(exercise) in muscleExercises['cardio']">
                    {{ exercise.name }}
                    <button @click="addExercise('cardio', exercise)">+</button>
                </li>
            </ul>
            <br>


            <input v-model="muscleSearch['cardio']" type="text" placeholder="Search..." />
            <button @click="fetchExercises('cardio', muscleSearch['cardio'])">Search</button>
            <br>

            <ul>
                <li v-for="(exercise) in muscleExercises['cardioQuery']">
                    {{ exercise.name }}
                    <button @click="addExercise('cardio', exercise)">+</button>
                </li>
            </ul>
            <br>

            <hr>
        </div>

        <div v-if="selectedGoals.includes('mobility')" class="mobility-section">
            <h3>Mobility</h3>

            <button @click="fetchExercises('mobility', null)"> CHOOSE STRETCHES</button>
            <br>

            <ul>
                <li v-for="(exercise) in muscleExercises['mobility']">
                    {{ exercise.name }}
                    <button @click="addExercise('mobility', exercise)">+</button>
                </li>
            </ul>
            <br>

            <input v-model="muscleSearch['mobility']" type="text" placeholder="Search..." />
            <button @click="fetchExercises('mobility', muscleSearch['mobility'])">Search</button>
            <br>

            <ul>
                <li v-for="(exercise) in muscleExercises['mobilityQuery']">
                    {{ exercise.name }}
                    <button @click="addExercise('mobility', exercise)">+</button>
                </li>
            </ul>
            <br>

            <hr>
        </div>

        <div v-if="selectedGoals.includes('strength')" class="strength-details">
            <h3>Weight, sets, & reps</h3>

            <ul>
                <li v-for="category in Object.keys(addedExercises).filter(c => c !== 'cardio' && c !== 'mobility')"  :key="category">

                    <p v-for="(exercise) in addedExercises[category]">
                        {{ exercise.name }}
                        Weight: <input type="number" v-model="exercise.weight"/>
                        Weight Unit: 
                        <select v-model="exercise.weightUnit" name="weightUnit" id="weightUnit" :key="exercise">
                            <option value="kilograms (kg)">kg</option>
                            <option value="pounds (lbs)">lbs</option>
                        </select>
                        Sets: <input type="number" v-model="exercise.sets" required/>
                        Reps: <input type="number" v-model="exercise.reps" required/>
                    </p>
                    
                </li>
            </ul>

            <hr>
        </div>

        <div v-if="selectedGoals.includes('endurance')" class="endurance-details">
            <h3>Time, distance, incline, & speed</h3>

            <ul>
                 <li v-for="category in Object.keys(addedExercises).filter(c => c === 'cardio')"  :key="category">

                    <p v-for="(exercise) in addedExercises[category]">
                        {{ exercise.name }}
                        Time: <input type="time" v-model="exercise.time" required step="1"/>
                        Distance: <input type="number" v-model="exercise.distance" required/>
                        Distance Unit: 
                        <select v-model="exercise.distanceUnit" name="distanceUnit" id="distanceUnit" :key="exercise">
                            <option value="miles">mi</option>
                            <option value="kilometers">km</option>
                            <option value="meters">m</option>                
                        </select>
                        Incline: <input type="number" v-model="exercise.incline" required/>
                        Incline Level: <input type="number" v-model="exercise.inclineUnit" required />
                        Speed: <input type="number" v-model="exercise.speed" required/>
                        Speed Unit: <select v-model="exercise.speedUnit" name="speedUnit" id="speedUnit" :key="exercise">
                            <option value="mph">mph</option>
                            <option value="km/h">km/h</option>
                            <option value="min/mile">min/mile</option>  
                            <option value="min/km">min/km</option>              
                        </select>
                    </p>
                 </li>
            </ul>

            <hr>
        </div>

        <div v-if="selectedGoals.includes('mobility')" class="mobility-details">
            <h3>Duration, reps, sets, intensity</h3>

            <ul>
                <li v-for="category in Object.keys(addedExercises).filter(c => c === 'mobility')"  :key="category">
                    <p v-for="(exercise) in addedExercises[category]">
                        {{ exercise.name }}
                        Duration: <input type="time" v-model="exercise.duration" required step="1"/>
                        Sets: <input type="number" v-model="exercise.sets" required/>
                        Reps: <input type="number" v-model="exercise.reps" required/>
                        Intensity: 
                        <select v-model="exercise.intensity" name="intensity" id="intensity" :key="exercise">
                            <option value="light">light</option>
                            <option value="moderate">moderate</option>
                            <option value="intense">intense</option>
                        </select>
                    </p>
                </li>
            </ul>
            <hr>
            
        </div>

        <div v-if="Object.keys(addedExercises).length != 0" class="selected-exercises">
            <h3>SELECTED EXERCISES</h3>

            <h5>STRENGTH TRAINING</h5>
    
            <p v-for="category in Object.keys(addedExercises).filter(c => c !== 'cardio' && c !== 'mobility')" :key="category">
                <p v-for="(exercise) in addedExercises[category]">
                    {{ exercise.exerciseId }} - {{ exercise.name }} - weight: {{ exercise.weight }} {{ exercise.weightUnit }} - {{ exercise.sets }} x {{ exercise.reps }}
                </p>
            </p>

            <h5>ENDURANCE & CARDIO</h5>

            <p v-for="category in Object.keys(addedExercises).filter(c => c === 'cardio')" :key="category">
                <p v-for="(exercise) in addedExercises[category]">
                    {{ exercise.exerciseId }} - {{ exercise.name }} - time: {{ exercise.time }} - distance: {{ exercise.distance }} {{ exercise.distanceUnit }} - incline: {{ exercise.incline }} {{ exercise.inclineUnit }} - speed: {{ exercise.speed }} {{ exercise.speedUnit }}
                </p>
            </p>
            
            <h5>Mobility & Flexibility</h5>

            <p v-for="category in Object.keys(addedExercises).filter(c => c === 'mobility')" :key="category">
                <p v-for="(exercise) in addedExercises[category]">
                    {{ exercise.exerciseId }} - {{ exercise.name }} - duration: {{ exercise.duration }} - {{ exercise.sets }} x {{ exercise.reps }} - intensity: {{ exercise.intensity }}
                </p>
            </p>

            <button @click="clearSelected">Clear</button>
            <hr>
        </div>
        <button @click="showResults">SAVE CHANGES</button>

    </div>
</template>

<script setup>
import { ref, reactive, watch } from 'vue'

const selectedGoals = ref([])
const muscleGroups = ref([])
const muscleExercises = reactive({})
const muscleSearch = reactive({})

const addedExercises = reactive({})

watch(muscleGroups, (newGroups, oldGroups) => {
    const removed = oldGroups.filter(group => !newGroups.includes(group))

    removed.forEach(group => {
        delete muscleExercises[group]
        delete muscleExercises[`${group}Query`]
        delete addedExercises[group]
    })
})


const fetchExercises = async (muscleGroup, query = null) => {
    try {
        const searchQuery = query || muscleGroup

        const response = await fetch(`https://www.exercisedb.dev/api/v1/exercises/search?offset=0&limit=10&q=${searchQuery}&threshold=0.5`)

        const data = await response.json()
        const dataList = await data.data

        console.log(dataList)

        const key = query ? `${muscleGroup}Query` : muscleGroup
        muscleExercises[key] = dataList


    } catch (error) {
        console.error(error)
    }

}

const addExercise = (muscleGroup, exercise) => {
    if (!addedExercises[muscleGroup]) {
        addedExercises[muscleGroup] = []
    }

    if (!addedExercises[muscleGroup].includes(exercise)) {
        addedExercises[muscleGroup].push(exercise)
    }
}

const showResults = () => {
    console.log(addedExercises)
}

const clearSelected = () => {
    Object.keys(addedExercises).forEach(key => delete addedExercises[key])
}

</script>