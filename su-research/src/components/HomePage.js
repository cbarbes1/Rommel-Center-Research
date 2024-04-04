import React from 'react'; // Importing React to enable JSX syntax and component logic
import { Link } from 'react-router-dom'; // Importing Link component for client-side navigation between routes
//import VideoBackground2 from './VideoBackground2'; // Importing a custom video background component

// Defining a functional component named HomePage
const HomePage = () => {
  // The component returns JSX to render the homepage UI
  return (
    // A div container for the entire homepage, using TailwindCSS classes for styling
    <div className="min-h-screen bg-stone-100 text-suGold">
        {/*<VideoBackground2 /> {/* Embedding the custom video background component */}
      {/* Container div for content, centered with margin auto and padding for spacing */}
      <div className="container mx-auto px-4 py-8">
        {/* Header section containing the navigation bar */}
        <header className="mb-8 relative">
            {/* Navigation bar with TailwindCSS classes for background, text color, padding, rounded corners, shadow, and flexbox layout */}
            <nav className="bg-suMaroon text-white p-4 rounded-md shadow-md flex justify-between items-center">
                {/* Navigation link to the homepage, styled to stand out as the brand name */}
                <Link to="/" className="font-bold text-lg hover:bg-suMaroon-dark rounded p-2 transition-colors duration-200 text-suGold">Salisbury Research</Link>
                {/* Container for additional navigation links, spaced with a gap */}
                <div className="flex gap-4">
                {/* Individual navigation links, each with hover effects and transition for smooth color change */}
                <Link to="/" className="font-bold text-lg hover:bg-suMaroon-dark rounded p-2 transition-colors duration-200 text-suGold">Home</Link>
                <Link to="/topics" className="font-bold text-lg hover:bg-suMaroon-dark rounded p-2 transition-colors duration-200 text-suGold">Topic A-Z</Link>
                <Link to="/faculty" className="font-bold text-lg hover:bg-suMaroon-dark rounded p-2 transition-colors duration-200 text-suGold">Faculty Contact</Link>
                <Link to="/articles" className="font-bold text-lg hover:bg-suMaroon-dark rounded p-2 transition-colors duration-200 text-suGold">Articles A-Z</Link>
                </div>
            </nav>
        </header>
        {/* Main content section */}
        <main>
          {/* Section for the page title, with text centering and margin-bottom for spacing */}
          <section className="text-center mb-12 relative" style={{position: 'relative'}}>
            {/* Page title with gradient text effect and responsive font size */}
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold bg-clip-text"
                    style={{
                      backgroundImage: 'linear-gradient(to right, #8A0000, #FFC420)',
                      WebkitBackgroundClip: 'text',
                      WebkitTextFillColor: 'transparent'
                    }}>
                Salisbury Research
            </h1>
            <h2 className="mt-4 text-2xl font-black bg-clip-text text-white"
              style={{
                backgroundImage: 'linear-gradient(to right, #8A0000, #FFC420)',
                WebkitBackgroundClip: 'text',
                WebkitTextFillColor: 'transparent'
              }}>
              Dedicated to advancing knowledge and fostering academic excellence across disciplines.</h2>
          </section>
          {/* Section for displaying feature cards in a grid layout, responsive to screen size */}
          <section className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {/* Individual feature card with hover effect for shadow */}
            <div className="bg-suMaroon rounded-lg shadow-lg p-6 hover:shadow-2xl transition-dark-shadow">
              {/* Card title and description with specific font size, weight, and color */}
              <h2 className="text-2xl font-semibold text-suGold mb-4">Data</h2>
              <p className="text-suGold">See the raw data of what research Salisbury Professor's are doing.</p>
            </div>
            {/* Repeating the structure for other feature cards */}
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
        {/* Footer section with copyright notice and additional information */}
        <footer className="font-bold mt-12 bg-suMaroon text-suGold text-center p-4 rounded-md">
          <p>© {new Date().getFullYear()} Salisbury University Research. All rights reserved.</p>
          <p className="mt-2">Salisbury, Maryland, USA</p>
        </footer>
      </div>
    </div>
  );
};

export default HomePage; // Exporting the HomePage component for use in other parts of the application
