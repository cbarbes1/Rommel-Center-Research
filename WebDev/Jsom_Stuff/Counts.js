class Counts {
    constructor() {
        this.jsonData = null;
    }

    async loadJson() {
        let response = await fetch('category_and_category_metadata.json');
        this.jsonData = await response.json();
    }

    get_fac_counts(category) {
        return this.jsonData[category]["faculty_count"];
    }

    get_dept_count(category) {
        return this.jsonData[category]["department_count"];
    }

    get_article_counts(category) {
        return this.jsonData[category]["article_count"];
    }

    async get_counts(category) {
        if (!this.jsonData) {
            await this.loadJson();
        }
        let facultyCount = this.get_fac_counts(category);
        let departmentCount = this.get_dept_count(category);
        let articleCount = this.get_article_counts(category);

        return [facultyCount, departmentCount, articleCount];
    }
}

let counts = new Counts();
let category = "Chemistry, Multidisciplinary";
counts.get_counts(category).then(result => {
    console.log(result);  // This will output [21, 5, 0] for the given JSON data
});
