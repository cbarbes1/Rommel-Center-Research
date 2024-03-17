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
