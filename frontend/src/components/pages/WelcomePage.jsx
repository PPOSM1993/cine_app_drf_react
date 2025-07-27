import { Header } from '../../index'

const WelcomePage = () => {
  return (
    <div className="min-h-screen bg-black text-white">
      <Header />

      <main className="pt-20 flex items-center justify-center h-[calc(100vh-80px)]">
        <h1 className="text-4xl font-bold">Bienvenido a CineWave</h1>
      </main>
    </div>
  );
};

export default WelcomePage;
