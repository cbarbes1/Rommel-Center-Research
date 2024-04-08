//Author: Jude Maggitti
//Created Date: 4/6/24
//Last Modifed: 4/7/24
//Note: Displays the header of the website page
import React from 'react'; // Importing React to enable JSX syntax and component logic
import { Link } from 'react-router-dom'; // Importing Link component for client-side navigation between routes


const Header = () => {//renders the header of the website
    return (
        <div class="flavor-header">
        <header class="site-header">
            <h1>Salsibury Research</h1>
            <nav class="navigation">
                <Link to="/" class="nav-link">Home</Link>
                <Link to="/TopicPage" class="nav-link">Topic A-Z</Link>
                <Link to="/FacultyPage" class="nav-link">Faculty Contact</Link>
                <Link to="/ArticlePage" class="nav-link">Articles A-Z</Link>
            </nav>
        </header>
    </div>
      );

};

export default Header; // Exporting the Header component for use in other parts of the application
