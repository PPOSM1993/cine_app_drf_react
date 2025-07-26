import GoogleButton from '../atoms/GoogleButton'

export default function LoginBox() {
  return (
    <div className="bg-white p-8 rounded shadow-lg text-center w-80">
      <h1 className="text-2xl font-bold mb-6 text-gray-800">Bienvenido a CineWave 🎬</h1>
      <GoogleButton />
    </div>
  )
}
