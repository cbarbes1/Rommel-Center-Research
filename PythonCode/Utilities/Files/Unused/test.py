import re

sample_text = "[Cottingham, Andrea; Purohit, Abhishek; Benner, Jeffrey; Miller, Jenna; Falcone, Gianna; Habay, Stephen] Salisbury Univ, Dept Chem, Salisbury, MD USA."
dept_pattern = re.compile(r"Salisbury Univ, Dept (.*?)(,|$)")
match = dept_pattern.search(sample_text)

if match:
    print(f"Match found: {match.group(1)}")
else:
    print("No match found.")

print(f"MATCH GROUP 0: {match.group(0)}")
print(f"MATCH GROUP 1: {match.group(1)}")
