import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css'; // Ensure this imports Tailwind CSS
import Header from './New_Components/Header';
import SearchBar from './New_Components/searchBar';
import IndexBody from './New_Components/HomePage';
import Footer from './New_Components/Footer';

function App() {
  return (
    <Router>
      <div className="App min-h-screen bg-suGray">
        <Routes>
          <Route path="/" element={<Header />} />
          <Route path="/search" element={<SearchBar url="/your-search-url" />} />
          <Route path="/body" element={<IndexBody />} />
          <Route path="/footer" element={<Footer />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;