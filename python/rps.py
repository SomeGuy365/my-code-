import random

ai = ['r','r','p','p','s','s']
playing = True

    
def train():
    for i in range(100):
        aiimp1 = random.choice(ai)
        aiimp2 = random.choice(ai)
        throwaway = play(aiimp1,aiimp2)
    print(ai)


def play(imp1,imp2):
    if imp1 == 'r':
        print('r')
        if imp2 == 'r':
            print('draw')
            return True
        elif imp2 == 'p':
            print('win')
        elif imp2 == 's':
            print('lost')
            ai.append('r')
            print(ai)
    elif imp1 == 'p':
        print('p')
        if imp2 == 'r':
            print('lost')
            ai.append('p')
            print(ai)
        elif imp2 == 'p':
            print('draw')
            return True
        elif imp2 == 's':
            print('win')
    elif imp1 == 's':
        print('s')
        if imp2 == 'r':
            print('win')
        elif imp2 == 'p':
            print('lost')
            ai.append('s')
            print(ai)
        elif imp2 == 's':
            print('draw')
            return True

while playing:
    choice = input('what do?')
    if choice == 'play':
        userimp = input('play')
        aiimp = random.choice(ai)
        playing = play(aiimp,userimp)
        continue
    elif choice == 'train':
        train()
        continue
