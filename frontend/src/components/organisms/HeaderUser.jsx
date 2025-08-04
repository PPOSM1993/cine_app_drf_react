import { useState } from "react";
import { Menu, X } from "lucide-react";
import { LogoWithText, HeaderBackground3D, authStore } from "../../index";
import { Link, useNavigate } from "react-router-dom";

const navLinks = [
  { name: "Inicio", href: "/" },
  { name: "Cartelera", href: "/cartelera" },
  { name: "Promociones", href: "/promociones" },
  { name: "Confitería", href: "/confiteria" },
  { name: "Trabaja con Nosotros", href: "/trabaja" },
  { name: "Contacto", href: "/contacto" },
];
export default function HeaderUser() {
  const [isOpen, setIsOpen] = useState(false);
  const navigate = useNavigate()
  const { user, logout } = authStore()

  const handleLogout = async () => {
    await logout()
    navigate("/login")
  }

  return (
    <header className="fixed top-0 left-0 w-full z-50 bg-gradient-to-br from-[#0f172a] to-[#1e293b] backdrop-blur-md text-white transition-all duration-300">

      <div className="max-w-7xl mx-auto px-2 py-4 flex justify-between items-center">
        {/* Logo a la izquierda */}
        <div className="flex items-center gap-4">
          <LogoWithText />
        </div>
        {/* Menú escritorio */}
        <nav className="hidden md:flex items-center space-x-6">
          {navLinks.map((link) => (
            <a
              key={link.name}
              href={link.href}
              className="hover:text-[#D7263D] font-medium transition"
            >
              {link.name}
            </a>
          ))}
          {/* Botones alineados */}
          <div className="flex space-x-2 ml-4">
            <Link
              to="/profile"
              className="px-4 py-2 rounded-sm font-semibold text-white bg-gray-600 hover:bg-gray-700 transition duration-300 shadow"
            >
              Perfil
            </Link>
            <Link onClick={handleLogout}
              className="bg-red-600 hover:bg-red-700 transition-colors text-white font-semibold py-2 px-4 rounded-md"
            >
              Cerrar sesión
            </Link>
          </div>
        </nav>
        {/* Botón burger móvil */}
        <button className="md:hidden text-white" onClick={() => setIsOpen(!isOpen)}>
          {isOpen ? <X size={24} /> : <Menu size={24} />}
        </button>
      </div>
      {/* Menú móvil desplegable */}
      {isOpen && (
        <div className="fixed inset-0 z-40">
          {/* Fondo desenfocado */}
          <div
            className="absolute inset-0 bg-[#F0F0F0] bg-opacity-40 backdrop-blur-sm"
            onClick={() => setIsOpen(false)}
          />
          {/* Menú lateral con slide-in y scroll */}
          <div className="absolute top-0 right-0 h-screen w-full sm:w-[95%] bg-gradient-to-br from-[#0f172a] to-[#1e293b] text-white z-50 shadow-lg animate-slide-in-right overflow-y-auto">
            <div className="flex flex-col h-full">
              {/* Botón cerrar */}
              <div className="flex justify-end p-4">
                <button className="text-[#D7263D]" onClick={() => setIsOpen(false)}>
                  <X size={28} />
                </button>
              </div>
              {/* Contenido scrollable */}
              <nav className="flex flex-col flex-grow px-6 pb-6 space-y-6 scroll-invisible">
                {navLinks.map((link) => (
                  <a
                    key={link.name}
                    href={link.href}
                    className="hover:text-[#D7263D] font-semibold transition"
                    onClick={() => setIsOpen(false)}
                  >
                    {link.name}
                  </a>
                ))}
                {!user && (
                  <div className="mt-8 flex gap-4">
                    <Link
                      to="/profile"
                      className="bg-red-600 hover:bg-red-700 text-white font-semibold py-2 px-4 rounded-md transition"
                    >
                      Perfil
                    </Link>
                    <Link
                      onClick={handleLogout}
                      className="bg-green-600 hover:bg-green-700 text-white-700 font-semibold py-2 px-4 rounded-md transition"
                    >
                      Cerrar Sesion
                    </Link>
                  </div>
                )}
              </nav>
            </div>
          </div>
        </div>
      )}
    </header>
  );
}