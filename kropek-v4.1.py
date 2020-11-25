

#Function to declare empty 2D table which works as space with border where "x" can move
def declare_empty_table(board_size):
    snake_board=[]
    for i in range (0,board_size):
       snake_board.append([])
       for j in range(0, board_size):
           snake_board[i].append(" ")

    #write border in table
    for i in range(0,board_size):
        snake_board[0][i]='\033[36m_\033[39m'
        snake_board[board_size-1][i]='\033[36m-\033[39m'
    for i in range (1,board_size-1):
        snake_board[i][0]='\033[36m|\033[39m'
        snake_board[i][board_size-1]='\033[36m|\033[39m'
    return snake_board

#Function to print current status of 2D table showing borders and "x" position
def print_table(snake_board,body_sign='\033[32mx\033[39m',head_sign='\033[35mO\033[39m',snake_length=0,curr_x=5,curr_y=5,position_move_x=0,position_move_y=0,snake_body_position="",food_exist=False,food_x="", food_y="",food_eaten=0):
    #Check if last position dictionary is not empty
    if snake_body_position:
        new_head_position_x=curr_x+position_move_x
        new_head_position_y=curr_y+position_move_y
        snake_board[new_head_position_x][new_head_position_y]=head_sign
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
        snake_board[curr_x][curr_y]=head_sign
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
        snake_board[int(current_body_element_position[0])][int(current_body_element_position[1])]=body_sign
        
        
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

import random
import os
import time
import math
from colorama import init
init(autoreset=True)
init()

#Set food symbol
food_symbol='\033[31m@\033[39m'

#set head symbol
body_sign='\033[32mx\033[39m'
#set body symbol
head_sign='\033[35mO\033[39m'

#Set initial food position
food_x=0
food_y=0

#Flag showing if food is on board
food_exist=False

#set failure counter
failures=0


#number of food eaten
food_eaten=0

#set snake parameters
start_snake_length=12
snake_length=start_snake_length
snake_body_position=[]
best_snake_length=start_snake_length
best_food_eaten=food_eaten


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
print_table(snake_board,body_sign,head_sign,snake_length,curr_x,curr_y,0,0,snake_body_position,food_exist)



