import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { GoogleButton, authStore } from '../../../index';
import logo from '../../../assets/logo.png'; // ajusta si cambia la ruta
import { loginUser } from '../../../api/auth'; // función de login con axios
import { useEffect } from "react";

export default function Login() {
  const [form, setForm] = useState({
    username: "",
    password: "",
  });
  const navigate = useNavigate();
  const [error, setError] = useState(null);
  const {fetchUser} = authStore();

  useEffect(() => {
    const token = localStorage.getItem("access");
    if (token) {
      navigate("/home");
    }
  }, [navigate]);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    try {
      const { username, password } = form;
      const data = await loginUser(username, password);
      localStorage.setItem("access", data.access);
      localStorage.setItem("refresh", data.refresh);
      await fetchUser();
      navigate("/home"); // o a /dashboard o donde prefieras
    } catch (err) {
      console.error(err);
      setError("Correo o contraseña incorrecta");
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-[#0f172a] to-[#1e293b] px-4 py-20">
      <div className="flex flex-col md:flex-row items-center justify-center gap-1 mb-5">
        <img src={logo} alt="Logo Cine" className="h-70 w-auto" />
      </div>

      <div className="w-full max-w-md bg-white dark:bg-slate-800 rounded-2xl shadow-lg p-8 space-y-6">
        <h2 className="text-2xl font-bold text-center text-slate-800 dark:text-white">Inicia Sesión</h2>

        {error && (
          <div className="text-red-500 text-sm text-center">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm text-slate-700 dark:text-slate-300 mb-1">Correo Electrónico</label>
            <input
              type="username"
              name="username"
              placeholder="Ingrese Correo"
              value={form.username}
              onChange={handleChange}
              required
              className="w-full px-4 py-2 rounded-md bg-slate-100 dark:bg-slate-700 text-slate-800 dark:text-white focus:outline-none focus:ring-2 focus:ring-pink-500"
            />
          </div>

          <div>
            <label className="block text-sm text-slate-700 dark:text-slate-300 mb-1">Contraseña</label>
            <input
              type="password"
              name="password"
              placeholder="Ingrese Contraseña"
              value={form.password}
              onChange={handleChange}
              required
              className="w-full px-4 py-2 rounded-md bg-slate-100 dark:bg-slate-700 text-slate-800 dark:text-white focus:outline-none focus:ring-2 focus:ring-pink-500"
            />
          </div>

          <button
            type="submit"
            className="w-full bg-pink-600 hover:bg-pink-700 transition-colors text-white font-semibold py-2 rounded-md"
          >
            Ingresar
          </button>
        </form>

        <div className="text-center text-sm text-slate-600 dark:text-slate-300">
          ¿Olvidaste tu contraseña?{" "}
          <Link to="/forgot_password" className="text-pink-500 hover:underline">
            Recuperar acceso
          </Link>
        </div>

        <div className="text-center text-sm text-slate-600 dark:text-slate-300">
          ¿No tienes cuenta?{" "}
          <Link to="/register" className="text-pink-500 hover:underline">
            Crear cuenta
          </Link>
        </div>

        <div className="text-center text-sm text-slate-600 dark:text-slate-300">
          <GoogleButton />
        </div>
      </div>
    </div>
  );
}
