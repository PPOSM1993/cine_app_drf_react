// src/pages/auth/Login.jsx
import { useState } from "react"
import { useNavigate } from "react-router-dom"
import { authStore } from "../../index"

const Login = () => {
    const navigate = useNavigate()
    const login = authStore((state) => state.login)

    const [formData, setFormData] = useState({
        username: "",
        password: "",
    })
    const [error, setError] = useState(null)
    const [loading, setLoading] = useState(false)

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        })
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        setLoading(true)
        setError(null)

        const res = await login(formData)

        setLoading(false)

        if (res.success) {
            console.log("✅ Login exitoso. Redirigiendo a /home...")
            navigate("/home")
        } else {
            console.log("❌ Login fallido:", res)
        }

    }

    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-50 px-4">
            <div className="max-w-md w-full bg-white p-8 rounded-lg shadow">
                <h2 className="text-2xl font-bold mb-6 text-center">Iniciar sesión</h2>

                {error && (
                    <div className="bg-red-100 text-red-600 px-4 py-2 rounded mb-4 text-sm">
                        {error}
                    </div>
                )}

                <form onSubmit={handleSubmit} className="space-y-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700">Correo, RUT o usuario</label>
                        <input
                            type="text"
                            name="username"  // <-- aquí cambia "identifier" por "username"
                            value={formData.username}
                            onChange={handleChange}
                            required
                            className="w-full border px-3 py-2 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
                        />
                    </div>

                    <div>
                        <label className="block text-sm font-medium text-gray-700">Contraseña</label>
                        <input
                            type="password"
                            name="password"
                            value={formData.password}
                            onChange={handleChange}
                            required
                            className="w-full border px-3 py-2 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
                        />
                    </div>

                    <button
                        type="submit"
                        disabled={loading}
                        className="w-full bg-indigo-600 text-white py-2 rounded-lg hover:bg-indigo-700 transition"
                    >
                        {loading ? "Cargando..." : "Entrar"}
                    </button>
                </form>

                <p className="mt-4 text-center text-sm text-gray-600">
                    ¿No tienes cuenta?{" "}
                    <a href="/register" className="text-indigo-600 hover:underline">
                        Regístrate
                    </a>
                </p>
            </div>
        </div>
    )
}

export default Login
