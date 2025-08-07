// src/api/axios.js
import axios from "axios"

const instance = axios.create({
  baseURL: "http://localhost:8000/api/authentication/", // << correcto
  headers: {
    "Content-Type": "application/json",
  },
  withCredentials: true, // ✅ necesario si usas cookies
})

export default instance
