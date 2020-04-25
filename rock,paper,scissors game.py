#!/usr/bin/env python
# coding: utf-8

#  # Rock, Paper, Scissors game

# In[ ]:


import random
from random import choice
global option1
global option2
def game():
    return(choice(["Rock","Paper","Scissors"]))

def start():
    print("player 1's turn")
    print("press enter to play")
    enter=input()
    option1=game()
    print(option1)
    print("player' 2s turn")
    print("press enter to play")
    enter=input()
    option2=game()
    print(option2)

def play():
    if (option1==option2):
        print("DRAW")
        print("play again")
        start()
    elif (option1=="Rock" and option2=="Paper"):
        print("Paper wraps the Rock")
        print("Player 2 wins")       
    elif (option1=="Rock" and option2=="Scissors"):
        print("Rock blunts Scissors")
        print("Player 1 wins")
    elif (option1=="Paper" and option2=="Scissors"):
        print("scissors cuts paper")
        print("Player 2 wins")   
    elif (option2=="Rock" and option1=="Paper"):
        print("Paper wraps the Rock")
        print("Player 1 wins")       
    elif (option2=="Rock" and option1=="Scissors"):
        print("Rock crushes Scissors")
        print("Player 2 wins")
    elif (option2=="Paper" and option1=="Scissors"):
        print("scissors cuts paper")
        print("Player 1 wins")             

op="y"
while (op=="y" or op=="Y"):
    start()
    play()
    print("Do you want to play again?(y/n)")
    op=input()       
              


# In[ ]:





# In[ ]:





# In[ ]:




