import { ref } from 'vue'

const user = ref(null)
const accessToken = ref(null)

export function useAuth() {

    const login = async (username, password) => {
        try {
            const result = await fetch('http://localhost:8000/api/users/login/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    username: username, 
                    password: password
                }) 
            })

            const data = await result.json()

            if (!result.ok) return false

            user.value = {
                firstName: data.first_name, 
                lastName: data.last_name,
                username: data.username
            }

            accessToken.value = data.access

            return true

        } catch (error) {
            console.error(error)
            return false
        }
    }

    const createAccount = async (firstName, lastName, email, username, password) => {
        try {
            const result = await fetch('http://localhost:8000/api/users/signup/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    first_name: form.first,
                    last_name: form.last,
                    email: form.email,
                    username: form.username,
                    password: form.password
                })
            })

            const data = await result.json()

            if (!result.ok) return false

            return login(username, password)

        } catch (error) {
            console.error(error)
            return false
        }
    }

    const getCurrentUser = async () => {
        if (!accessToken.value) return

        try {
            const result = await fetch('http://localhost:8000/api/users/me/', {
                headers: {
                    'Authorization': `Bearer ${accessToken.value}`
                }
            })

            const data = await result.json()

            if (!result.ok) return

            user.value = data

        } catch (error) {
            console.error(error)
        }
    }

    const logout = async () => {
        if (!accessToken.value) return

        try {
            await fetch('http://localhost:8000/api/users/logout/', {
                method: 'POST',
            })

            user.value = null
            accessToken.value = null

        } catch (error) {
            console.error(error)
        }
    }

    return { user, login, createAccount, getCurrentUser, logout }

}