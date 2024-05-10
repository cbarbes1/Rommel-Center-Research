//Author: Jude Maggitti
//Created Date: 4/7/24
//Last Modifed: 4/7/24
//Note: Renders the site, and controls the routes the website takes from use input


import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css'; // Ensure this imports Tailwind CSS
import HomeBody from './components/template/HomeBody.js';
import Layout from './components/template/Layout.js';
import TopicPage from './components/template/TopicPage.js'; // Make sure to import TopicPage
import FacultyPage from './components/template/FacultyPage.js'; // Make sure to import FacultyPage
import ArticlePage from './components/template/ArticlePage.js'; // Make sure to import ArticlePage

function App() {
  return (
    <Router>
      {/* <div className="App min-h-screen bg-suGray"> */}
      <Layout>{/* Layout Tag */}
        <Routes>
          <Route path="/" element={<HomeBody />} />{/* Home Page */}
          <Route path="/TopicPage/:category" element={<TopicPage />} />{/* Topic Page */}
          <Route path="/TopicPage" element={<TopicPage />} />{/* Defualt Topic Page */}
          <Route path="/FacultyPage/:name" element={<FacultyPage />} />{/* Faculty Page */}
          <Route path="/FacultyPage" element={<FacultyPage />} />{/* Defualt Faculty Page */}
          <Route path="/ArticlePage/:name" element={<ArticlePage />} />{/* Article Page */}
          <Route path="/ArticlePage" element={<ArticlePage />} />{/* Defualt Article Page */}
        </Routes>
      </Layout>{/* Layout End Tag */}
      {/* </div> */}
    </Router>
  );
}

export default App;