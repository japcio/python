import random
import os
import time

#Function to declare empty 2D table which works as space with border where "x" can move
def declare_empty_table(window_size):
    snake_board=[]
    for i in range (0,window_size):
       snake_board.append([])
       for j in range(0, window_size):
           snake_board[i].append(" ")

    #write border in table
    for i in range(0,window_size):
        snake_board[0][i]="_"
        snake_board[window_size-1][i]="-"
    for i in range (1,window_size-1):
        snake_board[i][0]="|"
        snake_board[i][window_size-1]="|"
    return snake_board

#Function to print current status of 2D table showing borders and "x" position
def print_table(snake_board,snake_length=4,curr_x=7,curr_y=7,position_move_x=0,position_move_y=0,snake_body_position=""):
    #Check if last position dictionary is not empty
    if snake_body_position:
        new_head_position_x=curr_x+position_move_x
        new_head_position_y=curr_y+position_move_y
        snake_board[new_head_position_x][new_head_position_y]="o"
        #Declare new snake body position table after head move
        new_snake_body_position=["z" for i in range(0, len(snake_body_position))]
        new_snake_body_position[0]=str(new_head_position_x)+","+str(new_head_position_y)
        #Head is already printed by line above. Now we need to move body. 
        for i in range (1,len(snake_body_position)):
            new_snake_body_position[i]=snake_body_position[i-1]
    #This is first round
    else: 
        #Draw snake head
        snake_board[curr_x][curr_y]="o"
        snake_body_position.append(str(curr_x)+","+str(curr_y))
        for i in range (1,snake_length):
            snake_body_position.append(str(curr_x)+","+str(curr_y-i))
        new_snake_body_position=snake_body_position
    #Add snake body after move to snake_board. Head is already added
    for i in range (1,len(new_snake_body_position)):
        current_line=""
        current_body_element_position=new_snake_body_position[i]
        #Split current_body_element_position into x and y coordinates
        current_body_element_position=current_body_element_position.split(",")
        snake_board[int(current_body_element_position[0])][int(current_body_element_position[1])]="x"
    #print whole snake_board which contains snake body
    for i in range (0,window_size):
        current_line=""
        for j in range (0,window_size):
            current_line=current_line+str(snake_board[i][j])
        print(current_line)

    #return new_snake_body_position table
    return new_snake_body_position
    

#Set "x" start position
curr_x=7
curr_y=7

#Set windows size where are borders
window_size=25

snake_length=8
snake_body_position=[]

snake_board=declare_empty_table(window_size)
print_table(snake_board,snake_length,curr_x,curr_y,0,0,snake_body_position)

while True:
    position_move_x=0
    position_move_y=0
    #Generate random direction of "x" to move. It cannot stay in the same place
    while position_move_x == 0 and position_move_y == 0:
        position_move_x=random.randrange(-1,2)
        position_move_y=random.randrange(-1,2)
    #Calculate next position of "x"
    next_x=curr_x+position_move_x
    next_y=curr_y+position_move_y
    #check if snake is not blocked by itself
    if snake_board[curr_x-1][curr_y] != " " and snake_board[curr_x+1][curr_y] != " " and snake_board[curr_x][curr_y-1] != " " and snake_board[curr_x][curr_y+1] != " ":
        for seconds in range(0,4):
            print(f"No possible moves. Reset in: {4-seconds}")
            time.sleep(1)
        curr_x=7
        curr_y=7
        snake_body_position=[]
        snake_board=declare_empty_table(window_size)
        print_table(snake_board,snake_length,curr_x,curr_y,0,0,snake_body_position)
        continue
    #Check if "x" do not move on border. If it does then calculate random next position again.
    elif next_x == 0 or next_x == (window_size-1):
        continue
    elif next_y == 0 or next_y == (window_size-1) :
        continue
    elif snake_board[next_x][next_y] != " ":
        continue
    #do not allow move -1,-1 or 1,1 or -1,1
    elif position_move_x*position_move_y != 0:
        continue

    
    snake_board=declare_empty_table(window_size)
 
    os.system('cls')
    snake_body_position=print_table(snake_board,snake_length,curr_x,curr_y,position_move_x,position_move_y,snake_body_position)
    curr_x=next_x
    curr_y=next_y
    
    time.sleep(0.1)
        
    
    
    
