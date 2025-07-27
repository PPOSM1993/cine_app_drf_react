// HeaderBackground3D.jsx
import { Canvas, useFrame } from '@react-three/fiber'
import { useRef } from 'react'
import * as THREE from 'three'

function Particles() {
  const ref = useRef()
  const count = 150
  const positions = new Float32Array(count * 3).map(() => THREE.MathUtils.randFloatSpread(20))

  const particlesGeometry = new THREE.BufferGeometry()
  particlesGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3))

  useFrame(({ mouse }) => {
    ref.current.rotation.y += 0.001
    ref.current.rotation.x = mouse.y * 0.2
    ref.current.rotation.y = mouse.x * 0.2
  })

  return (
    <points ref={ref} geometry={particlesGeometry}>
      <pointsMaterial color="#D7263D" size={0.15} />
    </points>
  )
}

export default function HeaderBackground3D() {
  return (
    <Canvas camera={{ position: [0, 0, 10], fov: 75 }}>
      <ambientLight intensity={0.5} />
      <Particles />
    </Canvas>
  )
}
