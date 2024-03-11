import re


class C1ContentExtractor:
    def extract_c1_content(self, entry_text):
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
                dept_match = re.search(r"Dept (.*?)(,|$)", line)
                if dept_match:
                    c1_content.append(dept_match.group(1))
        # return '\n'.join(c1_content)
        return c1_content


def main(file_path):
    with open(file_path, "r") as file:
        entry_text = file.read()
    extractor = C1ContentExtractor()
    extracted_content = extractor.extract_c1_content(entry_text)
    print("Extracted Content:\n", extracted_content)


if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")
    main(file_path)
