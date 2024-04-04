// # Author: Jude Maggitti
// # Last Modified: 3/10/24
// # Summary: gets the info of the article in html form based on a key
function fetchArticleData(key) {
    const xmlhttp = new XMLHttpRequest();
    xmlhttp.onload = function () {
        const abArr = JSON.parse(this.responseText);

        document.getElementById("abstract").innerHTML = abArr[key].Abstract;
        document.getElementById("Title").innerHTML = key;

        const authorList = document.getElementById("authorList");//gets list of authors
        abArr[key].Authors.forEach(function (item) {
            const authorItem = document.createElement("li");
            authorItem.innerHTML = item;
            authorList.appendChild(authorItem);
        });

        const citationsList = document.getElementById("citationsList");//gets list of citations
        abArr[key].Citations.forEach(function (item) {
            const citationsItem = document.createElement("li");
            citationsItem.innerHTML = item;
            citationsList.appendChild(citationsItem);
        });
    };
    xmlhttp.open("GET", "/static/json/AuthorSample.json", true);//gets json file
    xmlhttp.send();
}


document.addEventListener("DOMContentLoaded", function () {
    const urlParams = new URLSearchParams(window.location.search);
    const articleName = urlParams.get('key');

    fetchArticleData(articleName);
});


