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
            <a href="/html/Version3/index.html" class="nav-link">Home</a>
            <a href="/html/Version3/TopicPage.html" class="nav-link">Topic A-Z</a>
            <a href="/html/Version3/FacultyList.html" class="nav-link">Faculty Contact</a>
            <a href="/html/Version3/ArticleAZ.html" class="nav-link">Articles A-Z</a>
            </nav>
        </header>
    </div>`;
}
document.addEventListener("DOMContentLoaded", function () {
header();
});