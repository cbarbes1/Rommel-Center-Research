import React from 'react'; // Importing React to enable JSX syntax and component logic

function Footer() {
    return (
        <footer className="font-bold mt-12 bg-suMaroon text-suGold text-center p-4 rounded-md">
            <p>© {new Date().getFullYear()} Salisbury University Research. All rights reserved.</p>
            <p className="mt-2">Salisbury, Maryland, USA</p>
        </footer>
    );
}

export default Footer;
