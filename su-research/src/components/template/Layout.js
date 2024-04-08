//Author: Jude Maggitti
//Created Date: 4/6/24
//Last Modifed: 4/7/24
//Note: Holds/displays the layout of the webpages fto act as a template

import React from 'react'; // Importing React to enable JSX syntax and component logic
import { Link } from 'react-router-dom'; // Importing Link component for client-side navigation between routes
import Header from './Header'; //imports header file
import Footer from './Footer';//imports footer file
import '../style/styles.css'

const Layout = ({ children }) => {//renders the skeleton of the website with a child render
    return (
        <div>
          <Header />
          <main>{children}</main>
          <Footer />
        </div>
      );

};

export default Layout; // Exporting the Layout component for use in other parts of the application
