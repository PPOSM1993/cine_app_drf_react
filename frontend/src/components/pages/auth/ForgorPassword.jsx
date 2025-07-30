import { useState } from "react";
import { Link } from "react-router-dom";
import logo from "../../../assets/logo.png";

export default function ForgotPassword() {
  const [email, setEmail] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Recuperar contraseña para:", email);
    // Aquí irá la lógica para enviar correo al backend
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-[#0f172a] to-[#1e293b] px-4 py-20">
      <div className="flex flex-col md:flex-row items-center justify-center gap-1 mb-5">
        <img src={logo} alt="Logo Cine" className="h-70 w-auto" />
      </div>

      <div className="w-full max-w-md bg-white dark:bg-slate-800 rounded-2xl shadow-lg p-8 space-y-6">
        <h2 className="text-2xl font-bold text-center text-slate-800 dark:text-white">
          Recuperar Contraseña
        </h2>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm text-slate-700 dark:text-slate-300 mb-1">
              Correo Electrónico
            </label>
            <input
              type="email"
              name="email"
              placeholder="Ingrese su correo"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="w-full px-4 py-2 rounded-md bg-slate-100 dark:bg-slate-700 text-slate-800 dark:text-white focus:outline-none focus:ring-2 focus:ring-pink-500"
            />
          </div>

          <button
            type="submit"
            className="w-full bg-pink-600 hover:bg-pink-700 transition-colors text-white font-semibold py-2 rounded-md"
          >
            Enviar correo de recuperación
          </button>
        </form>

        <div className="text-center text-sm text-slate-600 dark:text-slate-300">
          ¿Recordaste tu contraseña?{" "}
          <Link to="/login" className="text-pink-500 hover:underline">
            Inicia sesión
          </Link>
        </div>
      </div>
    </div>
  );
}
