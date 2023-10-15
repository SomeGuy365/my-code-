nums = []
total = 0
mean = 0

while mean < 4:
    total = 0
    user_imp = int(input('enter a num:'))
    nums.append(user_imp)
    for i in nums:
        total += i
    mean = total/len(nums)

print(f'Your mean is {mean}!')