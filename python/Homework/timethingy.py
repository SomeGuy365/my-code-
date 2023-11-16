import time
times = time.time()
rawtime = time.localtime(times)
actualhour = time.strftime("%H",rawtime)
actualmin = time.strftime("%M",rawtime)
actualsec = time.strftime("%S",rawtime)

print(f"You are {24-int(actualhour)} hours, {60-int(actualmin)} minutes and {60-int(actualsec)} seconds from midnight")