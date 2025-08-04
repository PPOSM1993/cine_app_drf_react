import React from "react"
import { Routes, Route, Navigate } from "react-router-dom"
import {
  WelcomePage,
  Login,
  Register,
  ForgorPassword,
  Home,
  PrivateRoute,
  Profile
} from "../index"

export default function AppRouter() {
  return (
    <Routes>
      {/* 🔓 Rutas públicas */}
      <Route path="/" element={<WelcomePage />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/forgot_password" element={<ForgorPassword />} />

      {/* 🔐 Rutas protegidas */}
      <Route element={<PrivateRoute />}>
        <Route path="/home" element={<Home />} />
        <Route path="/profile" element={<Profile />} />
        {/* Agrega aquí otras rutas privadas como /dashboard, /profile, etc. */}
      </Route>

      {/* Ruta catch-all */}
      <Route path="*" element={<Navigate to="/" />} />
    </Routes>
  )
}
