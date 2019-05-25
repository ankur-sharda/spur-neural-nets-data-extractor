import requests
import json
import keras
from bs4 import BeautifulSoup
from keras.preprocessing.text import Tokenizer


class DataLoader:

    dictionary = {}
    skip = 0

    def __init__(self, s):
        self.skip = s

    def process_text(self, text):
        # convert a list of text strings to a matrix
        result = keras.preprocessing.text.text_to_word_sequence(text)
        texts = [].append(result)
        t = Tokenizer()
        t.fit_on_texts(texts)

    def load_data(self, country_code, region_key):
        addresses = self.get_addresses(country_code, region_key)
        for addr in addresses:
            substrings = self.create_substrings(addr)
            self.populate_dictionary(substrings)
        return addresses

    def get_addresses_country(self, country_code):
        url = "http://api.tuggl.com/addresses/list/"+country_code+"?pass=boohoo"
        r = requests.get(url)
        json_addresses = r.content
        list_addresses = json.loads(json_addresses)
        addresses = []
        for addr in list_addresses:
            full_address = addr['fullAddress'].replace("\xa0", "")
            # full_address = ''.join("[*d*]" if c.isdigit() else c for c in full_address)
            addresses.append(full_address)
        return addresses

    def get_addresses(self, country_code, region_key):
        url = "http://api.tuggl.com/addresses/list/"+country_code+"/"+region_key+"?pass=boohoo"
        r = requests.get(url)
        json_addresses = r.content
        list_addresses = json.loads(json_addresses)
        addresses = []
        for addr in list_addresses:
            full_address = addr['fullAddress'].replace("\xa0", "")
            # full_address = ''.join("[*d*]" if c.isdigit() else c for c in full_address)
            addresses.append(full_address)
        return addresses

    def create_substrings(self, address):
        substrings = []
        for i in range(len(address)):
            end = i + self.skip
            substring = address[i:end]
            if len(substring) == self.skip:
                substrings.append(substring)

        return substrings

    def populate_dictionary(self, substrings):
        for str in substrings:
            size = len(self.dictionary)+1
            if not str in self.dictionary:
                self.dictionary[str] = size

    def get_encodings(self, address):
        encodings = []
        substrings = self.create_substrings(address)
        for str in substrings:
            val = self.dictionary.get(str)
            if val is None:
                val = 0
            encodings.append(val)
        return encodings

    def get_page_slices(self, url):
        r = requests.get(url)
        soup = s(r.content)
        content = soup.text
        content = content.replace("  ", "")
        # We assume here that x is an int and > 0
        substrings = []
        jump = 15
        i = 0
        for char in content:
            sub = content[i:i + jump].strip()
            substrings.append(sub)
            i = i + jump
        substrings = [x for x in substrings if x != '']
        return substrings

    # def get_encodings(self, addresses):
    #     for addr in addresses:
    #         encodings.append(self.get_encodings_for_address(addr))
    #     return encodings

    # def convert_back_to_address(self, encodings):
    #     addresses = []
    #     for value in np.ndenumerate(encodings):
    #         addresses.append(self.convert_encoding_to_address(value))
    #     return addresses
    #
    # def convert_encoding_to_address(self, encoding):
    #     addr = ""
    #     for val in encoding:
    #         for num, str in self.dictionary.items():
    #             if str == val:
    #                 addr = addr + str
    #     return addr
