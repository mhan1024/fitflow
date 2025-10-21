import { reactive } from 'vue';
import { auth, googleProvider, appleProvider } from './FirebaseConfig.js';
import { signInWithEmailAndPassword, signInWithPopup, createUserWithEmailAndPassword, updateProfile, signOut } from 'firebase/auth';

const signUpForm = reactive({
    displayName: '',
    email: '',
    password: '' 
});

const loginForm = reactive({
    email: '',
    password: '' 
});

const resetForms = () => {
    signUpForm.displayName = '';
    signUpForm.email = '';
    signUpForm.password = '';

    loginForm.email = '';
    loginForm.password = '';
};

const handleAuth = async (providerId) => {
    try { 

        let authUser;

        switch(providerId) { 
            case 0:
                authUser = await createUserWithEmailAndPassword(auth, signUpForm.email, signUpForm.password);

                await updateProfile(authUser.user, { displayName: signUpForm.displayName }); 

                break;
            case 1:
                authUser = await signInWithEmailAndPassword(auth, loginForm.email, loginForm.password);

                break;
            case 2:
                authUser = await signInWithPopup(auth, googleProvider);
                break;
            case 3:
                authUser = await signInWithPopup(auth, appleProvider);
                break;
            default: 
                throw new Error("No provider id");
        };

        const idToken = await authUser.user.getIdToken();

        const result = await fetch('http://localhost:8000/auth/', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ idToken })
        });

        if (!result.ok) throw new Error(`Server error: ${result.status}`);

        const data = await result.json();

        console.log(data);

        resetForms();

    } catch (error) {
        console.error(error);
    }
}

const handleLogout = async () => {
    try {
        await signOut(auth);

    } catch (error) {
        console.error(error);
    }
}

export { signUpForm, loginForm, resetForms, handleAuth, handleLogout };