import { useState } from "react";
import { Link } from "react-router-dom";
import { GoogleButton } from "../../../index";
import logo from "../../../assets/logo.png";

export default function Register() {
  const [form, setForm] = useState({
    email: "",
    username: "",
    first_name: "",
    last_name: "",
    rut: "",
    password: "",
    confirm_password: "",
    accepted_terms: false,
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setForm({
      ...form,
      [name]: type === "checkbox" ? checked : value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (form.password !== form.confirm_password) {
      alert("Las contraseñas no coinciden");
      return;
    }
    console.log("Registro con:", form);
    // Aquí luego se conecta el backend
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-[#0f172a] to-[#1e293b] px-4 py-20">
      <div className="flex flex-col md:flex-row items-center justify-center gap-1 mb-5">
        <img src={logo} alt="Logo Cine" className="h-70 w-auto" />
      </div>

      <div className="w-full max-w-md bg-white dark:bg-slate-800 rounded-2xl shadow-lg p-8 space-y-6">
        <h2 className="text-2xl font-bold text-center text-slate-800 dark:text-white">
          Crear Cuenta
        </h2>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="grid grid-cols-2 gap-2">
            <input
              type="text"
              name="first_name"
              placeholder="Nombre"
              value={form.first_name}
              onChange={handleChange}
              required
              className="px-4 py-2 rounded-md bg-slate-100 dark:bg-slate-700 text-slate-800 dark:text-white"
            />
            <input
              type="text"
              name="last_name"
              placeholder="Apellido"
              value={form.last_name}
              onChange={handleChange}
              required
              className="px-4 py-2 rounded-md bg-slate-100 dark:bg-slate-700 text-slate-800 dark:text-white"
            />
          </div>

          <input
            type="text"
            name="username"
            placeholder="Nombre de usuario"
            value={form.username}
            onChange={handleChange}
            required
            className="w-full px-4 py-2 rounded-md bg-slate-100 dark:bg-slate-700 text-slate-800 dark:text-white"
          />

          <input
            type="email"
            name="email"
            placeholder="Correo electrónico"
            value={form.email}
            onChange={handleChange}
            required
            className="w-full px-4 py-2 rounded-md bg-slate-100 dark:bg-slate-700 text-slate-800 dark:text-white"
          />

          <input
            type="text"
            name="rut"
            placeholder="RUT (12345678-9)"
            value={form.rut}
            onChange={handleChange}
            className="w-full px-4 py-2 rounded-md bg-slate-100 dark:bg-slate-700 text-slate-800 dark:text-white"
          />

          <input
            type="password"
            name="password"
            placeholder="Contraseña"
            value={form.password}
            onChange={handleChange}
            required
            className="w-full px-4 py-2 rounded-md bg-slate-100 dark:bg-slate-700 text-slate-800 dark:text-white"
          />

          <input
            type="password"
            name="confirm_password"
            placeholder="Confirmar contraseña"
            value={form.confirm_password}
            onChange={handleChange}
            required
            className="w-full px-4 py-2 rounded-md bg-slate-100 dark:bg-slate-700 text-slate-800 dark:text-white"
          />

          <div className="flex items-center">
            <input
              type="checkbox"
              name="accepted_terms"
              checked={form.accepted_terms}
              onChange={handleChange}
              className="mr-2"
              required
            />
            <label className="text-sm text-slate-600 dark:text-slate-300">
              Acepto los{" "}
              <Link to="/terms" className="text-pink-500 hover:underline">
                Términos y Condiciones
              </Link>
            </label>
          </div>

          <button
            type="submit"
            className="w-full bg-pink-600 hover:bg-pink-700 transition-colors text-white font-semibold py-2 rounded-md"
          >
            Crear cuenta
          </button>
        </form>

        <div className="text-center text-sm text-slate-600 dark:text-slate-300">
          ¿Ya tienes cuenta?{" "}
          <Link to="/login" className="text-pink-500 hover:underline">
            Inicia sesión
          </Link>
        </div>

        <div className="text-center text-sm text-slate-600 dark:text-slate-300">
          <GoogleButton />
        </div>
      </div>
    </div>
  );
}
