import React from 'react'; // Importing React to enable JSX syntax and component logic
import { Link } from 'react-router-dom'; // Importing Link component for client-side navigation between routes


const Header = () => {
    return (
        <div class="flavor-header">
        <header class="site-header">
            <h1>Salsibury Research</h1>
            <nav class="navigation">
                <Link to="/" class="nav-link">Home</Link>
                <Link to="/TopicAZ" class="nav-link">Topic A-Z</Link>
                <Link to="/FacultyAZ" class="nav-link">Faculty Contact</Link>
                <Link to="/ArticleAZ" class="nav-link">Articles A-Z</Link>
            </nav>
        </header>
    </div>
      );

};

export default Header; // Exporting the Header component for use in other parts of the application
