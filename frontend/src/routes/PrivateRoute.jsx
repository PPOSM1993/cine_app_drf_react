import { Navigate, Outlet } from "react-router-dom"
import { authStore } from "../index"

export default function PrivateRoute() {
  const isAuthenticated = authStore((state) => state.isAuthenticated)
  return isAuthenticated ? <Outlet /> : <Navigate to="/login" replace />
}
