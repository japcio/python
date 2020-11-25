import random
import time
import os
from termcolor import colored
from colorama import init, Fore, Back, Style
init()
print(Style.RESET_ALL)

max_height=50
max_height=20
max_width=60

vertical_array=[]
elements_list=["a","b","c","d","f","g","o","p","r","s","t","u","x","y","z","!","?","@","#"]


for i in range(0,max_height):
    current_line_string=""
    for element in range (0,random.randint(int(max_width*0.8),max_width)):
            current_line_string=current_line_string+(elements_list[random.randint(0,(len(elements_list)-1))])+" "
    vertical_array.append(current_line_string)



for i in range (0,5):
    elements_list.append(" ")


while True:
        current_line_string=""
        for element in range (0,random.randint(int(max_width*0.8),max_width)):
            current_line_string=current_line_string+(elements_list[random.randint(0,(len(elements_list)-1))])+" "
        vertical_array[0]=current_line_string

        for line in range(0,len(vertical_array)):
              print('\033[92m' + vertical_array[line])
              time.sleep(0.1)
