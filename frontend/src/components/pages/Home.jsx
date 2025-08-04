import { Header, HeaderUser } from "../../index";

export default function Home() {


  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-[#0f172a] to-[#1e293b] text-white px-4">
      <HeaderUser />
      <h1 className="text-4xl font-bold mb-4">Bienvenido al sistema 🎬</h1>
      <p className="mb-6 text-center max-w-md">
        Has iniciado sesión correctamente. Esta es una página de prueba para validar la autenticación.
      </p>


    </div>
  );
}
