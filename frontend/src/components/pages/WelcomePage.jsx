import { Header } from '../../index'

const WelcomePage = () => {
  return (
    <div className="min-h-screen bg-white text-black ">
      <Header />

      <main className="pt-20 flex items-center justify-center h-[calc(100vh-80px)] bg-cinema">
        <h1 className="text-4xl font-bold text-center">Bienvenido a CineWave</h1>
      </main>
    </div>
  );
};

export default WelcomePage;
