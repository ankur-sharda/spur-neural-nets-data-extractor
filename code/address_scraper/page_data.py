import requests
from bs4 import BeautifulSoup as Soup


class PageData:

    def read_webpage_content(self, url):
        response = requests.get("http://api.tuggl.com/scrape/page-text?url=" + url + "&pass=boohoo")
        # print(response.content)
        return response.content.decode('utf-8')

    def convert_page_content_substrings(self, content, cut):
        substrings = []
        for i in range(len(content)):
            sub = content[i:i + cut]
            if len(sub) == cut:
                substrings.append(sub)
        return substrings

    def read_and_process_webpage(self, url, cut):
        content = self.read_webpage_content(url)
        content = content.replace("Alabama", "AL")
        substrings = self.convert_page_content_substrings(content, cut)
        return substrings

    def get_page_elements(self, url):
        response = requests.get(url)
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
