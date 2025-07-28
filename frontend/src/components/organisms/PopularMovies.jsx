// src/components/organisms/PopularMovies.jsx
export default function PopularMovies() {
  const movies = [
    {
      id: 1,
      title: "El Conjuro 4",
      image: "/conjuro.jpg",
      rating: "⭐ 8.4",
      tag: "Terror",
    },
    // + más
  ];

  return (
    <section className="w-full py-12 bg-black text-white">
      <h2 className="text-3xl font-bold text-center mb-6">🔥 Más Vistas</h2>
      <div className="grid grid-cols-2 md:grid-cols-4 gap-6 px-6">
        {movies.map((movie) => (
          <div
            key={movie.id}
            className="bg-gray-900 rounded-lg overflow-hidden shadow-md hover:scale-105 transition duration-300"
          >
            <img src={movie.image} alt={movie.title} className="h-48 w-full object-cover" />
            <div className="p-3">
              <span className="text-sm text-red-400">{movie.tag}</span>
              <h3 className="font-semibold">{movie.title}</h3>
              <p className="text-xs text-gray-400">{movie.rating}</p>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
