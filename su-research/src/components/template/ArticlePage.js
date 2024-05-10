//Author: Jude Maggitti
//Created Date: 4/7/24
//Last Modifed: 4/7/24
//Note: This file displays the contents of the articles submitted into the ai

import React from 'react'; // Importing React to enable JSX syntax and component logic
import { Link, useParams } from 'react-router-dom'; // Importing Link component for client-side navigation between routes
import jsonData from '../JSON/AuthorSample.json'; // Import JSON data file

const renderBodyAll = (data) => {//renders all articles
    return (

        <div>
            <section class="flavor">
                <section class="flavor-column bigger-column">
                    {Object.entries(data).map(([name, values]) => (
                        <ul>
                            <li><Link to={`/ArticlePage/${encodeURIComponent(name)}`} className="medium font">{name}</Link></li>
                        </ul>
                    ))}
                </section>
            </section>
        </div>
    );
};

const renderBodyArticle = (data, name) => {//renders one article data
    return (
        <div>
            <section className="flavor" key={name}>
                <section className="flavor-column bigger-column">
                    <h1 className="medium font">{name}</h1>
                    <ul>
                        <li>Authors<ul>
                            <li>{data.Authors}</li>
                        </ul>
                        </li>
                        <li>Abstract<ul>
                            <li>{data.Abstract}</li>
                        </ul>
                        </li>
                        <li>Citations<ul>
                            <li>
                                {data.Citations.map((article, index) => (
                                    <li key={index}>{article}</li>
                                ))}

                            </li>
                        </ul>
                        </li>
                    </ul>
                </section>
            </section>
        </div>
    );
};

const ArticlePage = () => {
    const { name } = useParams(); // Get the name from route parameters
    const data = jsonData;

    if (name && data[name]) {
        const facultyName = name; // Assuming the name is stored in a variable    
        return renderBodyArticle(data[name], facultyName);//renders a specific Article
    }
    else
        return renderBodyAll(data);//renders all Articles

};


export default ArticlePage; // Exporting the ArticlePage component for use in other parts of the application