import React from 'react'; // Importing React to enable JSX syntax and component logic
import { Link } from 'react-router-dom'; // Importing Link component for client-side navigation between routes
import Header from './Header';
import Footer from './Footer';
import '../style/styles.css'

const Layout = ({ children }) => {
    return (
        <div>
          <Header />
          <main>{children}</main>
          <Footer />
        </div>
      );

};

export default Layout; // Exporting the Layout component for use in other parts of the application
