from bs4 import BeautifulSoup as Soup
import requests


# snippet = "<p class='store-list-address'>136 Market Place<br />San Ramon, CA 94583</p>"
# snippet = snippet.replace("<br/>", " ")
# snippet = snippet.replace("<br />", " ")
# soup_string = soup(snippet, features="lxml")
#
# print(soup_string.)

response = requests.get("https://oakmountainhobbies.com/contact-us/")
soup = Soup(response.content.decode('utf-8'), features='lxml')
elements = soup.html.findAll("div")
elements.extend(soup.html.findAll("p"))
elements.extend(soup.html.findAll("span"))

texts = []

for e in elements:
    if e.text != "":
        print("--------")
        text = e.text.strip().replace("Alabama", "AL")
        texts.append(text)
        print(text)
