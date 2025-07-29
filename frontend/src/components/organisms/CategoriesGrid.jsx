
const categories = [
  { name: "Acción", color: "bg-red-600", icon: "🔥" },
  { name: "Comedia", color: "bg-yellow-400", icon: "😂" },
  { name: "Terror", color: "bg-purple-800", icon: "👻" },
  { name: "Animación", color: "bg-pink-500", icon: "🎨" },
  { name: "Documental", color: "bg-green-500", icon: "🎥" },
  { name: "Romance", color: "bg-rose-500", icon: "💘" },
];

export default function CategoriesGrid() {
  const handleCategoryClick = (category) => {
    console.log(`Filtrar por categoría: ${category}`);
    // Aquí puedes conectar tu lógica de filtro si usas Zustand, Context, Router, etc.
  };

  return (
    <section className="relative w-full py-16 bg-gradient-to-b from-black via-gray-900 to-black text-white overflow-hidden">
      {/* Blur decorativo de fondo */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[300px] rounded-full bg-pink-500 opacity-10 blur-[120px] z-0 pointer-events-none" />

      <h2 className="text-3xl font-bold text-center mb-10 z-10 relative">🎬 Categorías</h2>

      <div className="flex flex-wrap justify-center gap-4 px-6 z-10 relative">
        {categories.map((cat, index) => (
          <div
            key={cat.name}
            onClick={() => handleCategoryClick(cat.name)}
            className={`${cat.color} px-5 py-2 rounded-full text-md font-semibold hover:scale-105 hover:shadow-[0_0_15px_rgba(255,255,255,0.3)] transition-transform duration-300 cursor-pointer shadow-md animate-fade-in-up`}
            style={{ animationDelay: `${index * 0.1}s`, animationFillMode: "both" }}
          >
            {cat.icon} {cat.name}
          </div>
        ))}
      </div>
      <br />
      <br />
    </section>
  );
}
