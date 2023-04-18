
board = [["  ","  ","  "]
         ,["  ","  ","  "],
         ["  ","  ","  "]]

def print_board():
    global board
    columns = ["A ","B ","C ","D ","E ","F ","G ","H "]
    print(" ",columns)
    rowNum = 1
    for row in board:
        print(rowNum,row)
        rowNum+=1

print_board()