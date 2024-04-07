import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css'; // Ensure this imports Tailwind CSS
import HomeBody from './components/template/HomeBody.js';
import Layout from './components/template/Layout.js';
import TopicPage from './components/template/TopicPage.js'; // Make sure to import TopicPage

function App() {
  return (
    <Router>
      {/* <div className="App min-h-screen bg-suGray"> */}
      <Layout>
        <Routes>
          <Route path="/" element={<HomeBody />} />
          <Route path="/TopicPage/:category" element={<TopicPage />} />
          <Route path="/TopicPage" element={<TopicPage />} />
          {/* <Route path="/FacultyAZ" element={<ServicesPage />} /> */}
          {/* <Route path="/ArticleAZ" element={<ContactPage />} /> */}
        </Routes>
      </Layout>
      {/* </div> */}
    </Router>
  );
}

export default App;