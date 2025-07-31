// src/components/molecules/LogoWithText.jsx
import logo from '../../assets/logo.png'; // cambia según la ruta real

const LogoWithText = () => {
  return (
  <div className="flex items-center space-x-1 cursor-pointer">
    <img src={logo} alt="Logo Cine" className="h-10 w-auto" />
    <span className="text-xl font-bold text-white tracking-wide">PopCorn Cinema</span>
  </div>
  );
};

export default LogoWithText;
