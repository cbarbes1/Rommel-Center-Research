// # Author: Jude Maggitti
// # Last Modified: 3/10/24
// # Summary: gets the list of faculty in html form
function fetchFacultyListData() {
    const xmlhttp = new XMLHttpRequest();
    xmlhttp.onload = function () {
        const abArr = JSON.parse(this.responseText);

        const faculty_list = document.getElementById("faculty_list");

        faculty_list.innerHTML = '';

        abArr.forEach(function (item) {//gets each faculty member in a list
            const facultyListItem = document.createElement("ul");
            facultyListItem.innerHTML = `
            <li>
            <a href = "/html/Version1/Faculty.html?name=${encodeURIComponent(item.name)}" class ="custom-link"><p class = "medium font">${item.name}</p></a>
            </li>
            `;
            faculty_list.appendChild(facultyListItem);
        });
    };
    xmlhttp.open("GET", "/static/json/FacultyLinkList.json", true);//gets json file
    xmlhttp.send();
}

document.addEventListener("DOMContentLoaded", function () {
    fetchFacultyListData();
});
