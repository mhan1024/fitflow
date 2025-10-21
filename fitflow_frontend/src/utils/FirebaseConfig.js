import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider, OAuthProvider } from "firebase/auth";

const firebaseConfig = {
    apiKey: "AIzaSyBQSTVjLTeh3tF64A3yCcy7yRSW4HHUiwc",
    authDomain: "fitflow-daaae.firebaseapp.com",
    projectId: "fitflow-daaae",
    storageBucket: "fitflow-daaae.firebasestorage.app",
    messagingSenderId: "955627725183",
    appId: "1:955627725183:web:ea02f4cd7922bc49dbfa4a",
    measurementId: "G-EDW7XMNC97"
  };

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const googleProvider = new GoogleAuthProvider();
const appleProvider = new OAuthProvider("apple.com");

export { auth, googleProvider, appleProvider };