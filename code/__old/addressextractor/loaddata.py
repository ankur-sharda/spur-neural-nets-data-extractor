import sys
import json
import requests
import numpy as np

# Get the data

URL = "http://api.tuggl.com/addresses/list/US/WY?pass=boohoo"

r = requests.get(URL)
data = r.json()

alphabet = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !@#$%^&*(){}[]<>,.'
print(len(alphabet))

def oh_encode(data):

    # define universe of possible input values
    # define a mapping of chars to integers
    char_to_int = dict((c, i) for i, c in enumerate(alphabet))
    int_to_char = dict((i, c) for i, c in enumerate(alphabet))
    # integer encode input data
    integer_encoded = [char_to_int[char] for char in data]
    # print(integer_encoded)
    # one hot encode
    onehot_encoded = list()
    for value in integer_encoded:
        letter = [0 for _ in range(len(alphabet))]
        letter[value] = 1
        onehot_encoded.append(letter)

    # invert encoding

    return onehot_encoded


arr = np.array([])

i = 0

for d in data:
    # print(d)
    i = i+1
    json_string = json.dumps(d)
    obj = json.loads(json_string)
    # print(obj['fullAddress']+'')
    oh = obj['fullAddress'].replace("\xa0", "")[0:15]
    coded = oh_encode(oh)
    # print(coded)
    print([coded])
    arr = np.append(arr, [coded])
    print(i)

np.set_printoptions(threshold=sys.maxsize)
print(arr)

print(arr.shape)
print(i)


