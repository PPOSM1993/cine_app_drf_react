import { useRef } from 'react';
import { ChevronLeft, ChevronRight } from "lucide-react";

const upcomingMovies = [
    {
        id: 1,
        title: "Deadpool & Wolverine",
        image: "/images/deadpool.jpg",
        releaseDate: "25 Julio 2025",
        tag: "Preventa",
    },
    {
        id: 2,
        title: "Avatar 3",
        image: "/images/avatar3.jpg",
        releaseDate: "18 Diciembre 2025",
        tag: "Próximo estreno",
    },
    {
        id: 3,
        title: "Intensamente 2",
        image: "/images/insideout2.jpg",
        releaseDate: "8 Agosto 2025",
        tag: "Estreno especial",
    },
    {
        id: 4,
        title: "Dune: Parte 3",
        image: "/images/dune3.jpg",
        releaseDate: "Marzo 2026",
        tag: "Muy pronto",
    },
        {
        id: 5,
        title: "Dune: Parte 3",
        image: "/images/dune3.jpg",
        releaseDate: "Marzo 2026",
        tag: "Muy pronto",
    },
];


export default function UpcomingSlider() {
    const sliderRef = useRef();

    const scroll = (direction) => {
        const { current } = sliderRef;
        if (!current) return;
        const scrollAmount = 300;
        current.scrollBy({
            left: direction === "left" ? -scrollAmount : scrollAmount,
            behavior: "smooth",
        });
    };

    return (
        <section className="relative w-full py-16 bg-gradient-to-b from-black via-gray-900 to-black text-white overflow-hidden ">
            <div className='max-w-6xl mx-auto px-4'>
                <h2 className="text-3xl md:text-4xl text-white font-bold text-center mb-6">
                    🎟️ Preventa y Próximos Estrenos
                </h2>
                <div className="relative">
                    {/* Botón Prev */}

                    <button
                        onClick={() => scroll("left")}
                        className="absolute left-2 top-1/2 transform -translate-y-1/2 z-10 bg-white/10 hover:bg-white/20 p-1.5 rounded-full text-white"
                    >
                        <ChevronLeft className="w-6 h-6" />
                    </button>

                    <button
                        onClick={() => scroll("right")}
                        className="absolute right-2 top-1/2 transform -translate-y-1/2 z-10 bg-white/10 hover:bg-white/20 p-1.5 rounded-full text-white"
                    >
                        <ChevronRight className="w-6 h-6" />
                    </button>

                    <div className="overflow-x-auto scrollbar-hide px-6" ref={sliderRef}>
                        <div className="flex space-x-6 snap-x snap-mandatory scroll-smooth">
                            {upcomingMovies.map((movie) => (
                                <div
                                    key={movie.id}
                                    className="min-w-[240px] snap-center shrink-0 bg-gray-900 rounded-xl overflow-hidden shadow-lg hover:scale-105 transition duration-300"
                                >
                                    <img
                                        src={movie.image}
                                        alt={movie.title}
                                        className="w-full h-64 object-cover"
                                    />
                                    <div className="p-4">
                                        <span className="text-xs text-red-500 font-bold uppercase">
                                            {movie.tag}
                                        </span>
                                        <h3 className="text-white text-lg font-semibold mt-1">
                                            {movie.title}
                                        </h3>
                                        <p className="text-gray-400 text-sm">{movie.releaseDate}</p>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
}