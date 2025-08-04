import { Canvas } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import { GalaxyParticles } from "../../index";
import { Link } from "react-router-dom";
import { authStore } from "../../index";

export default function HeroWelcome() {
  const { user } = authStore();

  return (
    <div className="h-screen w-full relative">
      <Canvas camera={{ position: [0, 0, 10], fov: 75 }}>
        <ambientLight intensity={0.5} />
        <directionalLight position={[5, 5, 5]} />
        <GalaxyParticles />
        <OrbitControls enableZoom={false} enableRotate={false} />
      </Canvas>

      <div className="absolute inset-0 flex flex-col items-center justify-center bg-black/20 px-4 text-center">
        <h1 className="text-4xl md:text-6xl font-bold text-black drop-shadow-xl">
          Bienvenido a PopCorn Cinema 🍿
        </h1>
        <p className="mt-4 text-lg md:text-xl text-black max-w-xl font-bold">
          Explora las mejores películas del universo, desde clásicos hasta lo último en cartelera.
        </p>

        {!user && (
          <div className="mt-8 flex gap-4">
            <Link
              to="/login"
              className="bg-red-600 hover:bg-red-700 text-white font-semibold py-2 px-4 rounded-md transition"
            >
              Iniciar sesión
            </Link>
            <Link
              to="/register"
              className="bg-green-600 hover:bg-green-700 text-white-700 font-semibold py-2 px-4 rounded-md transition"
            >
              Registrarse
            </Link>
          </div>
        )}
      </div>
    </div>
  );
}
