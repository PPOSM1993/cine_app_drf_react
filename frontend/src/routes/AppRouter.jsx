// AppRouter.jsx
import { Routes, Route, Navigate } from "react-router-dom"
import { authStore } from "../index"
import {
  WelcomePage,
  Home,
  PrivateRoute,
  Login
} from "../index"

export default function AppRouter() {
  const isAuthenticated = authStore((state) => state.isAuthenticated)

  return (
    <Routes>
      {/* 🔓 Rutas públicas */}
      <Route path="/" element={<WelcomePage />} />
      <Route
        path="/login"
        element={isAuthenticated ? <Navigate to="/home" /> : <Login />}
      />

      {/* 🔐 Rutas protegidas */}
      <Route element={<PrivateRoute />}>
        <Route path="/home" element={<Home />} />
      </Route>

      {/* Ruta catch-all */}
      <Route path="*" element={<Navigate to="/" />} />
    </Routes>
  )
}
