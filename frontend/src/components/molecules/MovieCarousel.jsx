// src/components/molecules/MovieCarousel.jsx
import "keen-slider/keen-slider.min.css"
import { useKeenSlider } from "keen-slider/react"

const movies = [
  { title: "Interestelar", image: "/assets/interestelar.jpg" },
  { title: "Dune", image: "/assets/dune.jpg" },
  { title: "Oppenheimer", image: "/assets/oppenheimer.jpg" },
]

export default function MovieCarousel() {
  const [sliderRef] = useKeenSlider({ loop: true, slides: { perView: 1 } })

  return (
    <div ref={sliderRef} className="keen-slider">
      {movies.map((movie, i) => (
        <div key={i} className="keen-slider__slide">
          <img
            src={movie.image}
            alt={movie.title}
            className="w-full h-[400px] object-cover rounded-xl"
          />
        </div>
      ))}
    </div>
  )
}
