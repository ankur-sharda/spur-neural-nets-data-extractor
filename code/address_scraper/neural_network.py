from address_scraper.encoding import Encoding
from keras.models import Sequential
from keras.layers import Dense
import random
import numpy


class NeuralNetwork:

    model = Sequential()
    training_data = []
    prediction_data = []

    def train(self, data_file, percentage):
        seed = 7
        numpy.random.seed(seed)
        data_file = "../../data/encodings/"+data_file+".csv"

        # Load dataset
        total_data = numpy.loadtxt(data_file, delimiter=",")
        self.training_data = total_data[0:int(len(total_data) * percentage)]

        random.shuffle(self.training_data)

        # Split into input (X) and output (Y) variables
        data = total_data[:, 0:20]
        labels = total_data[:, 20]

        # Create model
        self.model.add(Dense(100, input_dim=20, activation='relu'))
        self.model.add(Dense(50, activation='relu'))
        self.model.add(Dense(22, activation='relu'))
        self.model.add(Dense(12, activation='relu'))
        self.model.add(Dense(3, activation='softmax'))
        # Compile model
        self.model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        # Fit the model
        self.model.fit(data, labels, epochs=30, batch_size=128, verbose=2)

    def predict(self, file, percentage):
        file = "../../data/encodings/" + file + ".csv"
        total_data = numpy.loadtxt(file, delimiter=",")

        # Calculate predictions
        self.prediction_data = total_data[int(len(total_data) * percentage):]
        random.shuffle(self.prediction_data)

        A = self.prediction_data[:, 0:20]
        B = self.prediction_data[:, 20]


        predictions = self.model.predict(A)

        print("[Predictions]")
        print(predictions)

        print("prediction label", B[2])

        total_correct = 0
        for i in range(len(predictions)):
            first = predictions[i, 0]
            second = predictions[i, 1]
            third = predictions[i, 2]

            val = ''
            string_type = ""
            if first > second and first > third:
                string_type = '[start]'
                val = first
            if second > first and second > third:
                string_type = '[end]'
                val = second
            if third > first and third > second:
                string_type = '[other]'
                val = third

            correct_label = ''
            if B[i] == 0:
                correct_label = '[start]'
            if B[i] == 1:
                correct_label = '[end]'
            if B[i] == 2:
                correct_label = '[other]'


            is_correct = False
            if string_type == correct_label:
                is_correct = True
                total_correct = total_correct+1

            print(self.prediction_data[i])
            print(i, " ", "".join(Encoding(file).decode(self.prediction_data[i])), string_type, val, correct_label, is_correct)

        print("Total correct: "+str((total_correct/len(B)) * 100))

        # Round predictions
        # rounded = [round(x[0]) for x in predictions]
        # print("[Rounded Predictions]")
        # print(rounded)

