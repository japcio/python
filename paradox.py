#start=`date +%s`
import random

goats=0
cars=0

gate_where_is_goat=0
chosen_gate=0
number_of_tries=100
gates=3
number_of_success_change=0
number_of_success_not_change=0

try_number=1
print ("Try_number: ")
while  try_number < (number_of_tries +1):
        print (try_number,end=" ")
        #Put goat in one gate and cars in rest of gates
        gate_where_is_car=random.randint(1,gates)
        chosen_gate=random.randint(1,gates)

        #Scenario #1. NOT change gate.
        if chosen_gate == gate_where_is_car:
                number_of_success_not_change+=1
                
        #Scenario #2. Change gate.
        if chosen_gate != gate_where_is_car:
                number_of_success_change+=1
        try_number+=1

print(f"Number of tries: {number_of_tries}")
print(f"Number of all gates: {gates}")
print(f"Success rate when you NOT change gate: {(number_of_success_not_change/number_of_tries*100)}")
print(f"Success rate when you change gate: {(number_of_success_change/number_of_tries*100)}")
