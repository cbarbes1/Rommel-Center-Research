import re
import warnings

class AttributeExtractionStrategy:
    def extract_attribute(self, entry_text):
        pass

    def extract_c1_content(self, entry_text):
        """
        Extracts the 'C1' content from the entry text.

        Parameters:
            entry_text (str): The text of the entry from which to extract the 'C1' content.

        Returns:
            str: The extracted 'C1' content or an empty string if not found.
        """
        c1_content = []
        entry_lines = entry_text.splitlines()
        for line in entry_lines:
            if "Salisbury Univ" in line:
                # Extract everything inside the brackets
                start = line.find("[")
                end = line.find("]")
                if start != -1 and end != -1:
                    c1_content.append(line[start + 1 : end])
                break
        return "\n".join(c1_content)

    def split_salisbury_authors(self, salisbury_authors):
        """
        Splits the authors string at each ';' and stores the items in a list.

        Parameters:
            authors_text (str): The string containing authors separated by ';'.

        Returns:
            list: A list of authors.
        """
        return [
            salisbury_author.strip()
            for salisbury_author in salisbury_authors.split(";")
        ]
        
    def extract_dept_from_c1(self, entry_text):
        """
        Extracts department and school names from the 'C1' content in the entry text.

        Parameters:
            entry_text (str): The text of the entry from which to extract the content.

        Returns:
            str: Extracted department and school names or an empty string if not found.
        """
        c1_content = []
        capturing = False
        entry_lines = entry_text.splitlines()
        for line in entry_lines:
            if line.startswith("C1"):
                capturing = True
            elif line.startswith("C3"):
                capturing = False
            if capturing and "Salisbury" in line:
                # Extract department and school names
                dept_match = re.search(self.dept_pattern, line)
                dept_match_alt = re.search(self.dept_pattern_alt, line)
                if dept_match:
                    c1_content.append(dept_match.group(1))
                elif dept_match_alt:
                    c1_content.append(dept_match_alt.group(1))
        # return '\n'.join(c1_content)
        return c1_content        
        
    
class AuthorExtractionStrategy(AttributeExtractionStrategy):
    def __init__(self):
        self.author_pattern = re.compile(r"AF\s(.+?)(?=\nTI)", re.DOTALL)
        
    def extract_attribute(self, entry_text):        
        author_c1_content = self.extract_c1_content(entry_text)

        # Use the get_salisbury_authors method to extract authors affiliated with Salisbury University
        salisbury_authors = self.split_salisbury_authors(author_c1_content)
        
        result = ()
        
        if salisbury_authors:
            result = (True, salisbury_authors)
        else:
            result = (False, None)
            warnings.warn(
                "Attribute: 'Author' was not found in the entry", RuntimeWarning
            )
        
        return result
    
class DepartmentExtractionStrategy(AttributeExtractionStrategy):
    def __init__(self):
        self.dept_pattern = re.compile(r"Dept (.*?)(,|$)")
        self.dept_pattern_alt = re.compile(r"Dept, (.*?) ,")

    def extract_attribute(self, entry_text):
        departments = self.extract_dept_from_c1(entry_text)
        return (True, departments) if departments else (False, None)
    
class WosCategoryExtractionStrategy(AttributeExtractionStrategy):
    def __init__(self):
        self.wc_pattern = re.compile(r"WC\s+(.+?)(?=\nWE)", re.DOTALL)
    
    def extract_attribute(self, entry_text):
        match = self.wc_pattern.search(entry_text)
        if match:
            categories = self.wos_category_splitter(match.group(1).strip())
            for i, category in enumerate(categories):
                category = re.sub(r"\s+", " ", category)
                categories[i] = category
            return True, categories
        warnings.warn(
            f"Attribute: 'WoS_Category' was not found in the entry", RuntimeWarning
        )
        return False, None
    
    def wos_category_splitter(self, category_string):
        """
        Splits a string of Web of Science (WoS) categories into a list of individual categories.

        This method is specifically designed to process strings where categories are separated by semicolons (';').
        It strips any leading or trailing whitespace from each category after splitting.

        Parameters:
            category_string (str): The string containing the categories, with each category separated by a semicolon (';').

        Returns:
            list: A list of strings, where each string is a trimmed category extracted from the input string.
        """
        return [category.strip() for category in category_string.split(";")]
    
class DefaultExtractionStrategy(AttributeExtractionStrategy):
    def __init__(self):
        self.title_pattern = re.compile(r"TI\s(.+?)(?=\nSO)", re.DOTALL)
        self.abstract_pattern = re.compile(r"AB\s(.+?)(?=\nC1)", re.DOTALL)
        self.end_record_pattern = re.compile(r"DA \d{4}-\d{2}-\d{2}\nER\n?", re.DOTALL)
        
    def extract_attribute(self, attribute, entry_text):
        """
        Extracts a single attribute from the entry text based on predefined patterns.

        Parameters:
            attribute (str): The name of the attribute to extract.
            entry_text (str): The text of the entry from which to extract the attribute.

        Returns:
            tuple: A tuple containing a boolean indicating whether the extraction was successful,
            and the extracted attribute value or None.
        """
        match = re.search(attribute, entry_text)
        if not match: 
            warnings.warn(
                f"Attribute: '{attribute}' was not found in the entry", RuntimeWarning
            )
            return False, None
        return True, match.group(1).strip()