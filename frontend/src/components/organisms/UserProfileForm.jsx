import { useState } from 'react'
import { User, Mail, Phone, Calendar, IdCard } from 'lucide-react'
import HeaderUser from './HeaderUser'

const UserProfileForm = ({ user }) => {
  const [formData, setFormData] = useState({
    username: user.username || '',
    email: user.email || '',
    first_name: user.first_name || '',
    last_name: user.last_name || '',
    rut: user.rut || '',
    phone: user.phone || '',
    birthdate: user.birthdate || '',
  })

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData((prev) => ({ ...prev, [name]: value }))
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    console.log('Datos a enviar:', formData)
    // Aquí agregarías la lógica para actualizar el perfil vía API
  }

  return (
    <>
      <div className="max-w-4xl mx-auto bg-white shadow-lg rounded-2xl p-8 bg-gradient-to-br from-[#0f172a] to-[#1e293b] text-white">
        {/* Encabezado del perfil */}
        <HeaderUser username={formData.username} email={formData.email} />

        {/* Formulario */}
        <form onSubmit={handleSubmit} className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6">

          {/* Username */}
          <div className='text-white'>
            <label className="block text-sm font-semibold text-gray-700 mb-1 text-white py-2">
              Nombre de usuario
            </label>
            <div className="flex items-center border rounded-lg shadow-sm px-3 py-2">
              <User className="w-5 h-5 text-gray-400 mr-2" />
              <input
                type="text"
                name="username"
                value={formData.username}
                onChange={handleChange}
                className="w-full outline-none"
              />
            </div>
          </div>

          {/* Email */}
          <div>
            <label className="block text-sm font-semibold text-gray-700 mb-1 text-white py-2">
              Correo electrónico
            </label>
            <div className="flex items-center border rounded-lg shadow-sm px-3 py-2 bg-gray-100">
              <Mail className="w-5 h-5 text-gray-400 mr-2" />
              <input
                type="email"
                name="email"
                value={formData.email}
                disabled
                className="w-full bg-gray-100 outline-none cursor-not-allowed text-black"
              />
            </div>
          </div>

          {/* Nombre */}
          <div>
            <label className="block text-sm font-semibold text-gray-700 mb-1 text-white py-2">
              Nombre
            </label>
            <input
              type="text"
              name="first_name"
              value={formData.first_name}
              onChange={handleChange}
              className="w-full border rounded-lg shadow-sm px-3 py-2 outline-none"
            />
          </div>

          {/* Apellido */}
          <div>
            <label className="block text-sm font-semibold text-gray-700 mb-1 text-white py-2">
              Apellido
            </label>
            <input
              type="text"
              name="last_name"
              value={formData.last_name}
              onChange={handleChange}
              className="w-full border rounded-lg shadow-sm px-3 py-2 outline-none"
            />
          </div>

          {/* RUT */}
          <div>
            <label className="block text-sm font-semibold text-gray-700 mb-1 text-white py-2">
              RUT
            </label>
            <div className="flex items-center border rounded-lg shadow-sm px-3 py-2">
              <IdCard className="w-5 h-5 text-gray-400 mr-2" />
              <input
                type="text"
                name="rut"
                value={formData.rut}
                onChange={handleChange}
                className="w-full outline-none"
              />
            </div>
          </div>

          {/* Teléfono */}
          <div>
            <label className="block text-sm font-semibold text-gray-700 mb-1 text-white py-2">
              Teléfono
            </label>
            <div className="flex items-center border rounded-lg shadow-sm px-3 py-2">
              <Phone className="w-5 h-5 text-gray-400 mr-2" />
              <input
                type="text"
                name="phone"
                value={formData.phone}
                onChange={handleChange}
                className="w-full outline-none"
              />
            </div>
          </div>

          {/* Fecha de nacimiento */}
          <div>
            <label className="block text-sm font-semibold text-gray-700 mb-1 text-white py-2">
              Fecha de Nacimiento
            </label>
            <div className="flex items-center border rounded-lg shadow-sm px-3 py-2">
              <Calendar className="w-5 h-5 text-gray-400 mr-2 text-white" />
              <input
                type="date"
                name="birthdate"
                value={formData.birthdate || ''}
                onChange={handleChange}
                className="w-full outline-none text-white"
              />
            </div>
          </div>

          {/* Botón */}
          <div className="md:col-span-2 flex justify-end">
            <button
              type="submit"
              className="px-6 py-2 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition"
            >
              Guardar cambios
            </button>
          </div>
        </form>
      </div>
    </>

  )
}

export default UserProfileForm
