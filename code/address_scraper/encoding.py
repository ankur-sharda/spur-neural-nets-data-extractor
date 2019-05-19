from address_scraper.dictionary import Dictionary
import csv


class Encoding:

    file_name = ""

    def __init__(self, stub):
        self.file_name = "../../data/encodings/"+stub+".csv"

    def encode_list(self, dicny, data_obj):
        encodings = []

        for text in data_obj:
            start = text[0:20]
            length = len(text)
            end = text[length - 20:length]
            start_encoded = self.encode_text(dicny, start)
            end_encoded = self.encode_text(dicny, end)
            start_encoded.append(0)
            end_encoded.append(1)
            encodings.append(start_encoded)
            encodings.append(end_encoded)
        self.save(encodings)

    def encode_list_backwards(self, dicny, data_obj):
        encodings = []

        for text in data_obj:
            start = text[0:20]
            length = len(text)
            end = text[length - 20:length]
            start_encoded = self.encode_text(dicny, start)
            end_encoded = self.encode_text(dicny, end)
            start_encoded.append(0)
            end_encoded.append(1)
            encodings.append(end_encoded)
            encodings.append(start_encoded)
        self.save(encodings)

    def encode_start(self, dicny, data_obj):
        encodings = []

        for text in data_obj:
            start = text[0:20]
            start_encoded = self.encode_text(dicny, start)
            start_encoded.append(0)
            encodings.append(start_encoded)
        self.save(encodings)

    def encode_text(self, dicny, text):
        encodings = []
        substrings = self.list_substrings(text, 1)
        for str in substrings:
            val = dicny.data.get(str, 0)
            encodings.append(val)
        return encodings

    def list_substrings(self, text, skip):
        substrings = []
        for i in range(len(text)):
            end = i + skip
            substring = text[i:end]
            if len(substring) == skip:
                substrings.append(substring)
        return substrings

    def save(self, encodings):
        with open(self.file_name, 'w') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows(encodings)

    def decode(self, encoding):
        decoding = []
        dcny = Dictionary("dict").get()
        for e in encoding:
            for key in dcny.data:
                if e == dcny.data[key]:
                    decoding.append(key)

        return decoding

