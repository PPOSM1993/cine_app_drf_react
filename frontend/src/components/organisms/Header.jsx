import { useState } from "react";
import { Menu, X } from "lucide-react";
import { Link } from "react-router-dom";
import { LogoWithText } from "../../index";


export default function Header() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <header className="fixed top-0 left-0 w-full z-50 bg-gradient-to-br from-[#0f172a] to-[#1e293b] backdrop-blur-md text-white transition-all duration-300">
      <div className="max-w-7xl mx-auto px-2 py-4 flex justify-between items-center">
        <div className="flex items-center gap-4">
          <LogoWithText />
        </div>

        <nav className="hidden md:flex items-center space-x-6">
        </nav>


      </div>

      {/* Menú móvil */}
      {isOpen && (
        <div className="fixed inset-0 z-40">
          <div
            className="absolute inset-0 bg-[#F0F0F0] bg-opacity-40 backdrop-blur-sm"
            onClick={() => setIsOpen(false)}
          />
          <div className="absolute top-0 right-0 h-screen w-full sm:w-[95%] bg-gradient-to-br from-[#0f172a] to-[#1e293b] text-white z-50 shadow-lg animate-slide-in-right overflow-y-auto">
            <div className="flex flex-col h-full">
              <div className="flex justify-end p-4">
                <button className="text-[#D7263D]" onClick={() => setIsOpen(false)}>
                  <X size={28} />
                </button>
              </div>
              <nav className="flex flex-col flex-grow px-6 pb-6 space-y-6 scroll-invisible">

              </nav>
            </div>
          </div>
        </div>
      )}
    </header>
  );
}
