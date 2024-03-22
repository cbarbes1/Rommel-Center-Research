import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css'; // Ensure this imports Tailwind CSS
import HomePage from './components/HomePage';
import TopicPage from './components/TopicPage'; // Make sure to import TopicPage

function App() {
  return (
    <Router>
      <div className="App min-h-screen bg-suGray">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/topics" element={<TopicPage />} />
          {/* Define more routes as needed */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;