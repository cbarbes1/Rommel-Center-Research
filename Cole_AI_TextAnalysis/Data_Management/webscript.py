import urllib.request
import re

fid = urllib.request.urlopen(
    "https://www.salisbury.edu/faculty-and-staff/#isFaculty=1&dept=&ltr=&page=1&pagesize=10"
)
webpage = fid.read().decode("utf-8")

print(webpage[:1000000])
# tag = "ol"

# reg_str = "<" + tag + ">(.*?)</"+tag+">"
# res = re.findall(reg_str, webpage)

# print("The strings extracted : "+str(res))
