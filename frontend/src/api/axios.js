import axios from "axios";

const instance = axios.create({
  baseURL: "http://localhost:8000/api/authentication", // ajusta si tu backend usa otro puerto o subruta
  headers: {
    "Content-Type": "application/json",
  },
});

export default instance;
