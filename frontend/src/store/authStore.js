import { create } from 'zustand'
import { auth, provider } from '../firebase/config'
import { signInWithPopup, signOut } from 'firebase/auth'

const useAuthStore = create((set) => ({
  user: null,
  loginWithGoogle: async () => {
    try {
      const result = await signInWithPopup(auth, provider)
      set({ user: result.user })
    } catch (error) {
      console.error('Error al iniciar sesión:', error)
    }
  },
  logout: async () => {
    await signOut(auth)
    set({ user: null })
  },
}))

export default useAuthStore
