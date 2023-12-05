won = False
turn = 'x'
#stores them all in one list, called board
board = [["1","2","3"],
         ["4","5","6"],
         ["7","8","9"]]
#will print out the tictactoe board
def print_board():
    global board
    line_num = 0
    for line in board:
        print(line[0]+" | "+line[1]+" | "+line[2])
        if line_num < 2:
            print("---------")
            line_num += 1
def checkwin():
    global board
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] or board[0][i] == board[1][i] == board[2][i]:
            print(f'{turn} wins!')
            return True
        
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        print(f"{turn} wins!")
        return True
        
    return False
#prints the board
print_board()
while won == False:
    ruser = int(input("Enter row:"))
    cuser = int(input("Ener column:"))
    board[ruser-1][cuser-1] = turn.upper()
    print_board()
    won = checkwin()
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'