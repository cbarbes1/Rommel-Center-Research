import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


class DataScraper:
    def __init__(self, url: str):
        self.url = url
        self.list = []

    def loadRSS(self):
        resp = requests.get(self.url)

        with open("feed.xml", "wb") as file:
            file.write(resp.content)

    def parseRSS(self, keyword):
        tree = ET.parse("feed.xml")
        root = tree.getroot()

        locs = tree.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
        link_list = [loc.text for loc in locs if keyword in loc.text]

        self.list = link_list

    def scrapeSites(self):

        response = requests.get(self.list[0])
        soup = BeautifulSoup(response.content, "html.parser")
        print(soup.find("main"))


if __name__ == "__main__":
    data = DataScraper("https://www.salisbury.edu/sitemap.xml")
    data.loadRSS()
    keyword = "faculty-and-staff.aspx"
    data.parseRSS(keyword)
    data.scrapeSites()
