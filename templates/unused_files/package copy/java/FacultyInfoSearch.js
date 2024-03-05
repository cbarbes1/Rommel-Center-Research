function fetchFacultyData(key) {
    const xmlhttp = new XMLHttpRequest();
    xmlhttp.onload = function () {
        const abArr = JSON.parse(this.responseText);

        document.getElementById("Name").innerHTML = abArr.Teacher[key].Name;
        document.getElementById("Office").innerHTML = abArr.Teacher[key].Office;
        document.getElementById("Email").innerHTML =  abArr.Teacher[key].Email;
        document.getElementById("Department").innerHTML = abArr.Teacher[key].Department;

        const ArticleList = document.getElementById("ArticleList");
        abArr.Teacher[key].Articles.forEach(function (item) {
            const articleItem = document.createElement("li");
            articleItem.innerHTML = item;
            ArticleList.appendChild(articleItem);
        });
    };
    xmlhttp.open("GET", "../json/FacultySample.json", true);
    xmlhttp.send();
}

fetchFacultyData(0);
