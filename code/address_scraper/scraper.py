from address_scraper.dictionary import Dictionary
from address_scraper.data import Data
from address_scraper.encoding import Encoding
from address_scraper.neural_network import NeuralNetwork


class Scraper:

    # This is where we run the address scraper

    c1 = "US"
    r1 = "TX"

    addresses1 = Data().load_addresses(c1, r1)

    addresses = []
    addresses.append("523 Thompson Ln, Austin, TX, 78742")
    addresses.append("5510 Weslayan Street, Houston, TX 77005")
    addresses2 = Data().load_multi_address(addresses)

    dict = Dictionary("dict")
    dict.build(addresses1)
    dict.build(addresses2)

    enc1 = Encoding("addresses_"+c1+"_"+r1)
    enc1.encode_list(dict, addresses1)

    enc2 = Encoding("single_address")
    enc2.encode_list(dict, addresses2)

    nn = NeuralNetwork()
    nn.train("addresses_"+c1+"_"+r1, 1)
    nn.predict("single_address", 1)


# from address_scraper.dictionary import Dictionary
# from address_scraper.data import Data
# from address_scraper.encoding import Encoding
# from address_scraper.neural_network import NeuralNetwork
#
#
# class Scraper:
#
#     # This is where we run the address scraper
#
#     c1 = "US"
#     r1 = "TX"
#
#     c2 = "US"
#     r2 = "CA"
#
#     c1 = "US"
#     c2 = "WY"
#
#     train__addresses = Data().load_addresses(c1, r1)
#     predict_addresses = Data().load_addresses(c2, r2)
#
#     # addresses = []
#     # addresses.append("523 Thompson Ln, Austin, TX, 78742")
#     # addresses.append("5510 Weslayan Street, Houston, TX 77005")
#     # addresses2 = Data().load_multi_address(addresses)
#
#     dict = Dictionary("dict")
#     dict.build(train__addresses)
#     dict.build(predict_addresses)
#
#     enc1 = Encoding("train_addresses")
#     enc1.encode_list(dict, train__addresses)
#
#     enc2 = Encoding("predict_addresses")
#     enc2.encode_list(dict, predict_addresses)
#
#     nn = NeuralNetwork()
#     nn.train("train_addresses", 1)
#     nn.predict("predict_addresses", .2)
