import { Link, useNavigate } from "react-router-dom";
import { authStore } from "../../index";

export default function Home() {
    const { user, logout } = authStore()
  const navigate = useNavigate()

  const handleLogout = async () => {
    await logout()
    navigate("/login")
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-[#0f172a] to-[#1e293b] text-white px-4">
      <h1 className="text-4xl font-bold mb-4">Bienvenido al sistema 🎬</h1>
      <p className="mb-6 text-center max-w-md">
        Has iniciado sesión correctamente. Esta es una página de prueba para validar la autenticación.
      </p>

    <Link onClick={handleLogout}
        className="bg-pink-600 hover:bg-pink-700 transition-colors text-white font-semibold py-2 px-4 rounded-md"
      >
        Cerrar sesión
      </Link>
    </div>
  );
}
