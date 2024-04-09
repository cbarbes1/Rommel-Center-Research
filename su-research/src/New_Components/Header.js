import React from 'react'; // Importing React to enable JSX syntax and component logic
import { Link } from 'react-router-dom';
import 'tailwindcss/tailwind.css';
import 'su-research/src/styles.css';

function Header() {
    return (
        <div className="flavor-header">
            <header className="site-header">
                <h1>Salsibury Research</h1>
                <nav className="navigation">
                    <Link to="/html/Version2/index.html" className="nav-link">Home</Link>
                    <Link to="/html/Version2/TopicAZ.html" className="nav-link">Topic A-Z</Link>
                    <Link to="/html/Version2/FacultyAZ.html" className="nav-link">Faculty Contact</Link>
                    <Link to="/html/Version2/ArticleAZ.html" className="nav-link">Articles A-Z</Link>
                </nav>
            </header>
        </div>
    );
}

export default Header;
