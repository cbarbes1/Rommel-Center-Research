import React, { useState, useEffect } from 'react'; // Importing React hooks: useState for state management, useEffect for side effects
import { Link } from 'react-router-dom'; // Importing Link component from react-router-dom for navigation without page reload
//import VideoBackground from './VideoBackground'; // Importing a custom VideoBackground component

// Defining the TopicPage functional component
const TopicPage = () => {
  // useState hook to manage 'topics' state, initially an empty array
  const [topics, setTopics] = useState([]); 
  // useState hook to manage 'isLoading' state, initially true indicating data is being loaded
  const [isLoading, setIsLoading] = useState(true);
  // useState hook to manage 'openDropdowns' state, initially an empty object to track which dropdowns are open
  const [openDropdowns, setOpenDropdowns] = useState({}); 

  // useEffect hook to fetch topics data on component mount
  useEffect(() => {
    // Defining an asynchronous function to fetch topics data
    const fetchTopics = async () => {
      setIsLoading(true); // Setting isLoading to true before fetching data
      try {
        const response = await fetch('/processed_category_data.json'); // Fetching data from the server
        const data = await response.json(); // Parsing the JSON response
        // Sorting the fetched topics alphabetically by their keys
        const sortedTopics = Object.entries(data).sort((a, b) => a[0].localeCompare(b[0]));
        setTopics(sortedTopics); // Updating the 'topics' state with the sorted topics
      } catch (error) {
        console.error('Failed to fetch topics:', error); // Logging any errors to the console
      } finally {
        setIsLoading(false); // Setting isLoading to false after fetching data
      }
    };

    fetchTopics(); // Calling the fetchTopics function
  }, []); // The empty dependency array ensures this effect runs only once after the initial render

  // Function to toggle the state of dropdowns
  const toggleDropdown = (categoryName, type) => {
    setOpenDropdowns(prevState => ({
      ...prevState,
      [`${categoryName}-${type}`]: !prevState[`${categoryName}-${type}`] // Toggling the boolean value for the specified dropdown
    }));
  };

  // Function to render the details of a topic based on its key
  const renderDetail = (key, value) => {
    let text = '';
    switch (key) {
      case 'faculty_count':
        text = `${value} Faculty`; // Formatting text for faculty count
        break;
      case 'article_count':
        text = `${value} Articles`; // Formatting text for article count
        break;
      case 'department_count':
        // Intentionally left blank for future implementation
        break;
      default:
        // Handling default case, joining array values with commas or returning the value directly
        text = Array.isArray(value) ? value.join(', ') : value;
    }
    return text; // Returning the formatted text
  };
    
  // Rendering the TopicPage component
  return (
    <div className="min-h-screen bg-stone-100 text-suGold">
        {/*<VideoBackground /> {/* Rendering the VideoBackground component */}
        <div className="container mx-auto px-4 py-8">
            {/* Header section with navigation links */}
            <header className="mb-8">
            <nav className="bg-suMaroon text-white p-4 rounded-md shadow-md flex justify-between items-center">
                {/* Navigation links using the Link component for SPA navigation */}
                <Link to="/" className="font-bold text-lg hover:bg-suMaroon-dark rounded p-2 transition-colors duration-200 text-suGold">Salisbury Research</Link>
                <div className="flex gap-4">
                {/* Additional navigation links */}
                <Link to="/" className="font-bold text-lg hover:bg-suMaroon-dark rounded p-2 transition-colors duration-200 text-suGold">Home</Link>
                <Link to="/topics" className="font-bold text-lg hover:bg-suMaroon-dark rounded p-2 transition-colors duration-200 text-suGold">Topic A-Z</Link>
                <Link to="/faculty" className="font-bold text-lg hover:bg-suMaroon-dark rounded p-2 transition-colors duration-200 text-suGold">Faculty Contact</Link>
                <Link to="/articles" className="font-bold text-lg hover:bg-suMaroon-dark rounded p-2 transition-colors duration-200 text-suGold">Articles A-Z</Link>
                </div>
            </nav>
            </header>
            {/* Main content section */}
            <main>
            {/* Section for the page title */}
            <section className="text-center mb-12 ">
                <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold bg-clip-text"
                    style={{
                      backgroundImage: 'linear-gradient(to right, #8A0000, #FFC420)',
                      WebkitBackgroundClip: 'text',
                      WebkitTextFillColor: 'transparent'
                    }}>
                    Topic Information
                </h1>
                <h2 className="mt-4 text-2xl font-black bg-clip-text text-white"
                    style={{
                            backgroundImage: 'linear-gradient(to right, #8A0000, #FFC420)',
                            WebkitBackgroundClip: 'text',
                            WebkitTextFillColor: 'transparent'
                        }}>
                        Explore detailed information on a wide range of topics.</h2>
            </section>
            {/* Section for displaying topics */}
            <section className="flex flex-wrap -mx-4">
                {isLoading ? (
                <p className="text-suGold w-full">Loading topic details...</p> // Displaying loading message
                ) : (
                topics.map(([categoryName, details]) => ( // Mapping over the topics array to render each topic
                    <article key={categoryName} className="w-full md:w-1/3 px-4 mb-8">
                    <div className="bg-suMaroon rounded-lg transition-shadow min-h-[12rem] max-h-[12rem] overflow-auto px-1 py-5 shadow-custom hover:shadow-medium transform hover:scale-105 duration-300">
                        <h2 className="font-bold text-xl text-white">{categoryName}</h2>
                        <ul>
                        {/* Mapping over the details of each topic to render them */}
                        {Object.entries(details).map(([key, value]) => {
                            if (key === 'faculty') {
                            return (
                                <li key={key}>
                                <button onClick={() => toggleDropdown(categoryName, 'faculty')} className="font-semibold text-white underline">
                                    Faculty
                                </button>
                                {/* Conditionally rendering the dropdown content */}
                                {openDropdowns[`${categoryName}-faculty`] && (
                                    <ul>
                                    {value.map((facultyName, index) => (
                                        <li key={index} className="font-medium text-white">{facultyName}</li>
                                    ))}
                                    </ul>
                                )}
                                </li>
                            );
                            } else if (key === 'departments') {
                            return (
                                <li key={key}>
                                <button onClick={() => toggleDropdown(categoryName, 'departments')} className="font-bold text-white underline">
                                  {details.department_count === 1 ? 'Department' : 'Departments'}
                                </button>
                                {/* Conditionally rendering the dropdown content */}
                                {openDropdowns[`${categoryName}-departments`] && (
                                    <ul>
                                    {value.map((departmentName, index) => (
                                        <li key={index} className="text-white">{departmentName}</li>
                                    ))}
                                    </ul>
                                )}
                                </li>
                            );
                            } else {
                            return <li key={key} className="font-bold text-white">{renderDetail(key, value)}</li>; // Rendering other details
                            }
                        })}
                        </ul>
                    </div>
                    </article>
                ))
                )}
            </section>
            </main>
            {/* Footer section */}
            <footer className="font-bold mt-12 bg-suMaroon text-suGold text-center p-4 rounded-md">
            <p>© {new Date().getFullYear()} Salisbury University Research. All rights reserved.</p>
            <p className="mt-2">Salisbury, Maryland, USA</p>
            </footer>
        </div>
    </div>
  );
};

export default TopicPage; // Exporting the TopicPage component for use in other parts of the application
