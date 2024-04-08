import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def scrape_arxiv_categories(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # # Find all 'a' tags with class 'link-subtle'
    category_tags = soup.find_all('h2', class_='accordion-head')

    # Extract the category code and name from each tag
    categories = {}
    for tag in category_tags:
        code = tag.text.strip()
        name = tag.find_next_sibling('div').text.strip() if tag.find_next_sibling('span') else None
        categories[code] = name

    return categories


def scrape_salisbury_faculty(url):
    response = requests.get(url)

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode, i.e., without opening a browser window
    options.add_argument('--disable-gpu')  # Disable GPU acceleration
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)

    time.sleep(5)

    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup)

    driver.quit()


if __name__ == "__main__":
    # url = 'https://arxiv.org/category_taxonomy'
    # categories = scrape_arxiv_categories(url)
    # for code, name in categories.items():
    #     print(f'{code}: {name}')
    url = 'https://www.salisbury.edu/faculty-and-staff/#isFaculty=1&dept=&ltr=&page=1&pagesize=10'
    categories = scrape_salisbury_faculty(url)