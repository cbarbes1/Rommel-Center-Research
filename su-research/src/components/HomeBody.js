import React from 'react'; // Importing React to enable JSX syntax and component logic
import { Link } from 'react-router-dom'; // Importing Link component for client-side navigation between routes


const HomeBody = () => {
    return (
        <section class="flavor">
            <div class="flavor-column-topic bigger-column">
                <ul>
                    <li><div class="larger-font">Needs</div>
                        <ul>
                            <li class="medium-font">Description of the problem at hand</li>
                        </ul>
                    </li>
                    <li>
                        <div class="larger-font">Mission Statement</div>
                        <ul>
                            <li class="medium-font">Description of our goal to solve the issue</li>
                        </ul>
                    </li>
                    <li>
                        <div class ="larger-font">The Team</div>
                        <ul>
                            <div>
                                <li class="row-team">
                                    <div class="column">
                                        <div class="medium-font">Spencer</div>
                                    </div>
                                    <div class="column">
                                        <div class="medium-font">Cole</div>
                                    </div>
                                    <div class="column">
                                        <div class="medium-font">Will</div>
                                    </div>
                                    <div class="column">
                                        <div class="medium-font">Jude</div>
                                    </div>
                                </li>                            
                            </div>
                        </ul>
                    </li>                                       
                </ul>
            </div>
        </section>
      );

};

export default HomeBody; // Exporting the Header component for use in other parts of the application
