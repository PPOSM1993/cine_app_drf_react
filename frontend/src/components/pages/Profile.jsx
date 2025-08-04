import { UserProfileForm, authStore } from '../../index'

const Profile = () => {
  const { user } = authStore()

  console.log("Usuario desde el store:", user) // 👈 verifica esto

  if (!user) {
    return <div className="p-6 text-center text-gray-600">Cargando perfil...</div>
  }

  return (
    <div className="max-w-4xl mx-auto p-6">
      <h1 className="text-2xl font-bold mb-4">Perfil de Usuario</h1>
      <UserProfileForm user={user} />
    </div>
  )
}

export default Profile
