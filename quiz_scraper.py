import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

animal_quiz_url = "https://pubquizquestions.net/questions/animals"

# opens the connection and grabs the webpage
uClient = urlopen(animal_quiz_url)

page_html = uClient.read()

uClient.close()

# parses html
page_soup = soup(page_html, "html.parser")
