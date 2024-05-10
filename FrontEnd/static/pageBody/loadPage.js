// # Author: Jude Maggitti
// # Last Modified: 3/31/24
// # Summary: loads webpages based on a key
function loadPage(fileName) {
    fetch('/static/pageBody/'+fileName+'.js')
        .then(response => response.text())
        .then(data => {
            const scriptElement = document.createElement('script');
            scriptElement.textContent = data;
            document.body.appendChild(scriptElement);
        })
        .catch(error => console.error('Error loading page:', error));
}
