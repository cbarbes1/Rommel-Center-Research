import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

const TopicPage = () => {
  const [topics, setTopics] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [openDropdowns, setOpenDropdowns] = useState({}); // Tracks which dropdowns are open for both faculty and departments

  useEffect(() => {
    const fetchTopics = async () => {
      setIsLoading(true);
      try {
        const response = await fetch('/processed_category_data.json');
        const data = await response.json();
        // Convert object to array of [key, value] pairs and sort alphabetically by key
        const sortedTopics = Object.entries(data).sort((a, b) => a[0].localeCompare(b[0]));
        setTopics(sortedTopics);
      } catch (error) {
        console.error('Failed to fetch topics:', error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchTopics();
  }, []);

  const toggleDropdown = (categoryName, type) => {
    setOpenDropdowns(prevState => ({
      ...prevState,
      [`${categoryName}-${type}`]: !prevState[`${categoryName}-${type}`]
    }));
  };

  const renderDetail = (key, value) => {
    let text = '';
    switch (key) {
      case 'faculty_count':
        text = `${value} Faculty`;
        break;
      case 'article_count':
        text = `${value} Articles`;
        break;
      case 'department_count':
        text = `${value} ${value === 1 ? 'Department' : 'Departments'}`;
        break;
      default:
        text = Array.isArray(value) ? value.join(', ') : value;
    }
    return text;
  };

  return (
    <div className="min-h-screen bg-stone-200 text-suGold">
      <div className="container mx-auto px-4 py-8">
        <header className="mb-8">
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
          <section className="text-center mb-12">
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold bg-clip-text text-transparent"
                style={{
                    backgroundImage: 'linear-gradient(to right, #8A0000 29%, #FFC420 80%)',
                    WebkitBackgroundClip: 'text',
                    WebkitTextFillColor: 'transparent'
                }}>
                Topic Information
            </h1>
            <p className="mt-4 text-lg font-bold bg-clip-text text-transparent"
                style={{
                        backgroundImage: 'linear-gradient(to right, #8A0000 29%, #FFC420 80%)',
                        WebkitBackgroundClip: 'text',
                        WebkitTextFillColor: 'transparent'
                    }}>
                    Explore detailed information on a wide range of topics.</p>
          </section>
          <section className="flex flex-wrap -mx-4">
            {isLoading ? (
              <p className="text-suGold w-full">Loading topic details...</p>
            ) : (
              topics.map(([categoryName, details]) => (
                <article key={categoryName} className="w-full md:w-1/3 px-4 mb-8">
                  <div className="bg-suMaroon rounded-lg shadow-xl transition-shadow min-h-[12rem] max-h-[12rem] overflow-auto px-1 py-5">
                    <h2 className="font-bold text-xl text-white">{categoryName}</h2>
                    <ul>
                      {Object.entries(details).map(([key, value]) => {
                        if (key === 'faculty') {
                          return (
                            <li key={key}>
                              <button onClick={() => toggleDropdown(categoryName, 'faculty')} className="font-semibold text-white underline">
                                Faculty
                              </button>
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
                                Departments
                              </button>
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
                          return <li key={key} className="font-bold text-white">{renderDetail(key, value)}</li>;
                        }
                      })}
                    </ul>
                  </div>
                </article>
              ))
            )}
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

export default TopicPage;
