cart = []
mode = ''

while mode != 'exit':
    mode = input('\nWhat to do?\n1:view\n2:add\n3:take away\n4:clear\n')
    if mode == '1':
        for i in cart:
            print(str(cart.index(i)+1) + ':' + i)
    elif mode == '2':
        cart.append(input('What to add:'))
    elif mode == '3':
        cart.remove(input('what to remove:'))
    elif mode == '4':
        cart = []