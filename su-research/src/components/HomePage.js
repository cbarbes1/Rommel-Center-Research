import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
  return (
    <div className="min-h-screen bg-zinc-300 text-suGold">
      <div className="container mx-auto px-4 py-8">
        <header className="mb-8">
          <nav className="bg-suMaroon text-white p-4 rounded-md shadow-md flex justify-between items-center">
            <a href="/" className="font-bold text-lg hover:bg-suGold rounded p-2 transition-colors duration-200 text-suGold">Salisbury Research</a>
            <div className="flex gap-4">
              <a href="/" className="font-bold text-lg hover:bg-suMaroon-dark rounded p-2 transition-colors duration-200 text-suGold">Home</a>
              <Link to="/topics" className="font-bold text-lg hover:bg-suMaroon-dark rounded p-2 transition-colors duration-200 text-suGold">Topics</Link>
              <a href="/faculty" className="font-bold text-lg hover:bg-suMaroon-dark rounded p-2 transition-colors duration-200 text-suGold">Faculty</a>
              <a href="/articles" className="font-bold text-lg hover:bg-suMaroon-dark rounded p-2 transition-colors duration-200 text-suGold">Articles</a>
            </div>
          </nav>
        </header>
        <main>
          <section className="text-center mb-12">
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold bg-clip-text text-transparent"
                style={{
                    backgroundImage: 'linear-gradient(to right, #8A0000 28%, #FFC420 72%)',
                    WebkitBackgroundClip: 'text',
                    WebkitTextFillColor: 'transparent'
                }}>
                Salisbury Research
            </h1>
            <p className="mt-4 text-lg text-gray-600">Dedicated to advancing knowledge and fostering academic excellence across disciplines.</p>
          </section>
          <section className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div className="bg-suMaroon rounded-lg shadow-lg p-6 hover:shadow-2xl transition-dark-shadow">
              <h2 className="text-2xl font-semibold text-suGold mb-4">Data</h2>
              <p className="text-suGold">See the raw data of what reserach Salisbury Professor's are doing.</p>
            </div>
            <div className="bg-suMaroon rounded-lg shadow-lg p-6 hover:shadow-2xl transition-dark-shadow">
              <h2 className="text-2xl font-semibold text-suGold mb-4">Academic Programs</h2>
              <p className="text-suGold">Offering a diverse range of programs that promote in-depth learning and research opportunities.</p>
            </div>
            <div className="bg-suMaroon rounded-lg shadow-lg p-6 hover:shadow-2xl transition-dark-shadow">
              <h2 className="text-2xl font-semibold text-suGold mb-4">Looking to work with our Researchers?</h2>
              <p className="text-suGold">At SU we have a plethora of talented researchers who are experts in their field. If you need help with something you're doing find out how to reach our here.</p>
            </div>
          </section>
        </main>
        <footer className="font-bold mt-12 bg-suMaroon text-suGold text-center p-4 rounded-md">
          <p>© {new Date().getFullYear()} Salisbury University Research. All rights reserved.</p>
          <p className="mt-2">Salisbury, Maryland, USA</p>
        </footer>
      </div>
    </div>
  );
};

export default HomePage;
