function body() {
    const body = document.getElementById("body");

    body.innerHTML=`
    <div class="content-container">
        <section class="filter">
            <article class="flavor-column bigger-column">
                <h2 class="medium-font">Filter Section</h2>
                <select class="medium-font dropdown" id="filter-option-1">
                    <option value="">Select Filter option 1</option>
                    <option value="option1">Filter option 1</option>
                    <option value="option2">Filter option 2</option>
                    <option value="option3">Filter option 3</option>
                </select>
                <select class="medium-font dropdown" id="filter-option-2">
                    <option value="">Select Filter option 2</option>
                    <option value="option1">Filter option 1</option>
                    <option value="option2">Filter option 2</option>
                    <option value="option3">Filter option 3</option>
                </select>
                <select class="medium-font dropdown" id="filter-option-3">
                    <option value="">Select Filter option 3</option>
                    <option value="option1">Filter option 1</option>
                    <option value="option2">Filter option 2</option>
                    <option value="option3">Filter option 3</option>
                </select>
            </article>
        </section>
        <section class="flavor">
            <article class="flavor-column-topic bigger-column" id="topic_Info">
            </article>
        </section>
    </div>`;
}
document.addEventListener("DOMContentLoaded", function () {
    body();
});