function fetchFacultyListData() {
    const xmlhttp = new XMLHttpRequest();
    xmlhttp.onload = function () {
        const abArr = JSON.parse(this.responseText);

        const faculty_list = document.getElementById("faculty_list");

        faculty_list.innerHTML = '';

        abArr.forEach(function (item) {
            const facultyListItem = document.createElement("ul");
            facultyListItem.innerHTML = `
            <li>
                <form class="send" action="/Faculty.html">
                <p class="large-font">${item.name}<button type="submit"></button></p>
            </li>
            `;
            faculty_list.appendChild(facultyListItem);
        });
    };
    xmlhttp.open("GET", "/static/json/FacultyLinkList.json", true);
    xmlhttp.send();
}
document.addEventListener("DOMContentLoaded", function () {
    fetchFacultyListData();
});
