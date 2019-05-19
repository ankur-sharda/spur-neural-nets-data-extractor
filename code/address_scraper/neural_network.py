import numpy
from keras.models import Sequential
from keras.layers import Dense
from address_scraper.encoding import Encoding


class NeuralNetwork:

    model = Sequential()
    training_data = []
    prediction_data = []

    def train(self, data_file, percentage):
        seed = 7
        numpy.random.seed(seed)
        data_file = "../../data/encodings/"+data_file+".csv"
        print(data_file)

        # Load dataset
        total_data = numpy.loadtxt(data_file, delimiter=",")
        self.training_data = total_data[0:int(len(total_data) * percentage)]

        # Split into input (X) and output (Y) variables
        X = total_data[:, 0:20]
        Y = total_data[:, 20]

        # Create model
        self.model.add(Dense(24, input_dim=20, activation='relu'))
        self.model.add(Dense(10, activation='relu'))
        self.model.add(Dense(2, activation='softmax'))

        # Compile model
        self.model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        # Fit the model
        self.model.fit(X, Y, epochs=5, batch_size=10, verbose=2)

    def predict(self, file, percentage):
        file = "../../data/encodings/" + file+".csv"
        total_data = numpy.loadtxt(file, delimiter=",")
        # Calculate predictions
        self.prediction_data = total_data[0:int(len(total_data) * percentage)]

        print(len(self.training_data))
        print(len(self.prediction_data))

        A = self.prediction_data[:, 0:20]
        predictions = self.model.predict(A)

        print(predictions)

        for a in A:
            print("".join(Encoding("single_address").decode(a)))

        # Round predictions
        rounded = [round(x[0]) for x in predictions]
        print(rounded)
