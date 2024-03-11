"""

!!!DO NOT USE!!!

This is just a dump of methods and other things no longer needed but that I want to keep track of in case I need to reference them for any reason in the future

"""

import re


class DeprecatedFunctions:
    def get_author(self, entry):
        """
        Extracts the author of the article from the entry, considering the format "last name, first name middle initial."

        Arguments:
            entry (str): The text of the article entry from which to extract the author.

        Returns:
            tuple: A tuple where the first element is a boolean indicating if the author was found,
                and the second element is the author itself if found, or None otherwise.
        """
        match = re.search(self.author_pattern, entry, re.DOTALL)
        if match:
            return True, match.group(1).strip()
        return False, None

    def get_title(self, entry):
        """
        Extracts the title of the article from the entry.

        Arguments:
            entry (str): The text of the article metadata entry from which to extract the title.

        Returns:
            tuple: A tuple where the first element is a boolean indicating if the title was found,
                and the second element is the title itself if found, or None otherwise.
        """
        match = re.search(self.title_pattern, entry, re.DOTALL)
        if match:
            return True, match.group(1).strip()
        return False, None

    def get_abstract(self, entry):
        """
        Extracts the abstract of the article from the entry.

        Arguments:
            entry (str): The text of the article entry from which to extract the abstract.

        Returns:
            tuple: A tuple where the first element is a boolean indicating if the abstract was found,
                and the second element is the abstract itself if found, or None otherwise.
        """
        match = re.search(self.abstract_pattern, entry, re.DOTALL)
        if match:
            return True, match.group(1).strip()
        return False, None
