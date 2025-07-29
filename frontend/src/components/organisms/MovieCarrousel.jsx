import { useRef } from "react";
import { ChevronLeft, ChevronRight } from "lucide-react";
import MovieCard from "../molecules/MovieCard";

const movies = [
  { title: "Interstellar", image: "/images/interstellar.jpg" },
  { title: "Inception", image: "/images/inception.jpg" },
  { title: "Dune", image: "/images/dune.jpg" },
  { title: "Blade Runner", image: "/images/blade.jpg" },
  { title: "Matrix", image: "/images/matrix.jpg" },
  { title: "Oppenheimer", image: "/images/oppenheimer.jpg" },
  { title: "Iron Man", image: "/images/ironman.jpg" },
];

export default function MovieCarrousel() {
  const scrollRef = useRef(null);

  const scroll = (direction) => {
    if (!scrollRef.current) return;
    const container = scrollRef.current;
    const scrollAmount = container.clientWidth * 0.7;
    container.scrollBy({ left: direction === "left" ? -scrollAmount : scrollAmount, behavior: "smooth" });
  };

  return (
    <section className="relative w-full py-20 bg-gradient-to-b from-black via-gray-900 to-black text-white overflow-hidden">
      <div className="container mx-auto px-4">
        <h2 className="text-3xl font-bold text-white mb-6 text-center">Películas Destacadas</h2>

        <div className="relative">
          {/* Botón izquierdo */}
          <button
            onClick={() => scroll("left")}
            className="hidden md:flex absolute left-0 top-1/2 -translate-y-1/2 z-10 p-2 bg-black/60 hover:bg-black/80 text-white rounded-full"
          >
            <ChevronLeft size={28} />
          </button>

          {/* Carrusel */}
          <div
            ref={scrollRef}
            className="flex gap-6 overflow-x-auto scrollbar-hide scroll-smooth pb-4 px-1"
          >
            {movies.map((movie, index) => (
              <MovieCard key={index} title={movie.title} image={movie.image} />
            ))}
          </div>

          {/* Botón derecho */}
          <button
            onClick={() => scroll("right")}
            className="hidden md:flex absolute right-0 top-1/2 -translate-y-1/2 z-10 p-2 bg-black/60 hover:bg-black/80 text-white rounded-full"
          >
            <ChevronRight size={28} />
          </button>
        </div>
      </div>
    </section>
  );
}
