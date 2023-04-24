from datetime import date
#read todays date
x_date = date.today()
day = x_date.weekday()
#the if statement reading the 0-6 index
if day < 5:
    print("Today is during the week :(")
else:  # 5 Sat, 6 Sun
    print("It's the weekend!")