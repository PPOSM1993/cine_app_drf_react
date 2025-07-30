import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import { WelcomePage, Login, Register, ForgorPassword, Home, PrivateRoute } from "../index";

export default function AppRouter() {
  return (
    <Routes>
      <Route path="/" element={<WelcomePage />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />

      {/*Estas son Rutas privadas o protegidas */}
      <Route path="/forgot_password" element={<ForgorPassword />} />
      <Route path="*" element={<Navigate to="/" />} />
      <Route path="/" element={<PrivateRoute />}>
        <Route path="home" element={<Home />} />
        {/* otras rutas privadas */}
      </Route>

    </Routes>
  );
}
