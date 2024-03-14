function search(key) {
    const header = document.getElementById("search");

    header.innerHTML = `
    <section>
            <div class="flavor-header" style="margin:auto;max-width:350px">
                <header class="site-header">
                    <form class="search" style="margin:auto;max-width:300px" action="${key}" method="GET">
                        <input type="text" placeholder="Search..." name="name">
                        <button type="submit"><i class="fa fa-search"></i></button>
                      </form>
                </header>
            </div>
    </section>
        `;
}
document.addEventListener("DOMContentLoaded", function () {
    search();
});
