// # Author: Jude Maggitti
// # Last Modified: 3/10/24
// # Summary: shows the info of the home page
function body() {
    const body = document.getElementById("body");

    body.innerHTML = `
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
                                        <img src="/static/image/Aragorn.jpg" alt="Spencer" width="100" height="100"> 
                                        <div class="medium-font">Spencer</div>
                                    </div>
                                    <div class="column">
                                        <img src="/static/image/Legolas.jpg" alt="Spencer" width="100" height="100"> 
                                        <div class="medium-font">Cole</div>
                                    </div>
                                    <div class="column">
                                        <img src="/static/image/Gandalf.jpg" alt="Will" width="100" height="100"> 
                                        <div class="medium-font">Will</div>
                                    </div>
                                    <div class="column">
                                        <img src="/static/image/Gimli.jpg" alt="Jude" width="100" height="100"> 
                                        <div class="medium-font">Jude</div>
                                    </div>
                                </li>                            
                            </div>
                        </ul>
                    </li>                                       
                </ul>
            </div>
        </section>`;
}
document.addEventListener("DOMContentLoaded", function () {
    body();
});
