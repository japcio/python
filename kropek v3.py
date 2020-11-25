import random
import os
import time

#Function to declare empty 2D table which works as space with border where "x" can move
def declare_empty_table(board_size):
    snake_board=[]
    for i in range (0,board_size):
       snake_board.append([])
       for j in range(0, board_size):
           snake_board[i].append(" ")

    #write border in table
    for i in range(0,board_size):
        snake_board[0][i]="_"
        snake_board[board_size-1][i]="-"
    for i in range (1,board_size-1):
        snake_board[i][0]="|"
        snake_board[i][board_size-1]="|"
    return snake_board

#Function to print current status of 2D table showing borders and "x" position
def print_table(snake_board,snake_length=0,curr_x=5,curr_y=5,position_move_x=0,position_move_y=0,snake_body_position="",food_exist=False,food_x="", food_y="",food_eaten=0):
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
        #If head moves toward food then clear food from board and make snake longer
        if new_head_position_x == food_x and new_head_position_y == food_y:
            snake_length=snake_length+1
            food_eaten=food_eaten+1
            snake_board[food_x][food_y]=" "
            food_exist=False
            food_x=""
            food_y=""
            last_body_element_position=new_snake_body_position[-1].split(",")
            add_body_end_flag=0
            while add_body_end_flag==0:
                add_body_x=random.randrange(-1,2)
                add_body_y=random.randrange(-1,2)
                if snake_board[int(last_body_element_position[0])-int(add_body_x)][int(last_body_element_position[1])-int(add_body_y)] != " ":
                    continue
                else:
                    add_body_end_flag=1
                    new_snake_body_position.append(str(add_body_x)+","+str(add_body_y))             
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
        
    #If food not exists on board then add it
    if food_exist == False:
        food_exist, food_x, food_y=add_food(snake_body_position, board_size)
    else:
        snake_board[food_x][food_y]=food_symbol
    #print whole snake_board which contains snake body
    for i in range (0,board_size):
        current_line=""
        for j in range (0,board_size):
            current_line=current_line+str(snake_board[i][j])
        print(current_line)

    #return new_snake_body_position table
    return new_snake_body_position,food_exist,food_x, food_y,snake_length,food_eaten

def add_food(snake_body_position,board_size):
    end_flag=0
    while end_flag == 0:
        food_x=random.randrange(1,board_size-2)
        food_y=random.randrange(1,board_size-2)
        for i in range (0,len(snake_body_position)):
            current_body_element_position=snake_body_position[i]
            #Split current_body_element_position into x and y coordinates
            current_body_element_position=current_body_element_position.split(",")
            if int(current_body_element_position[0]) == food_x and int(current_body_element_position[1]) == food_y:
                break
        end_flag=1
    snake_board[food_x][food_y]=food_symbol
    food_exist=True
    return food_exist, food_x, food_y

        
    


###############################################################################################################
#MAIN   

#Set food symbol
food_symbol="@"

#Set initial food position
food_x=0
food_y=0

#Flag showing if food is on board
food_exist=False


#number of food eaten
food_eaten=0

#set snake parameters
start_snake_length=12
snake_length=start_snake_length
snake_body_position=[]


#Set windows size where are borders
board_size=20

#Set "x y" start position
curr_x=board_size-2
curr_y=board_size-2

#Check if board size is enough for snake
if snake_length>board_size-2:
    print("Snake is too long for this board")
    time.sleep(3)
    os._exit(0)

snake_board=declare_empty_table(board_size)
print_table(snake_board,snake_length,curr_x,curr_y,0,0,snake_body_position,food_exist)



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
    if snake_board[curr_x-1][curr_y] != " " and snake_board[curr_x+1][curr_y] != " " and snake_board[curr_x][curr_y-1] != " " and snake_board[curr_x][curr_y+1] != " " and snake_board[curr_x-1][curr_y] != food_symbol \
       and snake_board[curr_x+1][curr_y] != food_symbol and snake_board[curr_x][curr_y-1] != food_symbol and snake_board[curr_x][curr_y+1] != food_symbol:
        for seconds in range(0,2):
            print(f"No possible moves. Reset in: {2-seconds}")
            time.sleep(1)
        curr_x=7
        curr_y=7
        food_exist=False
        snake_body_position=[]
        food_eaten=0
        snake_length=start_snake_length
        snake_board=declare_empty_table(board_size)
        print_table(snake_board,snake_length,curr_x,curr_y,0,0,snake_body_position)
        continue
    #Check if "x" do not move on border. If it does then calculate random next position again.
    elif next_x == 0 or next_x == (board_size-1):
        continue
    elif next_y == 0 or next_y == (board_size-1) :
        continue
    elif snake_board[next_x][next_y] != " " and snake_board[next_x][next_y] != food_symbol:
        continue
    #do not allow move -1,-1 or 1,1 or -1,1
    elif position_move_x*position_move_y != 0:
        continue

    
    snake_board=declare_empty_table(board_size)
 
    os.system('cls')
    snake_body_position,food_exist, food_x, food_y, snake_length,food_eaten= print_table(snake_board,snake_length,curr_x,curr_y,position_move_x,position_move_y,snake_body_position,food_exist, food_x, food_y,food_eaten)
    print(f"Snake length: {snake_length}. Food eaten: {food_eaten}")
    curr_x=next_x
    curr_y=next_y
    
    time.sleep(0.01)
        
    
    
    
