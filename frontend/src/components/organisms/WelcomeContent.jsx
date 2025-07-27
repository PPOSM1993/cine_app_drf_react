// src/components/organisms/WelcomeContent.jsx

import { MovieCarousel, Button } from '../../index'

export default function WelcomeContent() {
  return (
    <section className="px-8 py-12">
      <MovieCarousel />
      <div className="mt-10 flex justify-center">
        <Button text="Explorar Cartelera" />
      </div>
    </section>
  )
}
