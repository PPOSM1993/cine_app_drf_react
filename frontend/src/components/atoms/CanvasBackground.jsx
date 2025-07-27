// src/components/atoms/CanvasBackground.jsx
import { useEffect, useRef } from 'react'
import * as THREE from 'three'

const CanvasBackground = () => {
  const mountRef = useRef()

  useEffect(() => {
    const scene = new THREE.Scene()
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000)
    const renderer = new THREE.WebGLRenderer({ alpha: true })
    renderer.setSize(window.innerWidth, window.innerHeight)
    mountRef.current.appendChild(renderer.domElement)

    const geometry = new THREE.TorusKnotGeometry(10, 3, 100, 16)
    const material = new THREE.MeshBasicMaterial({ color: 0x00ffff, wireframe: true })
    const knot = new THREE.Mesh(geometry, material)
    scene.add(knot)

    camera.position.z = 50

    const animate = () => {
      requestAnimationFrame(animate)
      knot.rotation.x += 0.01
      knot.rotation.y += 0.01
      renderer.render(scene, camera)
    }

    animate()

    return () => mountRef.current.removeChild(renderer.domElement)
  }, [])

  return <div ref={mountRef} className="absolute inset-0 z-0" />
}

export default CanvasBackground
