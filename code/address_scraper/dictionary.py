from address_scraper.pickle_dict import PickleDict
import requests
import json


class Dictionary:

    data = {}
    file_stub = ""

    def __init__(self, stub):
        self.file_stub = stub

    def build(self, input):
        pd = PickleDict(self.file_stub)
        self.data = pd.read()
        for t in input:
            substrings = self.list_substrings(t, 2)
            self.populate_dictionary(substrings)
        pd.save(self.data)

    def save(self):
        pd = PickleDict(self.file_stub)
        pd.save(self.data)

    def get(self):
        pd = PickleDict(self.file_stub)
        self.data = pd.read()
        return self

    def read(self):
        pd = PickleDict(self.file_stub)
        return pd.read()

    def list_substrings(self, text, skip):
        substrings = []
        for i in range(len(text)):
            end = i + skip
            substring = text[i:end]
            if len(substring) == skip:
                substrings.append(substring)
        return substrings

    def get_addresses(self, country_code, region_key):
        url = "http://api.tuggl.com/addresses/list/" + country_code + "/" + region_key + "?pass=boohoo"
        r = requests.get(url)
        json_addresses = r.content
        list_addresses = json.loads(json_addresses)
        addresses = []
        for addr in list_addresses:
            full_address = addr['fullAddress'].replace("\xa0", "")
            addresses.append(full_address)
        return addresses

    def populate_dictionary(self, substrings):
        for text in substrings:
            # text = "".join(str(text))  # do this in case the str is actually a list
            if text not in self.data:
                size = len(self.data) + 2
                self.data[text] = size
