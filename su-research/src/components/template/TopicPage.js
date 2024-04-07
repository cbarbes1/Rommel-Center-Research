import React from 'react'; // Importing React to enable JSX syntax and component logic
import { Link, useParams } from 'react-router-dom'; // Importing Link component for client-side navigation between routes
import jsonData from '../JSON/processed_category_data.json'; // Import JSON data file

const renderBodyAll = (data) => {
    return (

        <div>
            {Object.entries(data).map(([category, values]) => (
                <section class="flavor" key={category}>
                    <section class="flavor-column bigger-column">
                        <Link to={`/TopicPage/${encodeURIComponent(category)}`} className="medium font">{category}</Link>
                        <ul>
                            <li>
                                <ul>
                                    <li>Faculty Count: {values.faculty_count}</li>
                                    <li>Department Count: {values.department_count}</li>
                                    <li>Article Count: {values.article_count}</li>
                                </ul>
                            </li>
                        </ul>
                    </section>
                </section>
            ))}
        </div>
    );
};

const renderBodyTopic = (category, data) => {
    return (
        <div>
            <section className="flavor" key={data}>
                <section className="flavor-column bigger-column">
                    <p className="medium font">{data}</p>
                    <ul>
                        <li>
                            <ul>
                                <li>Faculty Count: {category.faculty_count}</li>
                                <li>Department Count: {category.department_count}</li>
                                <li>Article Count: {category.article_count}</li>
                            </ul>
                        </li>
                    </ul>
                </section>
            </section>
        </div>
    );
};

const TopicPage = () => {
    const { category } = useParams(); // Get the category from route parameters
    const data = jsonData;

    if (category && data[category]){
        const categoryName = category; // Assuming the category name is stored in a variable    
        return renderBodyTopic(data[category], categoryName);
    }
    else
        return renderBodyAll(data);

};


export default TopicPage; // Exporting the TopicPage component for use in other parts of the application