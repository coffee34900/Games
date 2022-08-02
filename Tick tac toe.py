1#Tick tac toe using random library.

from itertools import count
import random

#X-player will always have the first turn.

currentPlayer = "X"
winner = None
gameRunning = True

# Game board 3X3

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
def printBoard(board):
    
    ''' Print the empty board '''
    
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# For input from the player

def playerInput(board):
    inp = int(input("Select a number from 1-9 to choose the spot: "))
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer  
    else:
        print("Player is already at that spot.")
        

#  Win, loose or tie

def checkHorizontle(board):
    
    '''Check horzotontally if somebody won or not '''
    
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    
    '''Check vertically if somebody won or not '''
    
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True

def checkDiag(board):
    
    '''Check diagonally if somebody won or not '''
    
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True

def checkIfWin(board):
    
    '''Check if somebody won or not '''
    
    global gameRunning
    if checkHorizontle(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

def checkIfTie(board):
    
    '''Check if its a tie '''
    
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False

# Switch player

def switchPlayer(board):
    global currentPlayer
    countX = 0
    countO = 0
    for i in board:
       if i == 'X':
           countX += 1
       elif i == 'O':
           countO += 1

    if countX > countO:
        if currentPlayer == "X":
            currentPlayer = "O"
        else:
            currentPlayer = "X"
    elif countO == countX:
        currentPlayer = 'X'
    


#   O-player is computer.

def computer(board):
    countX = 0
    countO = 0
    for i in board:
       if i == 'X':
           countX += 1
       elif i == 'O':
           countO += 1
    if countX >= countO:
        while currentPlayer == "O":
            position = random.randint(0, 8)
            if board[position] == "-":
                board[position] = "O"
                switchPlayer(board)


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkIfWin(board)
    checkIfTie(board)
    switchPlayer(board)
    computer(board)
    checkIfWin(board)
    checkIfTie(board)
