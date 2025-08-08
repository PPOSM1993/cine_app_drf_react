import { UserProfileForm, authStore } from '../../index'

const Profile = () => {
  const { user } = authStore()

  console.log("Usuario desde el store:", user) // 👈 verifica esto

  if (!user) {
    return <div className="p-6 text-center text-gray-600">Cargando perfil...</div>
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-[#0f172a] to-[#1e293b] px-4 py-20">
      <h1 className="text-2xl font-bold mb-4 text-white py-5">Perfil de Usuario</h1>
      <UserProfileForm user={user} />
    </div>
  )
}

export default Profile
