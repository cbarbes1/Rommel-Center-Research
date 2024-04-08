//Author: Jude Maggitti
//Created Date: 4/7/24
//Last Modifed: 4/7/24
//Note: This file displays the contents of the faculty members from the articles submitted into the ai

import React from 'react'; // Importing React to enable JSX syntax and component logic
import { Link, useParams } from 'react-router-dom'; // Importing Link component for client-side navigation between routes
import jsonData from '../JSON/FacultySample.json'; // Import JSON data file

const renderBodyAll = (data) => {//renders all faculty
    return (

        <div>
                <section class="flavor">
                    <section class="flavor-column bigger-column">
                    {Object.entries(data).map(([name, values]) => (
                        <ul>
                            <li><Link to={`/FacultyPage/${encodeURIComponent(name)}`} className="medium font">{name}</Link></li>
                        </ul>
                        ))}
                    </section>
                </section>
        </div>
    );
};

const renderBodyFaculty = (data, name) => {//renders one faculty data
    return (
        <div>
            <section className="flavor" key={name}>
                <section className="flavor-column bigger-column">
                    <h1 className="medium font">{name}</h1>
                    <ul>
                        <li>Office<ul>
                            <li>{data.Office}</li>
                        </ul>
                        </li>
                        <li>Email<ul>
                            <li>{data.Email}</li>
                        </ul>
                        </li>
                        <li>Department<ul>
                            <li>{data.Department}</li>
                        </ul>
                        </li>
                        <li>Citations<ul>
                            <li>
                                {data.Articles.map((article, index) => (
                                    <li key={index}>{article}</li>
                                ))}
                                
                            </li>
                        </ul>
                        </li>
                    </ul>
                </section>
                <aside class="flavor-column smaller-column">
            <p>Picture of the Faculty (If acceptable by Faculty)</p>
        </aside>
            </section>
        </div>
    );
};

const FacultyPage = () => {
    const { name } = useParams(); // Get the name from route parameters
    const data = jsonData;

    if (name && data[name]) {
        const facultyName = name; // Assuming the name is stored in a variable    
        return renderBodyFaculty(data[name], facultyName);//renders a specific Faculty
    }
    else
        return renderBodyAll(data);//renders all Faculty Names

};


export default FacultyPage; // Exporting the FacultyPage component for use in other parts of the application