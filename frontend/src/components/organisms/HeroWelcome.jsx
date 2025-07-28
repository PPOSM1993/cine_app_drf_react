import { Canvas } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import { GalaxyParticles } from "../../index";

export default function HeroWelcome() {
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
      </div>
    </div>
  );
}
