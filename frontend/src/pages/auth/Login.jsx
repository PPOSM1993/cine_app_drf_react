import { useState, useEffect } from "react"
import { useNavigate } from "react-router-dom"
import { authStore } from "../../index"
import logo from "../../assets/logo.png" // Asegúrate de tener una imagen de logo 
const Login = () => {
    const navigate = useNavigate()
    const { login, token } = authStore()

    const [formData, setFormData] = useState({
        username: "",
        password: "",
    })
    const [error, setError] = useState(null)
    const [loading, setLoading] = useState(false)

    // Redirige si ya está logueado (por token)
    useEffect(() => {
        if (token) {
            navigate("/home", { replace: true })
        }
    }, [token, navigate])

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
            navigate("/home")
        } else {
            setError("Usuario o contraseña incorrectos.")
        }
    }

    return (
        <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-[#0f172a] to-[#1e293b] px-4 py-20">
      <div className="flex flex-col md:flex-row items-center justify-center gap-1 mb-5">
        <img src={logo} alt="Logo Cine" className="h-70 w-auto" />
      </div>


            <div className="w-full max-w-md bg-white dark:bg-slate-800 rounded-2xl shadow-lg p-8 space-y-6">
                <h2 className="text-2xl font-bold mb-6 text-center text-white">Iniciar sesión</h2>

                {error && (
                    <div className="bg-red-100 text-red-600 px-4 py-2 rounded mb-4 text-sm">
                        {error}
                    </div>
                )}

                <form onSubmit={handleSubmit} className="space-y-4 text-white">
                    <div>
                        <label className="block text-sm font-medium text-white py-2">Usuario </label>
                        <input
                            type="text"
                            name="username"
                            value={formData.username}
                            placeholder="Correo, RUT o Nombre de Usuario"
                            onChange={handleChange}
                            required
                            className="w-full border px-3 py-2 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 border-gray-300 dark:bg-slate-700 dark:text-white"
                        />
                    </div>

                    <div>
                        <label className="block text-sm font-medium py-2">Contraseña</label>
                        <input
                            type="password"
                            name="password"
                            placeholder="Contraseña"
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
