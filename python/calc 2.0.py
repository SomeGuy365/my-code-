userinp = input('input:\n')
output = 0

newlist = list(userinp)
if newlist[1] == '+':
    for nums in newlist:
        if nums == '+':
            continue
        else:
            output += int(nums)
if newlist[1] == '-':
    output = int(newlist[0])
    for nums in newlist:
        if nums == '-' or nums == newlist[0]:
            continue
        else:
            output -= int(nums)

print(output)