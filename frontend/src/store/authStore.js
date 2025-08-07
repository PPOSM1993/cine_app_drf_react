// authStore.js
import { create } from "zustand"
import { persist } from "zustand/middleware"
import axios from "axios"

export const authStore = create(
  persist(
    (set) => ({
      user: null,
      isAuthenticated: false,

      login: async (formData) => {
        try {
          const res = await axios.post(
            "http://localhost:8000/api/authentication/login/",
            formData,
            { withCredentials: true }
          )

          set({
            user: res.data.user,
            isAuthenticated: true,
          })

          return { success: true, data: res.data }
        } catch (err) {
          console.error("Login error:", err.response?.data || err.message)
          return {
            success: false,
            error: err.response?.data || { detail: "Error desconocido" },
          }
        }
      },

      logout: () => {
        set({ user: null, isAuthenticated: false })
      },
    }),
    {
      name: "auth-storage", // nombre de la key en localStorage
      partialize: (state) => ({
        user: state.user,
        isAuthenticated: state.isAuthenticated,
      }),
    }
  )
)
