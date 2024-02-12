import re
import os
import json
import sys
sys.path.append('/mnt/linuxlab/home/spresley1/Desktop/425testing/ResearchNotes/Rommel-Center-Research/PythonCode/Utilities')

from utilities import Utilities

class WosCategorization():
    
    def __init__(self):
        self.utils = Utilities()
        self.category_counts = {}
        
    def load_counts(self, json_file_path):
        try:
            with open(json_file_path, 'r') as file:
                self.category_counts = json.load(file)
        except FileNotFoundError:
            self.category_counts = {}
    
    def save_counts(self, json_file_path):
        with open(json_file_path, 'w') as file:
            json.dump(self.category_counts, file, indent=4)
    
    def entries_to_categorize(self, entries):
        for entry, path in entries.items():
            print(f"Processing {entry}: {path}")
            categories_for_entry = self.utils.get_wos_categories(path)
            processed_authors = set()
            processed_artices = set()
            
            for category in categories_for_entry:
                self.process_category(category, path, processed_authors, processed_artices)
            
    def process_category(self, category, path, processed_authors, processed_articles):
        authors, articles = self.extract_authors_and_articles(path)
        
        # Initialize category in dictionary if not present
        if category not in self.category_counts:
            self.category_counts[category] = {'falculty_count':0, 
                                              'department_count':0, 
                                              'article_count':0}
        for author in authors:
            if author not in processed_authors:
                self.update_faculty_count(category)
                #TODO: in update faculty check if department exists yet if not add it
                processed_authors.add(author)
            
        for article in articles:
            if article not in processed_articles:
                self.update_article_count(category)
                processed_articles.add(article)
    
    def update_faculty_count(self, category):
        self.category_counts[category]['faculty_count'] += 1
           
    def update_department_count(self, category):
        self.category_counts[category]['department_count'] += 1
        
    def update_article_count(self, category):
        self.category_counts[category]['article_count'] += 1
    
    #TODO: implement this    
    def update_publication_counts():
        pass
    
    #TODO: implement this
    def update_citations_per_article_count():
        pass
    
    def extract_authors_and_articles(self, path):
        #TODO: implement logic to extract authors and articles via looking at the json
        
if __name__ == "__main__":
    # Load json data
    json_path = '../Utilities/file_paths.json'
    with open(json_path, 'r') as file:
        data = json.load(file)
    wos_cat = WosCategorization()
    wos_cat.entries_to_categorize(data)
    
    