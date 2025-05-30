
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.thegradcafe.com/survey/?q=Computer+Science"

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.title.string)

