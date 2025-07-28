import { useState } from "react";
import Tilt from "react-parallax-tilt";

const movies = [
  {
    id: 1,
    title: "Interstellar",
    image: "/images/interstellar.jpg",
    description: "Un viaje épico a través del espacio y el tiempo.",
    details: "En un futuro distópico, un grupo de astronautas viaja a través de un agujero de gusano en busca de un nuevo hogar para la humanidad.",
  },
  {
    id: 2,
    title: "Inception",
    image: "/images/inception.jpg",
    description: "Domina los sueños, desafía la realidad.",
    details: "Un ladrón que roba secretos a través del sueño debe realizar una tarea inversa: plantar una idea en la mente de su objetivo.",
  },
  {
    id: 3,
    title: "The Matrix",
    image: "/images/matrix.jpg",
    description: "¿Realidad o simulación? Tú decides.",
    details: "Un hacker descubre la verdad sobre su mundo: una simulación creada por máquinas para controlar a los humanos.",
  },
];

export default function MovieTiltGroup() {
  const [selectedMovie, setSelectedMovie] = useState(null);

  const openModal = (movie) => {
    setSelectedMovie(movie);
  };

  const closeModal = () => {
    setSelectedMovie(null);
  };

  return (
    <section className="w-full py-16 bg-black text-white relative">
      <div className="max-w-6xl mx-auto px-4">
        <h2 className="text-3xl md:text-4xl font-bold text-center mb-10">
          Destacados para ti 🎬
        </h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8 justify-items-center">
          {movies.map((movie) => (
            <Tilt
              key={movie.id}
              tiltMaxAngleX={15}
              tiltMaxAngleY={15}
              glareEnable={true}
              glareMaxOpacity={0.3}
              glareColor="#ffffff"
              glarePosition="all"
              className="relative w-[260px] h-[380px] rounded-xl overflow-hidden shadow-2xl transform transition duration-300 hover:scale-105 group bg-gray-900"
            >
              <img
                src={movie.image}
                alt={movie.title}
                className="w-full h-full object-cover group-hover:brightness-50 transition duration-300"
              />
              <div className="absolute bottom-0 w-full bg-black/60 text-center py-2 text-lg font-semibold z-10">
                {movie.title}
              </div>
              <div className="absolute inset-0 flex flex-col items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-20 px-4 text-center">
                <p className="text-sm mb-4">{movie.description}</p>
                <button
                  onClick={() => openModal(movie)}
                  className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-md transition"
                >
                  Ver más
                </button>
              </div>
            </Tilt>
          ))}
        </div>
      </div>

      {/* Modal */}
      {selectedMovie && (
        <div className="fixed inset-0 bg-black/80 flex items-center justify-center z-50 px-4">
          <div className="bg-white text-black max-w-md w-full rounded-xl shadow-lg p-6 relative">
            <button
              onClick={closeModal}
              className="absolute top-2 right-3 text-xl font-bold text-gray-600 hover:text-red-600"
            >
              ✕
            </button>
            <h3 className="text-2xl font-bold mb-2">{selectedMovie.title}</h3>
            <img
              src={selectedMovie.image}
              alt={selectedMovie.title}
              className="w-full h-48 object-cover rounded-md mb-4"
            />
            <p className="text-sm">{selectedMovie.details}</p>
          </div>
        </div>
      )}
    </section>
  );
}
