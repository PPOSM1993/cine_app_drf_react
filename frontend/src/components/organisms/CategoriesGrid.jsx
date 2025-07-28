const categories = [
  { name: "Acción", color: "bg-red-600", icon: "🔥" },
  { name: "Comedia", color: "bg-yellow-400", icon: "😂" },
  { name: "Terror", color: "bg-purple-800", icon: "👻" },
  { name: "Animación", color: "bg-pink-500", icon: "🎨" },
  { name: "Documental", color: "bg-green-500", icon: "🎥" },
  { name: "Romance", color: "bg-rose-500", icon: "💘" },
];

export default function CategoriesGrid() {
  return (
    <section className="w-full py-12 bg-gradient-to-b from-black via-gray-900 to-black text-white">
      <h2 className="text-3xl font-bold text-center mb-8">🎬 Categorías</h2>
      <div className="flex flex-wrap justify-center gap-4 px-4">
        {categories.map((cat) => (
          <div
            key={cat.name}
            className={`${cat.color} px-5 py-2 rounded-full text-md font-semibold hover:scale-105 transition transform cursor-pointer shadow-md`}
          >
            {cat.icon} {cat.name}
          </div>
        ))}
      </div>
    </section>
  );
}
