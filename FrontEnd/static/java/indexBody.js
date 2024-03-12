function body() {
    const body = document.getElementById("body");

    body.innerHTML = `
    <section class="flavor">
            <div class="flavor-column-topic bigger-column">
                <ul>
                    <li><div class="larger-font">Needs</div><ul>
                        <li class="medium-font">Description of the problem at hand</li>
                        </ul>
                    </li>
                    <li><div class="larger-font">Mission Statement</div><ul>
                            <li class="medium-font">Description of our goal to solve the issue</li>
                        </ul>
                    </li>
                    <li><div class ="larger-font">The Team</div><ul>
                            <li class="medium-font">Photos of each team member</li>
                        </ul>
                    </li>                                       
                </ul>
            </div>
        </section>`;
}
document.addEventListener("DOMContentLoaded", function () {
    body();
});