while True:
    position_move_x=0
    position_move_y=0
    if snake_board[curr_x-1][curr_y] != " " and snake_board[curr_x+1][curr_y] != " " and snake_board[curr_x][curr_y-1] != " " and snake_board[curr_x][curr_y+1] != " " and snake_board[curr_x-1][curr_y] != food_symbol \
       and snake_board[curr_x+1][curr_y] != food_symbol and snake_board[curr_x][curr_y-1] != food_symbol and snake_board[curr_x][curr_y+1] != food_symbol:
        #for seconds in range(0,2):
        #    print(f"No possible moves. Reset in: {2-seconds}")
        #    time.sleep(1)
        #Write best score
        if snake_length> best_snake_length:
            best_snake_length=snake_length
        if food_eaten>best_food_eaten:
            best_food_eaten=food_eaten
        food_eaten=0
        snake_length=start_snake_length
        curr_x=7
        curr_y=7
        food_exist=False
        snake_body_position=[]
        failures=failures+1
        snake_board=declare_empty_table(board_size)
        print_table(snake_board,body_sign,head_sign,snake_length,curr_x,curr_y,0,0,snake_body_position)
        continue
    #Calculate best score for each possible move
    #Move x=-1, y=0 right move
    if snake_board[curr_x-1][curr_y] == " " or snake_board[curr_x-1][curr_y] == food_symbol:
        right_move_score=math.sqrt((curr_x-1-food_x)**2+(curr_y-food_y)**2)+random.randint(0,1)
    else:
        right_move_score=1000+board_size
    if curr_x-2 > 0 and curr_y-1 > 0 and curr_y+1 < board_size-2:
        if snake_board[curr_x-2][curr_y] == "x" or snake_board[curr_x-2][curr_y-1] == "x" or snake_board[curr_x-2][curr_y+1] == "x":
            right_move_score=math.sqrt((curr_x-1-food_x)**2+(curr_y-food_y)**2)+random.randint(0,1)+500+board_size
    #Move x=1, y=0 left move
    if snake_board[curr_x+1][curr_y] == " " or snake_board[curr_x+1][curr_y] == food_symbol:
        left_move_score=math.sqrt((curr_x+1-food_x)**2+(curr_y-food_y)**2)+random.randint(0,1)
    else:
        left_move_score=1000+board_size
    if curr_x+2 < board_size-2 and curr_y-1 > 0 and curr_y+1 < board_size-2:
        if snake_board[curr_x+2][curr_y] == "x" or snake_board[curr_x+2][curr_y-1] == "x" or snake_board[curr_x+2][curr_y+1] == "x":
            left_move_score=math.sqrt((curr_x+1-food_x)**2+(curr_y-food_y)**2)+random.randint(0,1)+500+board_size
    #Move x=0, y=1 down move
    if snake_board[curr_x][curr_y+1] == " " or snake_board[curr_x][curr_y+1] == food_symbol:
        down_move_score=math.sqrt((curr_x-food_x)**2+(curr_y+1-food_y)**2)+random.randint(0,1)
    else:
        down_move_score=1000+board_size
    if curr_y+2 < board_size-2 and curr_x-1 > 0 and curr_x+1 < board_size-2:
        if snake_board[curr_x][curr_y+2] == "x" or snake_board[curr_x-1][curr_y+2] == "x" or snake_board[curr_x-1][curr_y+2] == "x":
            down_move_score=math.sqrt((curr_x-food_x)**2+(curr_y+1-food_y)**2)+random.randint(0,1)+500+board_size
    #Move x=0, y=-1 up move
    if snake_board[curr_x][curr_y-1] == " " or snake_board[curr_x][curr_y-1] ==food_symbol:
        up_move_score=math.sqrt((curr_x-food_x)**2+(curr_y-1-food_y)**2)+random.randint(0,1)
    else:
        up_move_score=1000+board_size
    if curr_y-2 > 0  and curr_x-1 > 0 and curr_x+1 < board_size-2:
        if snake_board[curr_x][curr_y-2] == "x" or snake_board[curr_x-1][curr_y-2] == "x" or snake_board[curr_x-1][curr_y-2] == "x":
            up_move_score=math.sqrt((curr_x-food_x)**2+(curr_y-1-food_y)**2)+random.randint(0,1)+500+board_size

    scores={'right_move_score' : right_move_score , 'left_move_score' : left_move_score, 'down_move_score' : down_move_score, 'up_move_score' : up_move_score }
    best_score=min(scores, key=scores.get)
    if best_score=='right_move_score':
            position_move_x=-1
            position_move_y=0
    elif best_score=='left_move_score':
            position_move_x=1
            position_move_y=0
    elif best_score=='down_move_score':
            position_move_x=0
            position_move_y=1
    elif best_score=='up_move_score':
            position_move_x=0
            position_move_y=-1

        
    next_x=curr_x+position_move_x
    next_y=curr_y+position_move_y


    
    snake_board=declare_empty_table(board_size)
    os.system('cls')
    snake_body_position,food_exist, food_x, food_y, snake_length,food_eaten= print_table(snake_board,body_sign,head_sign,snake_length,curr_x,curr_y,position_move_x,position_move_y,snake_body_position,food_exist, food_x, food_y,food_eaten)
    print(f"Snake length: {snake_length}. Food eaten: {food_eaten}")
    print(f"Best snake length: {best_snake_length}. Best food eaten: {best_food_eaten}. Failures: {failures}")
    print(f"Snake version: 4.1")
    curr_x=next_x
    curr_y=next_y
    
    time.sleep(0.05)
        
    
    
    
