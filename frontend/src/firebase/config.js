// src/firebase/config.js
import { initializeApp } from 'firebase/app'
import { getAuth, GoogleAuthProvider } from 'firebase/auth'

const firebaseConfig = {
  apiKey: "AIzaSyAEjYEJ2SoYblLuCfcCuP7UmTv8cxKTnDY",
  authDomain: "cinewave-378e4.firebaseapp.com",
  projectId: "cinewave-378e4",
  storageBucket: "cinewave-378e4.appspot.com", // ✅ corregido
  messagingSenderId: "119026781526",
  appId: "1:119026781526:web:651cd3dce589a1ef115af7",
  measurementId: "G-HQZW1F96ZL", // opcional, solo si usas Analytics
}

const app = initializeApp(firebaseConfig)
const auth = getAuth(app)
const provider = new GoogleAuthProvider()

export { auth, provider }
