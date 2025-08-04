import { useState } from 'react'

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
    // Aquí puedes agregar la lógica para actualizar el perfil vía API
    console.log('Datos a enviar:', formData)
  }

  return (
    <form onSubmit={handleSubmit} className="grid grid-cols-1 md:grid-cols-2 gap-6">
      {/* Username */}
      <div>
        <label className="block text-sm font-medium">Nombre de usuario</label>
        <input
          type="text"
          name="username"
          value={formData.username}
          onChange={handleChange}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
        />
      </div>

      {/* Email */}
      <div>
        <label className="block text-sm font-medium">Correo electrónico</label>
        <input
          type="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
          disabled
        />
      </div>

      {/* First Name */}
      <div>
        <label className="block text-sm font-medium">Nombre</label>
        <input
          type="text"
          name="first_name"
          value={formData.first_name}
          onChange={handleChange}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
        />
      </div>

      {/* Last Name */}
      <div>
        <label className="block text-sm font-medium">Apellido</label>
        <input
          type="text"
          name="last_name"
          value={formData.last_name}
          onChange={handleChange}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
        />
      </div>

      {/* RUT */}
      <div>
        <label className="block text-sm font-medium">RUT</label>
        <input
          type="text"
          name="rut"
          value={formData.rut}
          onChange={handleChange}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
        />
      </div>

      {/* Teléfono */}
      <div>
        <label className="block text-sm font-medium">Teléfono</label>
        <input
          type="text"
          name="phone"
          value={formData.phone}
          onChange={handleChange}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
        />
      </div>

      {/* Fecha de nacimiento */}
      <div>
        <label className="block text-sm font-medium">Fecha de nacimiento</label>
        <input
          type="date"
          name="birthdate"
          value={formData.birthdate || ''}
          onChange={handleChange}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
        />
      </div>

      {/* Botón */}
      <div className="md:col-span-2">
        <button
          type="submit"
          className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
        >
          Guardar cambios
        </button>
      </div>
    </form>
  )
}

export default UserProfileForm
