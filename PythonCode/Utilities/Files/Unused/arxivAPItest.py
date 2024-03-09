import arxiv
import requests

"""search = arxiv.Search(
    query = "Determining the most recent common ancestor in a finite linear habitat with asymmetric dispersal",
    max_results = 5,
    sort_by = arxiv.SortCriterion.Relevance
)

for result in arxiv.Client().results(search):
    print(f"TITLE: {result.title}\nAUTHORS: {result.authors}\nCATEGORIES: {result.categories}\nPRIM_CATEGORY: {result.primary_category}\nSUMMARY: {result.summary}\n")"""

"""import urllib.request as libreq
with libreq.urlopen('http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1') as url:
    r = url.read()
print(r)"""

"""

url = "https://export.arxiv.org/api/query?"

search_params = {
    "search_query": "all:electron",
    "start": 0,
    "max_results": 3,
    "sortBy": "submittedDate",
    "sortOrder": "descending"
}

response = requests.get(url, params=search_params)

print(response.text)"""


url = "https://export.arxiv.org/api/classify"

file_path = "./document.pdf"

with open(file_path, "rb") as file:
    response = requests.post(url, files={"file": file})

print(response.text)
