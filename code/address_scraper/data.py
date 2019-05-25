from bs4 import BeautifulSoup
import requests
import json


class Data:

    def load_single_address(self, address):
        texts = []
        texts.append(address)
        return texts

    def load_multi_address(self, addresses):
        texts = []
        for a in addresses:
            texts.append(a)
        return texts

    def load_addresses(self, country_code, region_key):
        texts = []
        url = "http://api.tuggl.com/addresses/list/" + country_code + "/" + region_key + "?pass=boohoo"
        r = requests.get(url)
        json_addresses = r.content
        list_addresses = json.loads(json_addresses)
        for addr in list_addresses:
            full_address = addr['fullAddress'].replace("\xa0", "")
            texts.append(full_address)
        return texts
