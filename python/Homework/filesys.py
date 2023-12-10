
def write(mess):
    file = open("quick.txt","w")
    file.write(mess)

def read():
    file = open("quick.txt","r")
    print(file.read())

write(input("what to write:"))
read()