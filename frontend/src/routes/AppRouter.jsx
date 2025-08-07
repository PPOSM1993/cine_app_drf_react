import React from "react"
import { Routes, Route, Navigate } from "react-router-dom"
import {
  WelcomePage,
  Home,
  PrivateRoute,
  Login
} from "../index"

export default function AppRouter() {
  return (
    <Routes>
      {/* 🔓 Rutas públicas */}
      <Route path="/" element={<WelcomePage />} />
      <Route path="/login" element={<Login />} />

      {/* 🔐 Rutas protegidas */}
      <Route element={<PrivateRoute />}>
        <Route path="/home" element={<Home />} />
        {/* Agrega aquí otras rutas privadas como /dashboard, /profile, etc. */}
      </Route>

      {/* Ruta catch-all */}
      <Route path="*" element={<Navigate to="/" />} />
    </Routes>
  )
}
