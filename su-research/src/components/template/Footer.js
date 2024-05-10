//Author: Jude Maggitti
//Created Date: 4/6/24
//Last Modifed: 4/7/24
//Note: Displays the footer of the website page

import React from 'react'; // Importing React to enable JSX syntax and component logic
import { Link } from 'react-router-dom'; // Importing Link component for client-side navigation between routes


const Footer = () => {//renders the footer of the website
    return (
        <footer className="font-bold mt-12 bg-suMaroon text-suGold text-center p-4 rounded-md">
          <p>© {new Date().getFullYear()} Salisbury University Research. All rights reserved.</p>
          <p className="mt-2">Salisbury, Maryland, USA</p>
        </footer>
      );

};

export default Footer; // Exporting the Footer component for use in other parts of the application
