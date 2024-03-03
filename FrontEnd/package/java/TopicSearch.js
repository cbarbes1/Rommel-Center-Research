function fetchTopicData() {
    const topic_Info = document.getElementById("topic_Info");

    function createTopicSegment(data) {
        const topicSegment = document.createElement("ul");
        topicSegment.innerHTML = `
        <li>
            <p class="large-font">${data.name}</p>
            <ul>
                <li><p id="faculty_count">Faculty Count: ${data.faculty_count}</p></li>
                <li><p id="department_count">Department Count: ${data.department_count}</p></li>
                <li><p id="article_count">Article Count: ${data.article_count}</p></li>
            </ul>
        </li>
    `;

    topic_Info.appendChild(topicSegment);

    }

    fetch('package/json/keyPaths.json')
        .then(response => response.json())
        .then(data => {
            data.forEach(createTopicSegment);
        })
        .catch(error => console.error('Error fetching JSON:', error));
}

fetchTopicData();