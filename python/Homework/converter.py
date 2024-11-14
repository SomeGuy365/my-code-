alpha = ["A","B","C","D","E","F"]

num = input("Enter number:")
choice = input("Is it denary or hexadecimal?d/h")

if choice == "d":
    p1 = int(num)//16
    p2 = int(num) % 16
    if p1 > 9:
        p1 = alpha[p1-10]

    if p2 > 9:
        p2 = alpha[p2-10]

    print(str(p1)+str(p2))

if choice == "h":
    if num[0] in alpha:
        p1 = (alpha.index(num[0])+10)*16
    else:
        p1 = int(num[0])

    if num[1] in alpha:
        p2 = alpha.index(num[1])+10
    else:
        p2 = int(num[1])

    print(p1+p2)
