from bs4 import BeautifulSoup

def extract_links(html: str):
    soup = BeautifulSoup(html, "html.parser")
    links = set()
    for tag in soup.find_all("a", href=True):
        links.add(tag["href"])
    return sorted(links)
