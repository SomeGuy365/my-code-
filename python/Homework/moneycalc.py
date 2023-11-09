hours = float(input('How may hours a week?'))
wage = float(input('whats your hourly wage?'))
exthours = float(input('how many extra time hours a week?'))
extwage = float(input('whats hourly wage of extra time?'))
weeks = float(input('how many work weeks a year?')) 

print(f'You make £{weeks*((hours*wage)+(exthours*extwage))} a year')
