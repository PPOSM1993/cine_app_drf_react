import { create } from 'zustand'
import { auth, provider } from '../firebase/config'
import { signInWithPopup, signOut } from 'firebase/auth'
import {axios} from '../index' // tu configuración con interceptor del token

const useAuthStore = create((set) => ({
  user: null,

  // 🔵 LOGIN CON GOOGLE (Firebase)
  loginWithGoogle: async () => {
    try {
      const result = await signInWithPopup(auth, provider)
      set({ user: result.user })
    } catch (error) {
      console.error('Error al iniciar sesión con Google:', error)
    }
  },

  // 🔵 LOGIN CON DJANGO JWT
  loginWithCredentials: async (username, password) => {
    try {
      const { data } = await axios.post('/authentication/login/', {
        username,
        password,
      })

      // Guarda tokens
      localStorage.setItem('access', data.access)
      localStorage.setItem('refresh', data.refresh)

      // Obtener datos del usuario autenticado
      const res = await axios.get('/authentication/user/')
      set({ user: res.data })

      return true
    } catch (err) {
      console.error('Login JWT falló:', err)
      throw err
    }
  },

  // 🔴 LOGOUT UNIFICADO
  logout: async () => {
    await signOut(auth).catch(() => {}) // Ignora errores si no estás en Google
    localStorage.removeItem('access')
    localStorage.removeItem('refresh')
    set({ user: null })
  },
}))

export default useAuthStore
