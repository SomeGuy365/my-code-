import random

print("Welcome to the gambling game!")
cash = 3
rolling = True

while cash > 0 and rolling:
    num = random.randint(1,6)
    print("you rolled a",str(num))

    if num == 6:
        cash *= 2
        print("Winner! You now have £"+str(cash))
    elif num == 1:
        if cash < 2:
            cash = 0
        else:
            cash -= 2
        print("You lose :(, You now have £"+str(cash)) 
    
    inp = input("Play again? y/n \n")
    if inp == "n":
        rolling = False

if cash == 0:
    print("Your out!")
else:
    print("Enjoy your £"+str(cash))