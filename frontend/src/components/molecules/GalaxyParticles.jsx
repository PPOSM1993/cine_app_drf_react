import { useRef } from "react";
import { useFrame } from "@react-three/fiber";
import * as THREE from "three";

export default function GalaxyParticles() {
  const particlesRef = useRef();

  const particlesCount = 2000;
  const positions = new Float32Array(particlesCount * 3);

  for (let i = 0; i < particlesCount * 3; i++) {
    positions[i] = (Math.random() - 0.5) * 40;
  }

  const geometry = new THREE.BufferGeometry();
  geometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));

  useFrame(() => {
    particlesRef.current.rotation.y += 0.0009;
  });

  return (
    <points ref={particlesRef} geometry={geometry}>
      <pointsMaterial size={0.1} color="#ffffff" sizeAttenuation depthWrite={false} />
    </points>
  );
}
