import React from 'react'; // Importing React to enable JSX syntax and component logic
import { Link } from 'react-router-dom';
import 'tailwindcss/tailwind.css';
function SearchBar({ url }) {
    return (
        <section>
            <div className="flavor-header" style={{ margin: 'auto', maxWidth: '350px' }}>
                <header className="site-header">
                    <form className="search" style={{ margin: 'auto', maxWidth: '300px' }} action={url} method="GET">
                        <input type="text" placeholder="Search..." name="name" />
                        <button type="submit"><i className="fa fa-search"></i></button>
                    </form>
                </header>
            </div>
        </section>
    );
}

export default SearchBar;
