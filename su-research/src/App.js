import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css'; // Ensure this imports Tailwind CSS
import HomeBody from './components/HomeBody';
import Layout from './components/Layout.js';
import TopicPage from './components/TopicPage'; // Make sure to import TopicPage

function App() {
  return (
    <Router>
      {/* <div className="App min-h-screen bg-suGray"> */}
      <Layout>
        <Routes>
          <Route path="/" element={<HomeBody />} />
          {/* <Route path="/TopicAZ" component={TopicPage} /> */}
          {/* <Route path="/FacultyAZ" component={ServicesPage} /> */}
          {/* <Route path="/ArticleAZ" component={ContactPage} /> */}
        </Routes>
      </Layout>
      {/* </div> */}
    </Router>
  );
}

export default App;