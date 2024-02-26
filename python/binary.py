import math

imp2 = input("Enter a sentence")

imp1 = 0

list = []

abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for x,something in enumerate(imp2):
    print(x,something)
    if something in abc:
        imp1 = ord(something)
        print(imp1)
        list.append('  ')
        while imp1 > 0:
            rem = imp1%2
            rem = str(rem)
            list.append(rem)
            imp1 = math.floor(imp1/2)
    elif something == ' ':
        list.append('  ')
        list.append(0)
        




list.reverse()
out = ''.join(str(x) for x in list)
out2 = out.split(' ')
out2.reverse()
out3 = ','.join(str(x) for x in out2)
out_len = len(out3)
out2 = out3.replace(',',' ',out_len)
print(out2)
