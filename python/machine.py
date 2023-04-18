def showboard():
    global board
    rowNum = 1
    for row in board:
        print(row)
        rowNum+=1

def isWinner():
# This function checks if any winner is winning
    # Check the rows
    for row in range (0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == 'X'):
            print("Player " + 'X' + ", you won!")
            return True
   
        elif (board[row][0] == board[row][1] == board[row][2] == '0'):
            print("Player " + '0' + ", you won!")
            return True
            

board = [["1","2","3"],["4","5","6"],["7","8","9"]]

game_won = False
turn = 2

while game_won == False:
    showboard()
    playerimp1 = int(input('where do you wanna go?'))
    playerimp2 = int(input('where do you wanna go?'))
    if turn%2 == 0:
        if board[playerimp1-1][playerimp2-1] != '0':
            board[playerimp1-1][playerimp2-1] = 'X'
        else:
            print('uh oh')
    elif turn%2 == 1:
        board[playerimp1-1][playerimp2-1] = '0'
    game_won = isWinner()
    turn += 1
