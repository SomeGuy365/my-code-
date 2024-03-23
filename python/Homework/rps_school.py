p1_choice = input("Enter p1 choice:")
p2_choice = input("Enter p2 choice:")

win = ''

if p1_choice == p2_choice:
    win = 'Draw'

if p1_choice == 'r':
    if p2_choice == 'p':
        win = 'Player 2 wins!'
    elif p2_choice == 's':
        win = 'Player 1 wins!'
elif p1_choice == 'p':
    if p2_choice == 'r':
        win = 'Player 1 wins!'
    elif p2_choice == 's':
        win = 'Player 2 wins!'
elif p1_choice == 's':
    if p2_choice == 'r':
        win = 'Player 2 wins!'
    elif p2_choice == 'p':
        win = 'Player 1 wins!'

print(win)