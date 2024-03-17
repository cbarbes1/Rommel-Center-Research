function body() {
    const body = document.getElementById("body");

    body.innerHTML = `
                <ul>
                    <li>Office<ul>
                            <li><p id="Office"></p></li>
                        </ul>
                    </li>
                    <li>Email<ul>
                            <li><p id="Email"></p></li>
                        </ul>
                    </li>
                    <li>Department<ul>
                            <li><p id="Department"></p></li>
                        </ul>
                    </li>
                    <li>Citations<ul>
                        <ul id="ArticleList"></ul>
                        </ul>
                    </li>
                </ul>`;
}
document.addEventListener("DOMContentLoaded", function () {
    body();
});
