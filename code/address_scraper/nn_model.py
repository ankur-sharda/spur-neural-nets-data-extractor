# here we train a neural network model
# then we save it to a file
# or a MongoDB database with pickle

class NeuralNetworkModel:

    name = ''

    def __init__(self, name):
        self.name = name

    def train(self, matrix):
