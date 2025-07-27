// src/components/organisms/Header.jsx
import { useState } from "react";
import { Menu, X } from "lucide-react";

import { LogoWithText } from '../../index'

const Header = () => {
  const [isOpen, setIsOpen] = useState(false);

  const navLinks = [
    { name: "Inicio", href: "/" },
    { name: "Cartelera", href: "/cartelera" },
    { name: "Ubicaciones", href: "/ubicaciones" },
    { name: "Mi cuenta", href: "/cuenta" },
  ];

  return (
    <header className="fixed top-0 left-0 w-full z-50 bg-black bg-opacity-70 backdrop-blur-md text-white">
      <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
        <LogoWithText />

        <nav className="hidden md:flex space-x-8">
          {navLinks.map((link) => (
            <a key={link.name} href={link.href} className="hover:text-yellow-400 transition">
              {link.name}
            </a>
          ))}
        </nav>

        <button
          className="md:hidden"
          onClick={() => setIsOpen(!isOpen)}
        >
          {isOpen ? <X size={24} /> : <Menu size={24} />}
        </button>
      </div>

      {/* Mobile menu */}
      {isOpen && (
        <div className="md:hidden px-4 pb-4">
          <nav className="flex flex-col space-y-2">
            {navLinks.map((link) => (
              <a key={link.name} href={link.href} className="hover:text-yellow-400 transition">
                {link.name}
              </a>
            ))}
          </nav>
        </div>
      )}
    </header>
  );
};

export default Header;
