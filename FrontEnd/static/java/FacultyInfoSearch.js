// # Author: Jude Maggitti
// # Last Modified: 3/31/24
// # Summary: gets the info of the facultymember in html form based on a key
function fetchFacultyData(key) {
    const xmlhttp = new XMLHttpRequest();
    xmlhttp.onload = function () {
        const abArr = JSON.parse(this.responseText);

        const facultyData = abArr[key];

        if (facultyData) {
            const ArticleList = document.getElementById("ArticleList");
            document.getElementById("Name").innerHTML = key;
            document.getElementById("Office").innerHTML = abArr[key].Office;
            document.getElementById("Email").innerHTML = abArr[key].Email;
            document.getElementById("Department").innerHTML = abArr[key].Department;

            abArr[key].Articles.forEach(function (item) {//gets list of articles under the faculty
                const articleItem = document.createElement("li");
                articleItem.innerHTML = item;
                ArticleList.appendChild(articleItem);
            });
        } else {
            document.getElementById("Name").innerHTML = `          
                    <p class="medium font">Faculty Not Found</p>`;
        }
    };
    xmlhttp.open("GET", "/static/json/FacultySample.json", true);//gets json file
    xmlhttp.send();
}

document.addEventListener("DOMContentLoaded", function () {
    const urlParams = new URLSearchParams(window.location.search);
    const facultyName = urlParams.get('name');

    fetchFacultyData(facultyName);
});

