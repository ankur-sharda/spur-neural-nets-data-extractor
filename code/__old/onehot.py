import keras as keras
from keras.preprocessing.text import Tokenizer

text = "36a Monash Ave, Nedland WA 6009"

tokenizer = Tokenizer(char_level=True)
encoding = keras.preprocessing.text.one_hot(text, 72)

print(encoding)
