import py2exe
class Game:
    game_status_continue="run"
    game_status_end="end"
    def __init__(self):
        self.game_status=self.game_status_continue
    def print_menu(self):
        self.min_speed=1
        self.max_speed=30
        self.min_board=20
        self.max_board=50
        self.initial_speed=1
        self.initial_board_size=20
        self.snake_length=6

        #Set console windows size
        os.system(f"mode con cols={self.max_board+1} lines={self.max_board+10}")
        #Ask user to set initial snake speed
        print(f"Snake speed (1-{self.max_speed}): [- / +, enter to continue]: {self.initial_speed}")
        key_press=msvcrt.getch().decode('ASCII') 
        while key_press != '\r':
            key_press=msvcrt.getch().decode('ASCII') 
            if key_press=='-':
                if self.initial_speed > self.min_speed:
                    self.initial_speed=self.initial_speed-1
                    os.system('cls')
                    print(f"Snake speed ({self.min_speed}-{self.max_speed}): [- / +, enter to continue]: {self.initial_speed}")
                key_press=''
            if key_press=='+':
                if self.initial_speed <self.max_speed:
                    self.initial_speed=self.initial_speed+1
                    os.system('cls')
                    print(f"Snake speed ({self.min_speed}-{self.max_speed}): [- / +, enter to continue]: {self.initial_speed}")
                key_press='' 
        #Ask user to set board size
        print(f"Board size ({self.min_board}-{self.max_board}): [- / +, enter to continue]: {self.initial_board_size}")
        key_press=msvcrt.getch().decode('ASCII') 
        while key_press != '\r':
            key_press=msvcrt.getch().decode('ASCII') 
            if key_press=='-':
                if self.initial_board_size > self.min_board:
                    self.initial_board_size=self.initial_board_size-1
                    os.system('cls')
                    print(f"Snake speed ({self.min_speed}-{self.max_speed}): [- / +, enter to continue]: {self.initial_speed}")
                    print(f"Board size ({self.min_board}-{self.max_board}): [- / +, enter to continue]: {self.initial_board_size}")
                key_press=''
            if key_press=='+':
                if self.initial_board_size <self.max_board:
                    self.initial_board_size=self.initial_board_size+1
                    os.system('cls')
                    print(f"Snake speed ({self.min_speed}-{self.max_speed}): [- / +, enter to continue]: {self.initial_speed}")
                    print(f"Board size ({self.min_board}-{self.max_board}): [- / +, enter to continue]: {self.initial_board_size}")
                key_press=''
        os.system('cls')
    #Function to print controls
    def print_controls(self):
        print("Play with WSAD keys")
    def print_statistics(self,Board,Snake):
        print(f"Current snake length: {Snake.food_count}")
        print(f"Current snake speed: {Board.speed}")

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
    #what was last key pressed by user and direction move of snake
    last_key_pressed='a'
    #Position of head
    head_x=""
    head_y=""
    food_count=0
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
        #check if  move is possible. If not then end game.
        start_time = time.time()
        #how long wait for user to press key
        wait_time = 1/Board.speed
        while True:  # making a loop
            curr_time= time.time()
            if curr_time - start_time < wait_time: 
                if msvcrt.kbhit():
                    key_pressed=msvcrt.getch().decode('ASCII')    
                    if key_pressed=='w' and self.last_key_pressed=='s':
                        break
                    elif key_pressed=='s' and self.last_key_pressed=='w':
                        break
                    elif key_pressed=='a' and self.last_key_pressed=='d':
                        break
                    elif key_pressed=='d' and self.last_key_pressed=='a':
                        break
                    else:
                         self.last_key_pressed=key_pressed         
            else:
                break  
        if self.last_key_pressed=='w':  # if key 'w' is pressed - up move
            try:
                delay=wait_time-(curr_time-start_time)
                time.sleep(delay)
                position_move_x=-1
                position_move_y=0
            except:
                position_move_x=-1
                position_move_y=0
        elif self.last_key_pressed=='s':  # if key 's' is pressed - down move
            try:
                delay=wait_time-(curr_time-start_time)
                time.sleep(delay)
                position_move_x=1
                position_move_y=0
            except:            
                position_move_x=1
                position_move_y=0
        elif self.last_key_pressed=='a':  # if key 'a' is pressed - left move
            try:
                delay=wait_time-(curr_time-start_time)
                time.sleep(delay)
                position_move_x=0
                position_move_y=-1
            except:
                position_move_x=0
                position_move_y=-1
        elif self.last_key_pressed=='d':  # if key 'd' is pressed - right move
            try:
                delay=wait_time-(curr_time-start_time)
                time.sleep(delay)
                position_move_x=0
                position_move_y=1 
            except:
                position_move_x=0
                position_move_y=1  
        if (Board.board[self.head_x+position_move_x][self.head_y+position_move_y] == Board.empty_place or Board.board[self.head_x+position_move_x][self.head_y+position_move_y] == Food.food_symbol) and \
            Board.board[self.head_x+position_move_x][self.head_y+position_move_y] != Snake.body_sign: 
            game.game_status=game.game_status_continue 
        else:
            game.game_status=game.game_status_end
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
    def __init__(self, board_size,Game,speed):
        self.game_status=Game.game_status
        self.board_size=board_size
        self.speed=speed
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
                Snake.food_count=Snake.food_count+1
                #Increase snake body by one element
                add_body_end_flag=0
                #increase speed when user ate food till maximum speed set in game
                if self.speed < game.max_speed:
                    self.speed=self.speed+1
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
        os.system('cls')
        self.draw_snake_on_board(Snake)
        self.print_board()
        game.print_controls()
        game.print_statistics(self,Snake)
        return Game.game_status,Food


"""MAIN PROGRAM"""
import random
import math
import time
import os
import keyboard
import msvcrt
game=Game()
game.print_menu()
food=Food()
board=Board(game.initial_board_size,game,game.initial_speed)
snake=Snake(game.snake_length,board.board_size)
board.draw_snake_on_board(snake)
board.food_exist=board.add_food(food)
board.print_board()

while game.game_status == game.game_status_continue:
    game.game_status,food=board.move_snake_on_board(snake,food,game)
    if game.game_status==game.game_status_end:
        board.clear_snake_on_board(snake)
        board.clear_food(food)
        print("Failure!!!")
        print("Press [Y] to try once again or any other key to quit...")
        key_press=msvcrt.getch().decode('ASCII')
        if key_press=='y':
            os.system('cls')
            game=Game()
            game.print_menu()
            food=Food()
            board=Board(game.initial_board_size,game,game.initial_speed)
            snake=Snake(game.snake_length,board.board_size)
            board.draw_snake_on_board(snake)
            board.food_exist=board.add_food(food)
            board.print_board()
            game.game_status=game.game_status_continue

