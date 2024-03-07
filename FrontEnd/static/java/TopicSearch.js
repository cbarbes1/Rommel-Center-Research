function fetchTopicData() {
    const xmlhttp = new XMLHttpRequest();
    xmlhttp.onload = function () {
        const abArr = JSON.parse(this.responseText);

        const topic_Info = document.getElementById("topic_Info");

        topic_Info.innerHTML = '';

        abArr.forEach(function (item) {
            const topicItem = document.createElement("ul");
            topicItem.innerHTML = `
                <li>
                    <p class="large-font">${item.name}</p>
                    <ul>
                        <li><p class="faculty_count">Faculty Count: ${item.faculty_count}</p></li>
                        <li><p class="department_count">Department Count: ${item.department_count}</p></li>
                        <li><p class="article_count">Article Count: ${item.article_count}</p></li>
                    </ul>
                </li>
            `;
            topic_Info.appendChild(topicItem);
        });
    };
    xmlhttp.open("GET", "/static/json/keyPaths.json", true);
    xmlhttp.send();
}
document.addEventListener("DOMContentLoaded", function() {
    fetchTopicData();
});
