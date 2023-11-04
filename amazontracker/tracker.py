import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.co.uk/dp/B093T7F1YP'
HEADERS = {"User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
PRICE = 160

def getPrice():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle')
    price = soup.find('a-price-whole')
    print(title)
    print(price)
    print(page.content)

if __name__ == "__main__":
    getPrice()