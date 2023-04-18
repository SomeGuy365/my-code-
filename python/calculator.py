running = True
output = 0

def add():
    imp1 = int(input('num1:\n'))
    imp2 = int(input('num2:\n'))
    return imp1 + imp2

def sub():
    imp1 = int(input('num1:\n'))
    imp2 = int(input('num2:\n'))
    return imp1 - imp2

def multi():
    imp1 = int(input('num1:\n'))
    imp2 = int(input('num2:\n'))
    return imp1 * imp2

while running:
    thing = input('what method?\n1:add\n2:subtract\n3:multiply\n')
    if thing == '1':
        output = add()
    if thing == '2':
        output = sub()
    if thing == '3':
        output = multi()
    print('result:'+ str(output) + '\n')