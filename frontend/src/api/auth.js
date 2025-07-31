import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/authentication/'; // Asegúrate de que esta ruta esté bien

export const loginUser = async (username, password) => {
  try {
    const response = await axios.post(`${API_BASE_URL}login/`, {
      username,
      password
    });
    return response.data;
  } catch (error) {
    if (error.response && error.response.data) {
      throw error.response.data;
    }
    throw error;
  }
};

export const registerUser = async (formData) => {
  return await axios.post(`${API_BASE_URL}register/`, formData);
};