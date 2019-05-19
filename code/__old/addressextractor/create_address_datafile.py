# We want to create a file of address data
# the first n columns will represent the letters
# the last column will be a 0 or 1 to represent whether it is the start or end of an address
# for now we will not consider the case where the input is not the start or end of an address

# Q: How do we handle the variable length situation
import csv
from __old.addressextractor import DataLoader

country_code = "US"
region_key = "NY"

dl = DataLoader(1)

data_file = '../../data/address_data_'+country_code+'_'+region_key+'.csv'

addresses = dl.get_addresses(country_code, region_key)

# Build the dictionary
for addr in addresses:
    dl.populate_dictionary(dl.create_substrings(addr))

# We only want encodings for the starts and ends of the addresses

starts_encoded = []
ends_encoded = []
data = []

for addr in addresses:
    start = addr[0:15]
    length = len(addr)
    end = addr[length-15:length]

    start_encoded = dl.get_encodings(start)
    end_encoded = dl.get_encodings(end)

    starts_encoded.append(start_encoded)
    ends_encoded.append(end_encoded)

    start_encoded.append(0)
    end_encoded.append(1)
    data.append(start_encoded)
    data.append(end_encoded)

page_url = 'https://realpython.com/python-keras-text-classification/'
substrings = dl.get_page_slices(page_url)
print(substrings)

for sub in substrings:
    encodings = dl.get_encodings(sub)
    if len(encodings) < 15:
        space = 15 - len(encodings)
        for i in range(space):
            encodings.append(0)
    print(len(encodings))
    encodings.append(2)
    data.append(encodings)

print(data)

with open(data_file, 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(data)



