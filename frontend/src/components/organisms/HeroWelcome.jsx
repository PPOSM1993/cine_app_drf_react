// src/components/organisms/HeroWelcome.jsx
import { Canvas } from "@react-three/fiber"
import { OrbitControls } from "@react-three/drei"

export default function HeroWelcome() {
  return (
    <div className="h-[60vh] relative">
      <Canvas>
        <ambientLight intensity={0.5} />
        <directionalLight position={[0, 5, 5]} />
        <mesh rotation={[0.3, 0.5, 0]}>
          <torusKnotGeometry args={[1.2, 0.4, 100, 16]} />
          <meshStandardMaterial color="crimson" metalness={0.5} roughness={0.2} />
        </mesh>
        <OrbitControls enableZoom={false} />
      </Canvas>
      <div className="absolute inset-0 flex items-center justify-center bg-black/40">
        <h1 className="text-5xl font-bold text-white drop-shadow-lg">
          Bienvenido a CineWave 🎬
        </h1>
      </div>
    </div>
  )
}
