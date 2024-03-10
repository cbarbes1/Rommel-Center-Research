function fetchTopicData() {
    const xmlhttp = new XMLHttpRequest();
    xmlhttp.onload = function () {
        const abArr = JSON.parse(this.responseText);

        const topic_Info = document.getElementById("topic_Info");

        topic_Info.innerHTML = '';

        Object.keys(abArr).forEach(function (topicName) {
            const topicItem = document.createElement("ul");
            const topicData = abArr[topicName];
            topicItem.innerHTML = `
                <li>
                <a href = "/html/Topic.html?name=${encodeURIComponent(topicName)}" ><p class = "medium font">${topicName}</p></a>
                    <ul>
                        <li><p class="faculty_count">Faculty Count: ${topicData.faculty_count}</p></li>
                        <li><p class="department_count">Department Count: ${topicData.department_count}</p></li>
                        <li><p class="article_count">Article Count: ${topicData.article_count}</p></li>
                    </ul>
                </li>
            `;
            topic_Info.appendChild(topicItem);
        });
    };
    xmlhttp.open("GET", "/static/json/categoryInfo.json", true);
    xmlhttp.send();
}
document.addEventListener("DOMContentLoaded", function () {
    fetchTopicData();
});
