"""my_dict = {
    "name": ["jude", "spencer", "will"],
    "age": "20, 57, 21"
}

print(my_dict)

print(my_dict.keys())

print(my_dict["name"])

jude = my_dict["name"][0]
print(jude)

spencer = my_dict["name"][1]
print(spencer)


category = {
    "math": {"facultycount": 3, "depcount":2}
}
print(category)

print(category["math"]["facultycount"])

for key in category:
    key_i = key
    print(category)
    fac_count = category[key_i]["facultycount"]
    print(fac_count)
    dep_count = category[key_i]["depcount"]
    print(dep_count)"""
    
  
    
class CategoryStuff:
    def __init__(self):
        self.category_dict = {
            "math": {"facultycount": 3, "depcount":2},
            "computerScience": {"facultycount": 5, "depcount": 3}
            }
    def get_category_info(self, category_name):
        return self.category_dict[category_name]
    
mystuff = CategoryStuff()

csStuff = mystuff.get_category_info("computerScience")
print(csStuff)

cs_fac_count = csStuff["facultycount"]
print(f"Coumputer Science Faculty Count: {cs_fac_count}")

cs_dep_count = csStuff["depcount"]
print(f"Computer Science Department Count: {cs_dep_count}")





