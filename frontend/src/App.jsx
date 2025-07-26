import useAuthStore from './store/authStore'

import { LoginPage } from './index'

function App() {
  const user = useAuthStore((state) => state.user)

  return user ? (
    <div className="p-8">
      <h1 className="text-2xl font-bold text-green-600">Hola, {user.displayName} 👋</h1>
      <p className="mt-2 text-gray-600">Correo: {user.email}</p>
    </div>
  ) : (
    <LoginPage />
  )
}

export default App
