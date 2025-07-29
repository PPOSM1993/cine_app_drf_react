import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),
    tailwindcss(),
],
  server: {
    historyApiFallback: true, // Para dev server (por si acaso)
  },
  build: {
    rollupOptions: {
      input: '/index.html',
    },}
})
