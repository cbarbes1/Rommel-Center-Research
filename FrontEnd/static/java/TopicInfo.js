function fetchTopic(key) {
    const xmlhttp = new XMLHttpRequest();
    xmlhttp.onload = function () {
        const abArr = JSON.parse(this.responseText);

        const topic_Info = document.getElementById("topic_Info");
        topic_Info.innerHTML = '';

        const topicItem = document.createElement("ul");
        topicItem.innerHTML = `
            <li>
                <p class="large-font">${key}</p>
                <ul>
                    <li><p class="faculty_count">Faculty Count: ${abArr[key].faculty_count}</p></li>
                    <li><p class="department_count">Department Count: ${abArr[key].department_count}</p></li>
                    <li><p class="article_count">Article Count: ${abArr[key].article_count}</p></li>
                    <li>
                        <p class="medium font">Faculty List:</p>
                        <ul>${abArr[key].faculty_set.map(item => `<li><p class="medium font">${item}</p></li>`).join('')}</ul>
                    </li>
                    <li>
                        <p class="medium font">Department List:</p>
                        <ul>${abArr[key].department_set.map(item => `<li><p class="medium font">${item}</p></li>`).join('')}</ul>
                    </li>
                </ul>
            </li>
        `;

        topic_Info.appendChild(topicItem);
    };

    xmlhttp.open("GET", "/static/json/categoryInfo.json", true);
    xmlhttp.send();
}

document.addEventListener("DOMContentLoaded", function () {
    const urlParams = new URLSearchParams(window.location.search);
    const facultyName = urlParams.get('name');

    fetchTopic(facultyName);
});
