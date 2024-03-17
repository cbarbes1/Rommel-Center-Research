function fetchArticleData(key) {
    const xmlhttp = new XMLHttpRequest();
    xmlhttp.onload = function () {
        const abArr = JSON.parse(this.responseText);

        const articleData = abArr[key];

        if (articleData) {
        document.getElementById("abstract").innerHTML = abArr[key].Abstract;
        document.getElementById("Title").innerHTML = key;

        const authorList = document.getElementById("authorList");
        abArr[key].Authors.forEach(function (item) {
            const authorItem = document.createElement("li");
            authorItem.innerHTML = item;
            authorList.appendChild(authorItem);
        });

        const citationsList = document.getElementById("citationsList");
        abArr[key].Citations.forEach(function (item) {
            const citationsItem = document.createElement("li");
            citationsItem.innerHTML = item;
            citationsList.appendChild(citationsItem);
        });
    } else {
        document.getElementById("Title").innerHTML = `          
                <p class="medium font">Article Not Found</p>`;
    }
    };
    xmlhttp.open("GET", "/static/json/AuthorSample.json", true);
    xmlhttp.send();
}


document.addEventListener("DOMContentLoaded", function () {
    const urlParams = new URLSearchParams(window.location.search);
    const articleName = urlParams.get('key');

    fetchArticleData(articleName);
});


