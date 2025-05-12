#Variables are also reset in the reset function.

from random import randint
from sys import exit
from time import sleep

moves = [
' ',' ',' ',
' ',' ',' ',
' ',' ',' '
] #Used to keep track of the moves on the board

WIN_COMBOS = [ #Used in canWin() to determine if the player can win next move
(0, 1, 2), #Across the top
(3, 4, 5), #Across the middle
(6, 7, 8), #Across the bottom

(0, 4, 8), #Top left to bottom right
(2, 4, 6), #Top right to bottom left

(0, 3, 6), #Down the left
(1, 4, 7), #Down the middle
(2, 5, 8) #Down the right
]

humanSymbol = ''
botSymbol = '' #Symbols are x or o, uppercase

def printBoard(): #This function prints the board
    global moves #Calls the moves variable
    print(moves[0],'|',moves[1],'|',moves[2])
    print('-- -- --')
    print(moves[3],'|',moves[4],'|',moves[5])
    print('-- -- --',)
    print(moves[6],'|',moves[7],'|',moves[8])

def detectWin(board, sym):
    global WIN_COMBOS
    for combo in WIN_COMBOS:
        if board[combo[0]] == sym and board[combo[1]] == sym and board[combo[2]] == sym:
            return True
    return False

def checkforWin(defender, mover):
    global moves, WIN_COMBOS
    tempMoves = moves.copy()
    for i in range(9):
        if moves[i] == ' ':
            tempMoves[i] = mover
            if detectWin(tempMoves, defender):
                return i
            tempMoves[i] = ' '
    return False

def botMove():
    global moves, humanSymbol, botSymbol
    CORNERMOVES = [0, 2, 6, 8]
    MIDDLE = 4
    EDGES = [1, 3, 5, 7]

    win = checkforWin(botSymbol, botSymbol)
    if win is not False:
        return win

    block = checkforWin(humanSymbol, humanSymbol)
    if block is not False:
        return block

    for move in CORNERMOVES:
        if moves[move] == ' ':
            return move
    if moves[MIDDLE] == ' ':
        return MIDDLE
    for move in EDGES:
        if moves[move] == ' ':
            return move
    return 'error'

def humanMove():
    global moves, humanSymbol, botSymbol #Calls needed global variables
    print('Enter where you would like to move. (1-9)')
    while True:
        move = input()
        try:
            move = int(move)
        except:
            print('Please enter a number from 1 to 9!')
        else:
            if move < 1 or move > 9:
                print('Please enter a number from 1 to 9!')
            else:
                break
        
    move -= 1
    if moves[move] == ' ':
        return move
    elif moves[move] == botSymbol:
        print('The bot has moved there already!')
        return humanMove()
    else:
        print('You have moved there already!')
        return humanMove()

def isTie():
    global moves
    if moves.count(' ') == 0:
        return True
    else:
        return False

def reset():
    global moves, humanSymbol, botSymbol
    moves = [
' ',' ',' ',
' ',' ',' ',
' ',' ',' '
]
    humanSymbol, botSymbol = '', ''


#Start of program.
while True:
    while humanSymbol not in ['X', 'O']:
        print('Would you like to be X or O?')
        answer = input().upper()
        if answer == 'X':
            humanSymbol = 'X'
            botSymbol = 'O'
        elif answer == 'O':
            humanSymbol = 'O'
            botSymbol = 'X'

    if randint(0,1) == 0:
        print('The bot will go first.')
        whoIsFirst = 'bot'
    else:
        print('You will go first.')
        whoIsFirst = 'human'

    if whoIsFirst == 'bot':
        while True:            
            moves[botMove()] = botSymbol
            printBoard()
            if detectWin(moves, botSymbol):
                winner = 'bot'
                break
            if isTie():
                winner = 'tie'
                break

            moves[humanMove()] = humanSymbol
            if detectWin(moves, botSymbol):
                printBoard()
                winner = 'human'
                break
            if isTie():
                printBoard()
                winner = 'tie'
                break

    else:
        while True:
            printBoard()
            moves[humanMove()] = humanSymbol
            if detectWin(moves, botSymbol):
                winner = 'human'
                break
            if isTie():
                winner = 'tie'
                break

            moves[botMove()] = botSymbol
            if detectWin(moves, botSymbol):
                printBoard()
                winner = 'bot'
                break
            if isTie():
                winner = 'tie'
                printBoard()
                break

    if winner == 'tie':
        print('It\'s a tie!')
    elif winner == 'bot':
        print('The bot won.')
    else:
        print('You won!')

    sleep(1)
    print('Would you like to play again? (y/n)')
    playAgain = input().lower()
    if playAgain == 'y':
        reset()
        print('~')
    else:
        exit()
