import random
import os
import time


#Function to declare empty 2D table which works as space with border where "x" can move
def declare_empty_table(window_size):
    two_dimension_array=[]
    for i in range (0,window_size):
       two_dimension_array.append([])
       for j in range(0, window_size):
           two_dimension_array[i].append(" ")

    #write border in table
    for i in range(0,window_size):
        two_dimension_array[0][i]="_"
        two_dimension_array[window_size-1][i]="-"
    for i in range (1,window_size-1):
        two_dimension_array[i][0]="|"
        two_dimension_array[i][window_size-1]="|"
    return two_dimension_array

#Function to print current status of 2D table showing borders and "x" position
def print_table(two_dimension_array,curr_position_x,curr_position_y):
    two_dimension_array[curr_position_x][curr_position_y]="x"

    for i in range (0,window_size):
        current_line=""
        for j in range (0,window_size):
            current_line=current_line+str(two_dimension_array[i][j])
        print(current_line)

    

#Set "x" start position
curr_position_x=5
curr_position_y=5

#Set windows size where are borders
window_size=10

two_dimension_array=declare_empty_table(window_size)
print_table(two_dimension_array,curr_position_x,curr_position_y)

while True:
    position_move_x=0
    position_move_y=0
    #Generate random direction of "x" to move. It cannot stay in the same place
    while position_move_x == 0 and position_move_y == 0:
        position_move_x=random.randrange(-1,2)
        position_move_y=random.randrange(-1,2)
    #Calculate next position of "x"
    next_position_x=curr_position_x-position_move_x
    next_position_y=curr_position_y-position_move_y

    #Check if "x" do not move on border. If it does then calculate random next position again.
    if next_position_x == 0 or next_position_x == (window_size-1):
        continue
    elif next_position_y == 0 or next_position_y == (window_size-1) :
        continue

    two_dimension_array=declare_empty_table(window_size)
    os.system('cls')
    print_table(two_dimension_array,next_position_x,next_position_y)
    curr_position_x=next_position_x
    curr_position_y=next_position_y
    
    time.sleep(0.1)
        
    
    
    
