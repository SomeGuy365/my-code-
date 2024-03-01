import random
import time

users = ["bob","jim","mike","a"]
passw = ["1967","brazil","ford","a"]

def authenticate():
    userinp = input("Enter your user:")
    passinp = input("Enter your pass:")
    if userinp in users:
        if passinp == passw[users.index(userinp)]:
            print("Access Granted")
            return userinp,passinp
    print("NO")

    return "N","N"


def checkwin(u1, u2):
    #checks player cards and returns winner
    if u1[0] == u2[0]:
        if int(u1[1]) > int(u2[1]):
            return "u1"
        else:
            return "u2"
    else:
        if u1[0] == "r":
            if u2[0] == "b":
                return "u1"
            elif u2[0] == "y":
                return "u2"

        if u1[0] == "y":
            if u2[0] == "r":
                return "u1"
            elif u2[0] == "b":
                return "u2"

        if u1[0] == "b":
            if u2[0] == "y":
                return "u1"
            elif u2[0] == "r":
                return "u2"


def fileprint(wincount):
    #writes winner to file
    file = open("python/program-project/winners3.txt", "a")
    if wincount.count("u1") > wincount.count("u2"):
        print("player One wins the game!")
        file.write(p1user+" :\n")
        file.write(str(len(p1cards)) + "\n")
        print("Winning cards:")
        print(p1cards)
    else:
        print("Player Two wins the game!")
        file.write(p2user +" :\n")
        file.write(str(len(p2cards)) + "\n")
        print("Winning cards:")
        print(p2cards)
    file.close()

    #pulls player scores and names from file and sorts them
    nums = []
    file = open("python/program-project/winners3.txt","r")
    line_list = file.read().splitlines()
    for i in range(len(line_list)):
        if line_list[i].isdigit():
            nums.append(int(line_list[i]))

    nums.sort(reverse=True)

    #decides length of leaderboard
    if len(nums) < 5:
        lengt = len(nums)
    else:
        lengt = 6

    #prints out sorted leaderboard somehow
    found = False
    position = 1

    print("Leaderboard:")
    #runs through top 5 sorted numbers 
    for i in range(1,lengt):
        num = nums[i-1]
        found = False
        count = 0

        #compares names/values to highest number 
        for b in range(len(line_list)//2):
            #checks if number
            if line_list[((b*2)+1)-(count*2)].isdigit():
                #checks if current top 5 number
                if int(line_list[((b*2)+1)-(count*2)]) == num and found == False:

                    print(str(position) + ":" + line_list[(b*2)] + " " + str(num))                
                    line_list.remove(line_list[((b*2)+1)-(count*2)])
                    line_list.remove(line_list[b*2])

                    found = True
                    position += 1
                    count += 1

    file.close()




#deck initiation
decktemplate = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
deck = []

for i in decktemplate:
    deck.append("r" + str(i))
    deck.append("b" + str(i))
    deck.append("y" + str(i))
random.shuffle(deck)

print(len(deck))

#initial authentication
authenticated = False
print("Player one authenticate:")
p1user,p1pass = authenticate()
if  p1user != "N":
    print("Player two authenticate:")
    p2user,p2pass = authenticate()
    if p2user != "N":
        authenticated = True


#play rounds and decide winner
p1card = ""
p2card = ""
p1cards = []
p2cards = []

wincount = []

roundnum = 1
#loops until deck is empty 
while len(deck) > 0 and authenticated:
    #pulls random deck from card
    p1card = deck[random.randint(0, len(deck) - 1)]
    p2card = deck[random.randint(0, len(deck) - 1)]

    #stops players pulling same card
    while p1card == p2card:
        p2card = deck[random.randint(0, len(deck) - 1)]

    #removes pulled cards from deck
    deck.remove(p1card)
    deck.remove(p2card)

    #appends winner to winner list
    wincount.append(checkwin(p1card, p2card))
    #gives both cards to winner
    if checkwin(p1card,p2card) == "u1":
        p1cards.append(p1card)
        p1cards.append(p2card)
    else:
        p2cards.append(p1card)
        p2cards.append(p1card)

    #prints round winner
    if checkwin(p1card, p2card) == "u1":
        print("Player one wins round " + str(roundnum))
    else:
        print("Player two wins round " + str(roundnum))

    time.sleep(0.8)
    roundnum += 1


#write to file and print top 5 from file if authenticated 
if authenticated:
    fileprint(wincount)