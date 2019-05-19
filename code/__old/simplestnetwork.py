# Create first network with Keras

import numpy
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten

# Fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
data_file = "../data/address_data_US_TX.csv"
training_percentage = 0.1

# Load dataset
dataset_train = numpy.loadtxt(data_file, delimiter=",")

training_data = dataset_train[0:int(len(dataset_train)*training_percentage)]

# Split into input (X) and output (Y) variables
X = dataset_train[:, 0:15]
Y = dataset_train[:, 15]

prediction_data = dataset_train[int(len(dataset_train)*training_percentage):]

# dataset_predict = numpy.loadtxt(data_file, delimiter=",")
A = prediction_data[:, 0:15]

# Create model
model = Sequential()
model.add(Dense(24, input_dim=15, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(3, activation='softmax'))

# Compile model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(X, Y, epochs=5, batch_size=10,  verbose=2)

# Calculate predictions
predictions = model.predict(A)

print("++++++++++++++++++++++++++++++++++++")
print(len(training_data))
print(len(prediction_data))
print("++++++++++++++++++++++++++++++++++++")

# Round predictions
rounded = [round(x[0]) for x in predictions]
print("###################################")
print(rounded)
print(len(rounded))
print("###################################")
