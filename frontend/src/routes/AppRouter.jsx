import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import { WelcomePage, Login } from "../index";

export default function AppRouter() {
  return (
    <Routes>
      <Route path="/" element={<WelcomePage />} />
      <Route path="/login" element={<Login />} />
      <Route path="*" element={<Navigate to="/" />} />
    </Routes>
  );
}
