storage = int(input("Enter desired storage in GB:"))
portable = True if input("Do you need it portable?") == "yes" else False
durable = True if input("Do you need it durable?") == "yes" else False
cheap = True if input("Do you need it cheap?") == "yes" else False
quick = True if input("Do you need it quick?") == "yes" else False

#Magnetic:   Portable,  not durable,    cheap,     mid speed,  256GB
#Solid state:Portable,  durable,        expensive, high speed  >256GB
#Optical:    Portable,  mid durability, cheap,     low speed   25GB

if storage > 256:
    if cheap == False:
        print("Choose solid-state storage")
    else:
        print("Change your standards")
elif storage > 25:
    if durable == False:
        print("Choose magnetic storage")
    elif cheap == False:
        print("Choose solid-state storage")
    else:
        print("Change your standards")
else:
    if quick == False:
        print("Choose optical storage")
    elif cheap == False:
        print("Choose solid-state storage")
    elif durable == False:
        print("Choose magnetic storage")
    else:
        print("Change your standards")