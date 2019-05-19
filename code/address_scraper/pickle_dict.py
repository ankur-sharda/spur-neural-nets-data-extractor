from pathlib import Path
import pickle
import os


class PickleDict:

    file_name = ""

    def __init__(self, name):
        self.file_name = "../../data/dictionaries/"+name+".pkl"

    def read(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'xt') as f:
                f.close()

        with open(self.file_name, 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                data = {}

        return data

    def save(self, data):
        with open(self.file_name, "wb") as file:
            pickle.dump(data, file)
            file.close()


