
import { LogoWithText, HeaderBackground3D } from "../../index";

export default function Header() {

  return (
    <header className="fixed top-0 left-0 w-full z-50 bg-gradient-to-br from-[#0f172a] to-[#1e293b] backdrop-blur-md text-white transition-all duration-300">

      <div className="max-w-7xl mx-auto px-2 py-4 flex justify-between items-center">
        {/* Logo a la izquierda */}
        <div className="flex items-center gap-4">
          <LogoWithText />
        </div>

        </div>
    </header>
  );
}