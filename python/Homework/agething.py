names = ["bob","phil","dave","dan"]
ages = [43,62,27,16]

user_inp = input("Enter you name:")
print(f"Your age is {ages[names.index(user_inp)]}")

user_age = int(input("Enter your age:"))

for i in ages:
    if i > user_age:
        print(f"Your younger than {names[ages.index(i)]}")
    elif i < user_age:
        print(f"Your older than {names[ages.index(i)]}")
    else:
        print(f"Your the same age as {names[ages.index(i)]}")