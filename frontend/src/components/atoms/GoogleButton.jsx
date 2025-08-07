import { authStore } from '../../index'

export default function GoogleButton() {
  const loginWithGoogle = authStore((state) => state.loginWithGoogle)

  return (
    <button
      onClick={loginWithGoogle}
      className="bg-white text-gray-800 px-6 py-2 rounded shadow-md hover:bg-gray-100 flex items-center gap-2 w-fit mx-auto transition duration-200"
    >
      <img
        src="https://www.svgrepo.com/show/475656/google-color.svg"
        alt="Google"
        className="w-5 h-5"
      />
      <span>Iniciar sesión con Google</span>
    </button>
  )
}
