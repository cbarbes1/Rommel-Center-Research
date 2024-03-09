import re
import os
import json
import sys

sys.path.append(
    "/mnt/linuxlab/home/spresley1/Desktop/425testing/ResearchNotes/Rommel-Center-Research/PythonCode/Utilities"
)

from utilities import Utilities


class WosCategorization:

    def __init__(self):
        self.utils = Utilities()
        self.category_counts = {}
        self.author_pattern = re.compile(r"Author:(.*?)_", re.DOTALL)
        self.article_pattern = re.compile(r"_Title:(.*?)\.txt", re.DOTALL)

    def get_category_counts(self):
        return self.category_counts

    def load_counts(self, json_file_path):
        """
        Arguments:
            json_file_path: str, path to json file containing category counts
        Returns:
            None

        Loads the counts from the json file and stores them in category_counts dictionary
        """
        try:
            with open(json_file_path, "r") as file:
                self.category_counts = json.load(file)
        except FileNotFoundError:
            self.category_counts = {}

    def save_counts(self, json_file_path):
        """
        Arguments:
            json_file_path: str, path to json file to save category counts to
        Returns:
            None

        Save the category_counts to the json

        idea of this function and load_counts is to allow for the ability to save to a json file and then load it back in to continue processing

        if we just want to load the current counts in the json file and don't need to run the whole program to update stuff then we can just use load_counts to pull into category_counts what we have

        if we're running the program all the way through then this function will save that data to the json file so the above statements can be done in the future
        """
        with open(json_file_path, "w") as file:
            json.dump(self.category_counts, file, indent=4)

    def entries_to_categorize(self, entries):
        """
        Arguments:
            entries (dict): dictionary of entries to categorize, keys are entry names and values are paths to the json files
        Returns:
            None

        goes through each entry and processes the categories for that entry
        """
        for entry, path in entries.items():
            # print(f"Processing {entry}: {path}")
            categories_for_entry = self.utils.get_wos_categories(path)

            # add the processed authors and articles to corresponding sets. Avoids duplicates and allows for quick lookup time.
            processed_authors = set()
            processed_articles = set()

            for category in categories_for_entry:
                self.process_category(
                    category, path, processed_authors, processed_articles
                )
        return self.category_counts

    def process_category(self, category, path, processed_authors, processed_articles):
        """
        Arguments:
            category (str): category to process
            path (str): path to json file
            processed_authors (set): set of authors that have already been processed
            processed_articles (set): set of articles that have already been processed
        Returns:
            None

        Checks if category already exists, if it doesn't creates it and initializes all its counts to 0
        Then checks if the author or article has already been processed. If not, updates the counts for the category and adds them to corresponding sets

        Idea: add article if it doesn't exist. Update faculty count if they don't have work under that category yet (avoid counting the same author for each paper they have under the category)
                doesn't count the same article more than once (this step is not as necessary, but it ensures if for some reason we have duplicate documents we don't count n-amount of duplicates)
        """
        author, article = self.extract_authors_and_articles(path)

        # Initialize category in dictionary if not present
        category = self.clean_category_name(category)
        if category not in self.category_counts:
            self.category_counts[category] = {
                "faculty_count": 0,
                "department_count": 0,
                "article_count": 0,
            }
        if author is not None and author not in processed_authors:
            self.update_faculty_count(category)
            # TODO: in update faculty check if department exists yet if not add it
            processed_authors.add(author)

        if article is not None and article not in processed_articles:
            self.update_article_count(category)
            processed_articles.add(article)

    def clean_category_name(self, category):
        cleaned_name = " ".join(category.split())
        return cleaned_name

    def update_faculty_count(self, category):
        """
        Arguments:
            category (str): category to update faculty count for
        Returns:
            None

        Takes in category and updates it's faculty counter by 1
        """
        self.category_counts[category]["faculty_count"] += 1

    def update_department_count(self, category):
        """
        Arguments:
            category (str): category to update faculty count for
        Returns:
            None

        Takes in category and updates it's department counter by 1
        """
        self.category_counts[category]["department_count"] += 1

    def update_article_count(self, category):
        """
        Arguments:
            category (str): category to update faculty count for
        Returns:
            None

        Takes in category and updates it's article counter by 1
        """
        self.category_counts[category]["article_count"] += 1

    # TODO: implement this
    def update_publication_counts():
        pass

    # TODO: implement this
    def update_citations_per_article_count():
        pass

    # TODO: implement this
    def extract_authors_and_articles(self, path):
        # TODO: implement logic to extract authors and articles via looking at the json
        author_match = self.author_pattern.search(path)
        article_match = self.article_pattern.search(path)

        if author_match and article_match:
            author = author_match.group(1)[1:].strip()
            article = article_match.group(1).replace("_", " ").strip()
            return author, article
        print("Extract authors and articles didn't find what it was looking for")
        return None, None


if __name__ == "__main__":
    # Load json data
    json_path = "../Utilities/file_paths.json"
    wos_cat = WosCategorization()
    with open(json_path, "r") as file:
        data = json.load(file)
        # print(data)
        wos_cat.entries_to_categorize(data)

    category_counts = wos_cat.get_category_counts()
    print(category_counts)
