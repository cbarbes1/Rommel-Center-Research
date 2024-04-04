// # Author: Jude Maggitti
// # Last Modified: 3/31/24
// # Summary: gets the info of the topic/category based on a key.
function fetchTopic(key) {
    const xmlhttp = new XMLHttpRequest();
    xmlhttp.onload = function () {
        const abArr = JSON.parse(this.responseText);

        const topic_Info = document.getElementById("topic_Info");
        topic_Info.innerHTML = '';

        const topicData = abArr[key];

        if (topicData) {
            const topicItem = document.createElement("ul");
            topicItem.innerHTML = `
                <li>
                    <p class="large-font">${key}</p>
                    <ul>
                        <li><p class="faculty_count">Faculty Count: ${topicData.faculty_count}</p></li>
                        <li><p class="department_count">Department Count: ${topicData.department_count}</p></li>
                        <li><p class="article_count">Article Count: ${topicData.article_count}</p></li>
                        <li>
                            <p class="medium font">Faculty List:</p>
                            <ul>${topicData.faculty.map(item => `<li><p class="medium font">${item}</p></li>`).join('')}</ul>
                        </li>
                        <li>
                            <p class="medium font">Department List:</p>
                            <ul>${topicData.departments.map(item => `<li><p class="medium font">${item}</p></li>`).join('')}</ul>
                        </li>
                    </ul>
                </li>
            `;
            topic_Info.appendChild(topicItem);
        } else {
            topic_Info.innerHTML = `
            <ul>
                <li>
                <ul>
                    <li>
                        <p class="medium font">Topic Not Found</p>
                    </li>
                </ul>
                </li>
            </ul>`;
        }
    };

    xmlhttp.open("GET", "/static/json/processed_category_data.json", true);//gets json file
    xmlhttp.send();
}

document.addEventListener("DOMContentLoaded", function () {
    const urlParams = new URLSearchParams(window.location.search);
    const facultyName = urlParams.get('name');
    fetchTopic(facultyName);
});
