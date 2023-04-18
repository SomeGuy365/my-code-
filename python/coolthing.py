
#FIBBONACCI SEQUENCE!

import time

num1 = 0
num2 = 1
print(num1,num2)

output = [0,1]

userinp = input('how many nums?')

for i in range(int(userinp)-2):
    num3 = num1 +num2
    num1 = num2
    num2 = num3
    output.append(num2)

for x,i in enumerate(output):
    print(x+1,i)
    time.sleep(0.2)