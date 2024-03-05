// function fetchArticleListData() {
//     const topic_Info = document.getElementById("topic_Info");

//     function createTopicSegment(data) {
//         const topicSegment = document.createElement("ul");
//         topicSegment.innerHTML = `
//         <li>
//             <form class="send" action="/Article.html">
//             <p class="large-font">${data.name} 
//             <button type="submit"></button>
//             </p>
//           </form>
//         </li>
//     `;

//     topic_Info.appendChild(topicSegment);

//     }

//     fetch('../json/ArticleLinkList.json')
//         .then(response => response.json())
//         .then(data => {
//             data.forEach(createTopicSegment);
//         })
//         .catch(error => console.error('Error fetching JSON:', error));
// }

// fetchArticleListData();

function fetchArticleListData() {
    const xmlhttp = new XMLHttpRequest();
    xmlhttp.onload = function () {
        const abArr = JSON.parse(this.responseText);

        const article_List = document.getElementById("article_List");

        article_List.innerHTML = '';

        abArr.forEach(function (item) {
            const articleListItem = document.createElement("ul");
            articleListItem.innerHTML = `
            <li>
             <form class="send" action="/Article.html">
             <p class="large-font">${item.name} 
             <button type="submit"></button>
             </p>
           </form>
         </li>
            `;
            article_List.appendChild(articleListItem);
        });
    };
    xmlhttp.open("GET", "/static/json/ArticleLinkList.json", true);
    xmlhttp.send();
}
document.addEventListener("DOMContentLoaded", function () {
    fetchArticleListData();
});
