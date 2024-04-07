import React from 'react'; // Importing React to enable JSX syntax and component logic
import { Link, useParams } from 'react-router-dom'; // Importing Link component for client-side navigation between routes
import jsonData from '../JSON/AuthorSample.json'; // Import JSON data file

const renderBodyAll = (data) => {
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

const renderBodyArticle = (data, name) => {
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
        const facultyName = name; // Assuming the name name is stored in a variable    
        return renderBodyArticle(data[name], facultyName);
    }
    else
        return renderBodyAll(data);

};


export default ArticlePage; // Exporting the ArticlePage component for use in other parts of the application