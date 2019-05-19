# https://www.youtube.com/watch?v=wQ8BIBpya2k

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten

from tensorflow.keras.layers import Conv2D, MaxPooling2D

(x_train, y_train), (x_test, y_test) = mnist.load_data(path='mnist.npz')

print(x_train)

# #plt.imshow(x_train[0], cmap=plt.cm.binary)
# # plt.show()
#
# print(y_train[0])
#
# x_train = tf.keras.utils.normalize(x_train, axis=1)
# x_test = tf.keras.utils.normalize(x_test, axis=1)
#
# print(x_train[0])
#
# plt.imshow(x_train[0], cmap=plt.cm.binary)
# # plt.show()
#
# print(y_train[0])
#
# x_train = tf.keras.utils.normalize(x_train, axis=1)
# x_test = tf.keras.utils.normalize(x_test, axis=1)
#
# print(x_train[0])
#
# plt.imshow(x_train[0], cmap=plt.cm.binary)
# # plt.show()
#
# model = tf.keras.models.Sequential()
# # model.add(tf.keras.layers.Flatten())
# # model.add(tf.keras.layers.Conv2D(32, (28, 28)))
# # model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
# # model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
#
# X = X/255.0
#
# model.add(Conv2D(256, (3, 3), input_shape=X.shape[1:]))
# model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
#
# model.add(Conv2D(256, (3, 3)))
# model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
#
# model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
# model.add(Dense(64))
#
# model.add(Dense(1))
# model.add(Activation('sigmoid'))
#
#
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#
# model.fit(x_train, y_train, epochs=3)
#
# val_loss, val_acc = model.evaluate(x_test, y_test)
# print(val_loss)
# print(val_acc)
#
# model.save('epic_num_reader.model')
#
# new_model = tf.keras.models.load_model('epic_num_reader.model')
#
# predictions = new_model.predict(x_test)
#
# print(predictions)
#
# print(np.argmax(predictions[0]))
#
# plt.imshow(x_test[0], cmap=plt.cm.binary)
# plt.show()

