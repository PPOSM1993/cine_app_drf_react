import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { Link } from "react-router-dom";
import { FaFacebookF, FaInstagram, FaTwitter, FaYoutube } from "react-icons/fa";
import { Moon, Sun } from "lucide-react";

export default function Footer() {
  const [email, setEmail] = useState("");
  const [darkMode, setDarkMode] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Suscrito:", email);
    setEmail("");
  };

  const toggleDark = () => {
    const newMode = !darkMode;
    setDarkMode(newMode);
    document.documentElement.classList.toggle("dark", newMode);
    localStorage.setItem("theme", newMode ? "dark" : "light");
  };

  useEffect(() => {
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "dark") {
      setDarkMode(true);
      document.documentElement.classList.add("dark");
    } else {
      setDarkMode(false);
      document.documentElement.classList.remove("dark");
    }
  }, []);


  return (
    <motion.footer
      initial={{ opacity: 0, y: 50 }}
      whileInView={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8 }}
      className="relative w-full py-16 bg-gradient-to-b bg-gray-900 to-black to-black text-white overflow-hidden"
    >
      <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-10">
        {/* Column 1: Logo + redes */}
        <div className="py-1">
          <h3 className="text-xl font-bold mb-4">🎥 CineApp</h3>
          <p className="text-sm text-gray-300">
            Tu cine favorito en línea. Explora estrenos, preventas y mucho más.
          </p>
          <div className="flex gap-4 mt-4 text-lg">
            <a href="#" className="hover:text-blue-400 transition-all duration-200"><FaFacebookF /></a>
            <a href="#" className="hover:text-pink-500 transition-all duration-200"><FaInstagram /></a>
            <a href="#" className="hover:text-blue-300 transition-all duration-200"><FaTwitter /></a>
            <a href="#" className="hover:text-red-600 transition-all duration-200"><FaYoutube /></a>
          </div>
        </div>

        {/* Column 2: Links */}
        <div className="mt-1 justify-center px-10">
          <h4 className="text-md font-semibold mb-4">Navegación</h4>
          <ul className="space-y-2 text-sm text-gray-300">
            <li>
              <Link to="/" className="hover:text-white transition">Inicio</Link>
            </li>
            <li>
              <Link to="/estrenos" className="hover:text-white transition">Estrenos</Link>
            </li>
            <li>
              <Link to="/categorias" className="hover:text-white transition">Categorías</Link>
            </li>
            <li>
              <Link to="/contacto" className="hover:text-white transition">Contacto</Link>
            </li>
          </ul>
        </div>

        {/* Column 3: Newsletter */}
        <div>
          <h4 className="text-md font-semibold mb-4">Newsletter</h4>
          <p className="text-sm text-gray-300 mb-2">
            Recibe noticias, estrenos y promociones directamente en tu correo.
          </p>
          <form onSubmit={handleSubmit} className="flex flex-col gap-2">
            <input
              type="email"
              placeholder="Tu correo"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="px-3 py-2 rounded-md bg-white/10 text-white placeholder-gray-400 outline-none"
              required
            />
            <button
              type="submit"
              className="bg-pink-600 hover:bg-pink-700 transition rounded-md py-2 text-sm font-semibold"
            >
              Suscribirse
            </button>
          </form>
        </div>

      </div>

      {/* Bottom copyright */}
      <div className="text-center text-sm text-gray-400 mt-10">
        © {new Date().getFullYear()} CineApp. Todos los derechos reservados.
      </div>
    </motion.footer>
  );
}
