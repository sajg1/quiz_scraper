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

containers = page_soup.findAll("tr")
# use iter and next in order to skip the first tr element as it contains the headers "Question" and "Answer"
iter_containers = iter(containers)
next(iter_containers)

for container in iter_containers:
    question = container.span.text
    answer = container.strong.text
    print("Question: ", question)
    print("Answer: ", answer)
