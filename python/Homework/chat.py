import random 

questions = ['Whats your favourite colour?','Fav food?','fav drink?']
answers = [['blue','pink','brown'],['cheesecake','pizza','cottage cheese'],['milk','sprite','toilet water']]

q = False

while q == False:
    choice = random.choice(questions)
    print(choice)
    imp = input('')
    if imp == answers[questions.index(choice)][0]:
        print(f'I also like {answers[questions.index(choice)][0]}')
    elif imp == answers[questions.index(choice)][1]:
        print(f'{answers[questions.index(choice)][1]} as aight')
    elif imp == answers[questions.index(choice)][2]:
        print('>:(')
    else:
        print('Never heard of it')

    user_q = input('wanna stop?y/n\n')
    if user_q == 'y':
        q = True
    else:
        continue