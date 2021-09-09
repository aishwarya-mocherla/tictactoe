import os
import sys
game=[" "," "," "," "," "," "," "," "," "]

def print_game():
    print( game[0] ," | ", game[1] ," | ", game[2] )
    print("___|_____|___")
    print("   |     |   ")
    print( game[3] ," | ", game[4] ," | ", game[5] )
    print("___|_____|___")
    print("   |     |   ")
    print( game[6] ," | ", game[7] ," | ", game[8] )
    
def begin():
    print("PRESS :\n 1: If Player 1 is 'X' and player 2 is 'O' \n -OR- \n 2: If Player 1 is 'O' and Player 2 is 'X' ")
    tr = int(input())
    if tr==1:
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'
    while (True):
        print("Player 1's turn")
        player(player1)
        n = check_result(player1,player2)
        if n==1:
            sys.exit()
        print("Player 2's turn")
        player(player2)
        n = check_result(player1,player2)
        if n==1:
            sys.exit()

def player(p):
    t = int(input("Choose an empty space from 1-9"))
    if game[t-1] != " ":
        print("Space is not empty")
        player(p)
    else:
        game[t-1] = p
        print_game()
        
def check_result(p1,p2):
    value=6
    for i in range(8):
        if game[i]==" ":
            game[i]=6
    solution1 = list(set((game[0],game[4],game[8])))
    solution2 = list(set((game[0],game[3],game[6])))
    solution3 = list(set((game[1],game[4],game[7])))
    solution4 = list(set((game[3],game[4],game[5])))
    solution5 = list(set((game[2],game[5],game[8])))
    solution6 = list(set((game[2],game[4],game[6])))
    solution7 = list(set((game[6],game[7],game[8])))
    solution8 = list(set((game[0],game[1],game[2])))
    result=[solution1,solution2,solution3,solution4,solution5,solution6,solution7,solution8]
    for i in range(8):
        if len(result[i])==1 and result[i][0] !=6:
            if result[i][0]== p1:
                print("PLAYER 1 WINS!!")
            else:
                print("PLAYER 2 WINS!!")
                value = 5
        
    for i in range(8):
        if game[i]==6:
            game[i]=" "
    if value == 5:
        return 1
    else:
        return 2
    
    

################# DRIVER CODE ########################
print("The Pattern Of TicTacToe is as follows:")
print(" 1 | 2 | 3 ")
print("___|___|___")
print("   |   |   ")
print(" 4 | 5 | 6 ")
print("___|___|___")
print("   |   |   ")
print(" 7 | 8 | 9 ")

begin()
player()
check_result()