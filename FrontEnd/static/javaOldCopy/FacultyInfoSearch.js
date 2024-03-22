function fetchFacultyData(key) {
    const xmlhttp = new XMLHttpRequest();
    xmlhttp.onload = function () {
        const abArr = JSON.parse(this.responseText);

        document.getElementById("Name").innerHTML = key;
        document.getElementById("Office").innerHTML = abArr[key].Office;
        document.getElementById("Email").innerHTML =  abArr[key].Email;
        document.getElementById("Department").innerHTML = abArr[key].Department;

        const ArticleList = document.getElementById("ArticleList");
        abArr[key].Articles.forEach(function (item) {
            const articleItem = document.createElement("li");
            articleItem.innerHTML = item;
            ArticleList.appendChild(articleItem);
        });
    };
    xmlhttp.open("GET", "/static/json/FacultySample.json", true);
    xmlhttp.send();
}

document.addEventListener("DOMContentLoaded", function () {
    const urlParams = new URLSearchParams(window.location.search);
    const facultyName = urlParams.get('name');

    fetchFacultyData(facultyName);
});

