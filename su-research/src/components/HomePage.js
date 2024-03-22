import React from 'react';
import { Link } from 'react-router-dom';
import VideoBackground2 from './VideoBackground2';

const HomePage = () => {
  return (
    <div className="min-h-screen bg-zinc-300 text-suGold">
        <VideoBackground2 />
      <div className="container mx-auto px-4 py-8">
        <header className="mb-8 z-20 relative">
            <nav className="bg-suMaroon text-white p-4 rounded-md shadow-md flex justify-between items-center">
                <Link to="/" className="font-bold text-lg hover:bg-suGold rounded p-2 transition-colors duration-200 text-suGold">Salisbury Research</Link>
                <div className="flex gap-4">
                <Link to="/" className="font-bold text-lg hover:bg-suMaroon-dark rounded p-2 transition-colors duration-200 text-suGold">Home</Link>
                <Link to="/topics" className="font-bold text-lg hover:bg-suMaroon-dark rounded p-2 transition-colors duration-200 text-suGold">Topic A-Z</Link>
                <Link to="/faculty" className="font-bold text-lg hover:bg-suMaroon-dark rounded p-2 transition-colors duration-200 text-suGold">Faculty Contact</Link>
                <Link to="/articles" className="font-bold text-lg hover:bg-suMaroon-dark rounded p-2 transition-colors duration-200 text-suGold">Articles A-Z</Link>
                </div>
            </nav>
        </header>
        <main>
          <section className="text-center mb-12 z-30 relative" style={{position: 'relative'}}>
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold bg-clip-text text-transparent"
                style={{
                    backgroundImage: 'linear-gradient(to right, #D2122E 28%, yellow 72%)',
                    WebkitBackgroundClip: 'text',
                    WebkitTextFillColor: 'transparent'
                }}>
                Salisbury Research
            </h1>
            <h2 className="mt-4 text-2xl font-black bg-clip-text text-white"              
                // style={{
                //     backgroundImage: 'linear-gradient(to right, #D2122E 28%, yellow 72%)',
                //     WebkitBackgroundClip: 'text',
                //     WebkitTextFillColor: 'transparent'
                // }}>
                >Dedicated to advancing knowledge and fostering academic excellence across disciplines.</h2>
          </section>
          <section className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 z-30 relative">
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
        <footer className="font-bold mt-12 bg-suMaroon text-suGold text-center p-4 rounded-md z-20 relative">
          <p>© {new Date().getFullYear()} Salisbury University Research. All rights reserved.</p>
          <p className="mt-2">Salisbury, Maryland, USA</p>
        </footer>
      </div>
    </div>
  );
};

export default HomePage;
