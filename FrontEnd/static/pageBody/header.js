// # Author: Jude Maggitti
// # Last Modified: 3/31/24
// # Summary: Header for the webpages
function header() {
    const header = document.getElementById("nav");

    header.innerHTML = `
    <div class="flavor-header">
        <header class="site-header">
            <h1>Salsibury Research</h1>
            <nav class="navigation">
                <a href="#" class="nav-link" onclick="loadPage('indexBody')">Home</a>
                <a href="#" class="nav-link" onclick="loadPage('TopicBody')">Topic A-Z</a>
                <a href="#" class="nav-link" onclick="loadPage('FacultyListSearch')">Faculty Contact</a>
                <a href="#" class="nav-link" onclick="loadPage('ArticleListSearch')">Articles A-Z</a>
            </nav>
        </header>
    </div>`;
}
document.addEventListener("DOMContentLoaded", function () {
header();
});
