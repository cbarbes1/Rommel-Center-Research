function fetchArticleData(key) {
    const xmlhttp = new XMLHttpRequest();
    xmlhttp.onload = function () {
        const abArr = JSON.parse(this.responseText);

        document.getElementById("abstract").innerHTML = abArr.Article[key].Abstract;
        document.getElementById("Title").innerHTML = abArr.Article[key].Title;

        const authorList = document.getElementById("authorList");
        abArr.Article[key].Authors.forEach(function (item) {
            const authorItem = document.createElement("li");
            authorItem.innerHTML = item;
            authorList.appendChild(authorItem);
        });

        const citationsList = document.getElementById("citationsList");
        abArr.Article[key].Citations.forEach(function (item) {
            const citationsItem = document.createElement("li");
            citationsItem.innerHTML = item;
            citationsList.appendChild(citationsItem);
        });
    };
    xmlhttp.open("GET", "/static/json/AuthorSample.json", true);
    xmlhttp.send();
}


document.addEventListener("DOMContentLoaded", function () {
    const urlParams = new URLSearchParams(window.location.search);
    const articleKey = urlParams.get('key');

    fetchArticleData(articleKey);
});


