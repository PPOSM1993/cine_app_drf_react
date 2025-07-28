import Tilt from 'react-parallax-tilt';

export default function MovieCard({ image, title }) {
  return (
    <Tilt
      glareEnable={true}
      glareMaxOpacity={0.2}
      scale={1.05}
      transitionSpeed={1500}
      className="w-56 min-w-[14rem] h-80 bg-white rounded-xl shadow-lg overflow-hidden cursor-pointer"
    >
      <img
        src={image}
        alt={title}
        className="w-full h-4/5 object-cover"
      />
      <div className="p-2 text-center">
        <h3 className="text-lg font-semibold text-gray-800">{title}</h3>
      </div>
    </Tilt>
  );
}
