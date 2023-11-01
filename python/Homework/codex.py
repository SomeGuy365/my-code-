alpha = 'abcdefghijklmnopqrstuvwxyz'
out= ''

shift = int(input('How much do you want to shift?'))
mode = input('1:Encode\n2:Decrypt\n')

message = input('what do you want to encode?')

if mode == '1':
    for i in message:
        if alpha.index(i) == len(alpha)-1:
            out += alpha[shift-1]
        else:
            out += alpha[alpha.index(i)+shift]
elif mode == '2':
    for i in message:
        if alpha.index(i) == 0:
            out += alpha[len(alpha)-shift]
        else:
            out += alpha[alpha.index(i)-shift]

print(out)