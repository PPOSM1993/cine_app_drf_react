import {
  Header,
  HeroWelcome,
  MovieCarrousel,
  MovieTiltGroup,
  UpcomingSlider,
  CategoriesGrid,
  PopularMovies,
  Footer
} from '../../index';

const WelcomePage = () => {
  return (
    <div className="bg-white text-black">
      <Header />

      {/* Agregado padding-top para compensar el header fijo */}
      <main className="w-full pt-1 md:pt-1">
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
