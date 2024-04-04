// # Author: Jude Maggitti
// # Last Modified: 3/10/24
// # Summary: gets the header of the webpages in html form
function header() {
    const header = document.getElementById("header");

    header.innerHTML = `
    <div class="flavor-header">
        <header class="site-header">
            <h1>Salsibury Research</h1>
            <nav class="navigation">
                <a href="/html/index.html" class="nav-link">Home</a>
                <a href="/html/TopicAZ.html" class="nav-link">Topic A-Z</a>
                <a href="/html/FacultyAZ.html" class="nav-link">Faculty Contact</a>
                <a href="/html/ArticleAZ.html" class="nav-link">Articles A-Z</a>
            </nav>
        </header>
    </div>`;
}
document.addEventListener("DOMContentLoaded", function () {
header();
});
