from __old.addressextractor import DataLoader


# address_list = DataLoader().getAddressList("US", "WY")
#
# print(address_list)

# print(DataLoader().load_data("36a Monash, Ave Nedlands WA 6009", 3))

dl = DataLoader(1)
# addresses = dl.load_data("US", "WY")
# encodings = dl.get_encodings(addresses)
# # dl.convert_back_to_address(encodings)

dl.process_text("36a Monash, Ave Nedlands WA 6009")

# dl.one_hot_encode("36a Monash, Ave Nedlands WA 6009")

#
# imdb = keras.datasets.imdb
#
# (train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)
#
# print("Training entries: {}, labels: {}".format(len(train_data), len(train_labels)))
#
# print(train_data)
# print('------------------')
# print(train_labels)
# print('------------------')
# print(imdb.load_data(num_words=10000))
