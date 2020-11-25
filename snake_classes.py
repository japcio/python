"""Each object is point represented by x,y value"""
class Point:
    def __init__(self,position_x,position_y):
        self.position_x=position_x
        self.position_y=position_y

#Class is use only to check if game is in progress or should be ended
class Game:
    game_status_continue="run"
    game_status_end="end"
    def __init__(self):
        self.game_status=self.game_status_continue

"""Class representing food which appears on board and can be eaten by snake"""
#class Food:
class Food:
    food_symbol='@'
    food_x=0
    food_y=0

   

"""Class representing snake"""
class Snake:
    #class variables
    head_sign="O"
    body_sign="x"
    #Position of head
    head_x=""
    head_y=""
    def __init__(self, length, board_size):
        self.length=length
        self.body_position=[]
        #Assign points location of snake body, omit head
        if self.length < board_size -1:
            for i in range(0,self.length-1):
                self.body_position.append(str(board_size//2)+str(",")+str(board_size-3-i))
            #Add snake head to body position
            self.head_x=board_size//2
            self.head_y=board_size -2-self.length
            self.body_position.append(str(self.head_x)+str(",")+str(self.head_y))
        else:
            print("Snake is longer than board size") 
        self.body_position.reverse()
    def move_snake_body(self,Board,Food):
        #check if any move is possible. If not then end game.
        if Board.board[self.head_x-1][self.head_y] != Board.empty_place \
        and Board.board[self.head_x+1][self.head_y] != Board.empty_place \
        and Board.board[self.head_x][self.head_y-1] != Board.empty_place \
        and Board.board[self.head_x][self.head_y+1] != Board.empty_place \
        and Board.board[self.head_x-1][self.head_y] != Food.food_symbol \
        and Board.board[self.head_x+1][self.head_y] != Food.food_symbol \
        and Board.board[self.head_x][self.head_y-1] != Food.food_symbol \
        and Board.board[self.head_x][self.head_y+1] != Food.food_symbol:
            game.game_status=game.game_status_end   
        else:
            """Calculate best score for each possible move. 
            Check what is next to snake head and calculate which direction is closest to food."""
            #Move x=-1, y=0 right move
            if Board.board[self.head_x-1][self.head_y] == Board.empty_place or Board.board[self.head_x-1][self.head_y] == Food.food_symbol:
                right_move_score=math.sqrt((self.head_x-1-Food.food_x)**2+(self.head_y-Food.food_y)**2)
            else:
                right_move_score=1000+Board.board_size
            #Move x=1, y=0 left move
            if Board.board[self.head_x+1][self.head_y] == Board.empty_place or Board.board[self.head_x+1][self.head_y] == Food.food_symbol:
                left_move_score=math.sqrt((self.head_x+1-Food.food_x)**2+(self.head_y-Food.food_y)**2)
            else:
                left_move_score=1000+Board.board_size
            #Move x=0, y=1 down move
            if Board.board[self.head_x][self.head_y+1] == Board.empty_place or Board.board[self.head_x][self.head_y+1] == Food.food_symbol:
                down_move_score=math.sqrt((self.head_x-Food.food_x)**2+(self.head_y+1-Food.food_y)**2)
            else:
                down_move_score=1000+Board.board_size
            #Move x=0, y=-1 up move
            if Board.board[self.head_x][self.head_y-1] == Board.empty_place or Board.board[self.head_x][self.head_y-1] ==Food.food_symbol:
                up_move_score=math.sqrt((self.head_x-Food.food_x)**2+(self.head_y-1-Food.food_y)**2)
            else:
                up_move_score=1000+Board.board_size

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

            #Assign new head position to current head position
            Board.clear_snake_on_board(self)
            self.head_x=self.head_x+position_move_x
            self.head_y=self.head_y+position_move_y
            #Declare new snake body position table after move
            new_body_position=['' for value in range(0, len(self.body_position))]
            new_body_position[0]=str(self.head_x)+","+str(self.head_y)
            for i in range (1,len(self.body_position)):
                new_body_position[i]=self.body_position[i-1]
            
             
            self.body_position=new_body_position
             #If no possible move then set game status to "end"
            game.game_status=game.game_status_continue
            
        return game.game_status



"""Class representing board printed on screen. The board is limited with borders. 
On board food appears and snake moves itself"""
class Board:
    board=[]
    empty_place=" "
    horizontal_border="_"
    vertical_border="|"
    food_exist=False
    game_status=""
    def __init__(self, board_size,Game):
        self.game_status=Game.game_status
        self.board_size=board_size
        #create empty two dimensional table
        for i in range (0,board_size):
            self.board.append([])
            for j in range(0, board_size):
                self.board[i].append(self.empty_place)
        """Write game board borders"""
        for i in range(0,board_size):
            self.board[0][i]=self.horizontal_border
            self.board[board_size-1][i]=self.horizontal_border
        for i in range (1,board_size):
            self.board[i][0]=self.vertical_border
            self.board[i][board_size-1]=self.vertical_border
               
    """Function printing the board game on screen"""
    def print_board(self):
        for i in range (0, self.board_size):
            current_line=""
            for j in range (0,self.board_size):
                current_line=current_line+str(self.board[i][j])
            print(current_line)
    #Function adding snake body to board
    def draw_snake_on_board(self,Snake):
        #First element is head
        current_element=Snake.body_position[0].split(",")
        self.board[int(current_element[0])][int(current_element[1])]=Snake.head_sign
        for i in range(1, len(Snake.body_position)):
        #Split current_element into x and y coordinates
            current_element=Snake.body_position[i].split(",")
            self.board[int(current_element[0])][int(current_element[1])]=Snake.body_sign
    
    #Function clearing snake from board
    def clear_snake_on_board(self,Snake):
        for i in range(0, len(Snake.body_position)):
        #Split current_element into x and y coordinates
            current_element=Snake.body_position[i].split(",")
            self.board[int(current_element[0])][int(current_element[1])]=Board.empty_place

    
    #Function adding food on board
    def add_food(self,Food):
        end_flag=0
        while end_flag == 0:
            Food.food_x=random.randrange(1,self.board_size-2)
            Food.food_y=random.randrange(1,self.board_size-2)
            if self.board[Food.food_x][Food.food_y]==self.empty_place:
                self.board[Food.food_x][Food.food_y]=Food.food_symbol
                end_flag=1
        self.food_exist=True
        return Food
      
    #Function clearing food from board. E.g. when snake eats it.
    def clear_food(self,Food):
        self.board[Food.food_x][Food.food_y]=self.empty_place
        self.food_exist=False
        del Food

    """Function which initialise snake on board after it moves. It checks if snake it food and if yes then create new food.
    Then it clears current snake and draw new one after position move"""
    def move_snake_on_board(self,Snake,Food,Game):
        Game.game_status=Snake.move_snake_body(self,Food)
        #Check if snake could be moved. If yes then continue game. Otherwise set status to end.
        if Game.game_status == Game.game_status_continue:
            #check if after snake move the snake head is on food. If yes then snake eats it and new food should be 
            if Snake.head_x == Food.food_x and Snake.head_y == Food.food_y:
                self.clear_food(Food)
                #Increase snake body by one element
                add_body_end_flag=0
                while add_body_end_flag == 0:
                    add_body_x=random.randrange(-1,2)
                    add_body_y=random.randrange(-1,2)
                    last_body_element_position=Snake.body_position[-1].split(",")
                    if self.board[int(last_body_element_position[0])-int(add_body_x)][int(last_body_element_position[1])-int(add_body_y)] != board.empty_place:
                        continue
                    else:
                        add_body_end_flag=1
                        Snake.body_position.append(str(int(last_body_element_position[0])-int(add_body_x))+","+str(int(last_body_element_position[1])-int(add_body_y)))
                        Snake.length=Snake.length+1 
                        self.add_food(Food)
            
            self.clear_snake_on_board(Snake)
            self.draw_snake_on_board(Snake)
            self.print_board()
        return Game.game_status,Food

           



"""MAIN PROGRAM"""
import random
import math
import time
import os
game=Game()
food=Food()
board=Board(15,game)
snake=Snake(6,board.board_size)
board.draw_snake_on_board(snake)
board.food_exist=board.add_food(food)
board.print_board()

while game.game_status == game.game_status_continue:
    os.system('cls')
    game.game_status,food=board.move_snake_on_board(snake,food,game)
    time.sleep(0.5)
print("end")
time.sleep(5)



"""old part of program 

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
        snake_board[curr_x][curr_y]='\033[35mO\033[39m'
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
        snake_board[int(current_body_element_position[0])][int(current_body_element_position[1])]='\033[32mx\033[39m'
        
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
best_snake_length=start_snake_length
best_food_eaten=food_eaten

#set failure counter
failures=0


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
    if snake_board[curr_x-1][curr_y] != " " and snake_board[curr_x+1][curr_y] != " " and snake_board[curr_x][curr_y-1] != " " and snake_board[curr_x][curr_y+1] != " " and snake_board[curr_x-1][curr_y] != food_symbol \
       and snake_board[curr_x+1][curr_y] != food_symbol and snake_board[curr_x][curr_y-1] != food_symbol and snake_board[curr_x][curr_y+1] != food_symbol:
        #for seconds in range(0,2):
        #    print(f"No possible moves. Reset in: {2-seconds}")
        #   time.sleep(1)
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
        failures=failures+1
        snake_body_position=[]
        snake_board=declare_empty_table(board_size)
        print_table(snake_board,snake_length,curr_x,curr_y,0,0,snake_body_position)
        continue
    #Calculate best score for each possible move
    #Move x=-1, y=0 right move
    if snake_board[curr_x-1][curr_y] == " " or snake_board[curr_x-1][curr_y] == food_symbol:
        right_move_score=math.sqrt((curr_x-1-food_x)**2+(curr_y-food_y)**2)+random.randint(0,1)
    else:
        right_move_score=1000+board_size
    #Move x=1, y=0 left move
    if snake_board[curr_x+1][curr_y] == " " or snake_board[curr_x+1][curr_y] == food_symbol:
        left_move_score=math.sqrt((curr_x+1-food_x)**2+(curr_y-food_y)**2)+random.randint(0,1)
    else:
        left_move_score=1000+board_size
    #Move x=0, y=1 down move
    if snake_board[curr_x][curr_y+1] == " " or snake_board[curr_x][curr_y+1] == food_symbol:
        down_move_score=math.sqrt((curr_x-food_x)**2+(curr_y+1-food_y)**2)+random.randint(0,1)
    else:
        down_move_score=1000+board_size
    #Move x=0, y=-1 up move
    if snake_board[curr_x][curr_y-1] == " " or snake_board[curr_x][curr_y-1] ==food_symbol:
        up_move_score=math.sqrt((curr_x-food_x)**2+(curr_y-1-food_y)**2)+random.randint(0,1)
    else:
        up_move_score=1000+board_size

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
    snake_body_position,food_exist, food_x, food_y, snake_length,food_eaten= print_table(snake_board,snake_length,curr_x,curr_y,position_move_x,position_move_y,snake_body_position,food_exist, food_x, food_y,food_eaten)
    print(f"Snake length: {snake_length}. Food eaten: {food_eaten}")
    print(f"Best snake length: {best_snake_length}. Best food eaten: {best_food_eaten}. Failures: {failures}")
    print(f"Snake version: 4.0")
    curr_x=next_x
    curr_y=next_y
    
    time.sleep(0.05)
        
    
    
    end of old program """
