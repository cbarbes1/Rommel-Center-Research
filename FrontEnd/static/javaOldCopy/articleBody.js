// # Author: Jude Maggitti
// # Last Modified: 3/31/24
// # Summary: holds the body html of an article
function body() {
    const body = document.getElementById("body");

    body.innerHTML = `
    <ul>
    <li>Authors<ul>
            <ul id="authorList"></ul>
        </ul>
    </li>
    <li>Abstract<ul>
            <li><p id="abstract"></p></li>
        </ul>
    </li>
    <li>Citations<ul>
            <li><p id="citationsList"></p></li>
        </ul>
    </li>                                       
</ul>`;
}
document.addEventListener("DOMContentLoaded", function () {
    body();
});
