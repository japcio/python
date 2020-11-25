import json

numbers=[2,3,5,7,11,13]
filename='numbers.json'
with open(filename,'w') as file:
    json.dump(numbers,file)


with open(filename) as file:
    load_numbers=json.load(file)

print("load_nubmers: {load_numbers[2]}")

filename2='numbers.txt'
with open(filename2,'w') as file:
    file.write(str(numbers))


with open(filename2) as file:
    load_numbers2=file.read()

print(load_numbers2[2])



