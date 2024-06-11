corenum = int(input("Enter Number of Cores:"))
corespeed = int(input("Enter core speed in Hertz:"))
ips = corenum*corespeed

print("Your compurter can do",ips,"instructions per second")

instrnum = int(input("How many instructions do you want to do?"))

print("That will take",instrnum/ips,"seconds")