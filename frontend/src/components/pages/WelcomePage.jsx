import { Header, HeroWelcome, MovieCarrousel, MovieTiltGroup, UpcomingSlider, CategoriesGrid } from '../../index'

const WelcomePage = () => {
  return (
    <div className="min-h-screen bg-white text-black ">
      <Header />

      <main className="w-full">
        <HeroWelcome />
        <MovieCarrousel />
        <MovieTiltGroup />
        <UpcomingSlider />
        <CategoriesGrid />
      </main>
    </div>
  );
};

export default WelcomePage;
