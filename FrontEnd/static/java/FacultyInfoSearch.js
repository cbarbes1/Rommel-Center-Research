function fetchFacultyData(key) {
    const xmlhttp = new XMLHttpRequest();
    xmlhttp.onload = function () {
        const abArr = JSON.parse(this.responseText);

        document.getElementById("Name").innerHTML = abArr[key].Name;
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

fetchFacultyData(0);
