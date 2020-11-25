import math

pi_file_path=".\pi.txt"
with open(pi_file_path) as file_object:
    pi_number=file_object.read()

#print(pi_number)
birthday="1009"

if birthday in pi_number:
    print("hurra")