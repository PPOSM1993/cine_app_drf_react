import { Header, HeroWelcome, MovieCarrousel, MovieTiltGroup, UpcomingSlider, CategoriesGrid, PopularMovies, Footer } from '../../index'

const WelcomePage = () => {
  return (
    <div className="min-h-screen bg-white text-black">
      <Header />

      <main className="w-full">
        <HeroWelcome />
        <MovieCarrousel />
        <MovieTiltGroup />
        <div className="relative">
          <div className="absolute -top-12 left-1/2 -translate-x-1/2 w-[600px] h-[200px] rounded-full bg-pink-500 blur-3xl opacity-30 animate-pulse z-0" />
          <UpcomingSlider />
        </div>
        <div className="relative">
          <div className="absolute -top-8 left-[30%] w-[400px] h-[160px] bg-red-600 blur-[100px] opacity-20 rounded-full z-0" />
          <PopularMovies />
        </div>
        <div className="relative">
          <div className="absolute -top-8 left-[30%] w-[400px] h-[160px] bg-red-600 blur-[100px] opacity-20 rounded-full z-0" />
          <CategoriesGrid />
        </div>
      <div className="relative">

          <div className="absolute -top-8 left-[30%] w-[400px] h-[160px] bg-red-600 blur-[100px] opacity-20 rounded-full z-0" />
          <Footer />
        </div>
      </main>
    </div>
  );
};

export default WelcomePage;
