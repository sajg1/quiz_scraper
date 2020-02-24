import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

counter = 1
animal_quiz_url = "https://pubquizquestions.net/questions/animals/page-1"

# opens the connection and grabs the webpage
uClient = urlopen(animal_quiz_url)

page_html = uClient.read()

uClient.close()

# parses html
page_soup = soup(page_html, "html.parser")

# finds the last page number in order to control the while loop
total_pages = int(page_soup.findAll("b")[1].text)

# Question category
category = page_soup.find("section", {"id":"page-title"}).h1.text

# writing data to csv
filename = "animal_quiz_questions.csv"
f = open(filename, 'w')
headers = "category, question, answer\n"
f.write(headers)

while counter <= total_pages:

    uClient = urlopen(animal_quiz_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("tr")
    # use iter and next in order to skip the first tr element as it contains the headers "Question" and "Answer"
    iter_containers = iter(containers)
    next(iter_containers)

    for container in iter_containers:
        question = container.span.text
        answer = container.strong.text
        f.write(category + "," + question.replace(",", "|") .strip()+ "," + answer.replace(",", "|").strip() + "\n")
        # print("Question: ", question)
        # print("Answer: ", answer)
    print(counter)
    counter += 1
    animal_quiz_url = "https://pubquizquestions.net/questions/animals/page-" + str(counter)
f.close()
