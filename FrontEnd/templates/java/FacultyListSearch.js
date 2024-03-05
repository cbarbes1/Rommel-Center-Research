function fetchTopicData() {
    const topic_Info = document.getElementById("topic_Info");

    function createTopicSegment(data) {
        const topicSegment = document.createElement("ul");
        topicSegment.innerHTML = `
        <li>
            <form class="send" action="/Faculty.html">
            <p class="large-font">${data.name}<button type="submit"></button></p>
        </li>
    `;

    topic_Info.appendChild(topicSegment);

    }

    fetch('templates/json/FacultyLinkList.json')
        .then(response => response.json())
        .then(data => {
            data.forEach(createTopicSegment);
        })
        .catch(error => console.error('Error fetching JSON:', error));
}

fetchTopicData();