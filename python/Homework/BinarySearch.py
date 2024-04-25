names = ['Berners-Lee', 'Hopper', 'Lovelace', 'Turing', 'Von Neumann' ] 

found  = False 

name_wanted = input('select a name to search for…') 

if name_wanted not in names: 
    found = True
    print('yikes') 

ub = len(names)
lb = 0
while found == False and len(names) > 0: 
    position = (ub+lb)//2
    print(names[position])

    if names[position] == name_wanted : 
        print(name_wanted, 'is at position', position) 
        found = True 

    elif name_wanted in names[:position]: 
        ub = position-1
    else: 
        lb = position+1