import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import { WelcomePage, Login, Register, ForgorPassword } from "../index";

export default function AppRouter() {
  return (
    <Routes>
      <Route path="/" element={<WelcomePage />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />}/>
      <Route path="/forgot_password" element={<ForgorPassword />} />
      <Route path="*" element={<Navigate to="/" />} />
    </Routes>
  );
}
