catalogue = {
    "bag": 5 ,
    "t-shirt": 7 ,
    "trousers": 6,
    "shorts": 5,
    "fancy shoes": 23,
    "cheap shoes": 4,
    "belt": 2,
    "sunglasses": 3,
    "cool hat": 7,
    "tophat": 12
}

user_choice = ""
total = 0

for i in catalogue:
    print(f"{i.capitalize()} : £{catalogue[i]}")

print("Type Checkout to finish shoping")

while user_choice != "checkout":
    user_choice = input("What you wanna get?").lower()
    if user_choice in catalogue:
        total += catalogue[user_choice]
        continue
    elif user_choice != "checkout":
        print("Nice Try >:(")
        continue

print(f"Your total is £{total}")
if input("Have you got a discount?") == "y":
    if input("Enter Code:") == "Happy2024":
        total = float(total)/2
        print(f"Your new total is £{total}!")

