export default function AuthTemplate({ children }) {
  return (
    <div className="h-screen flex items-center justify-center bg-gradient-to-br from-blue-500 to-indigo-600">
      {children}
    </div>
  )
}
