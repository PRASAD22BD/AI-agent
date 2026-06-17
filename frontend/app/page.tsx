export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-2">
      <h1 className="text-4xl font-bold">AI Job Application Agent</h1>
      <p className="mt-4 text-xl">Your personal AI recruiter and job search assistant.</p>
      
      <div className="mt-8 flex gap-4">
        <button className="px-6 py-3 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 transition">
          Get Started
        </button>
        <button className="px-6 py-3 border border-gray-300 rounded-lg font-semibold hover:bg-gray-50 transition">
          Learn More
        </button>
      </div>
    </div>
  );
}
