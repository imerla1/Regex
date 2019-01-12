import re


with open('data.txt', 'r') as file:

    content = file.readlines()

    names = []
    counter = 0

    while counter < len(content):
        names.append(content[counter])
        counter += 5
with open('data.txt', 'r') as file:

    matches = file.read()


address = re.compile(r'[0-9]+\s\w+\sSt.,\s\w+\s\w+\s[0-9]+').findall(matches)
email = re.compile(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+[.]+[a-zA-Z]+').findall(matches)
phone_number = re.compile(r'\d{3}.\d{3}.\d{4}').findall(matches)
new_names = []


Info_dict = {}

for na, ad, ph, em in zip(names, address, phone_number, email):
    Info_dict[na] = {'address': ad, 'phone_number':ph, 'email':em}

