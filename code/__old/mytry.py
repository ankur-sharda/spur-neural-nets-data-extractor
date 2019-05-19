from numpy import array
from numpy import argmax
from keras.utils import to_categorical

# define example
address = "36a Monash Ave, Nedlands 6009"
data = list(address)
data = array(data)

# one hot encode
encoded = to_categorical(data, dtype='str')

# invert encoding
inverted = argmax(encoded[0])

from keras.preprocessing.text import Tokenizer
tokenizer = Tokenizer(char_level=True)
tokenizer.fit_on_texts(data)
sequence_of_int = tokenizer.texts_to_sequences(data)

print(sequence_of_int)