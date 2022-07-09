# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
import datetime as dt
date = dt.datetime.now()
weekday = date.weekday()
if weekday == 1:
    day = "Mon"
elif weekday == 2:
   day = "Tue"
elif weekday == 3:
    day = "Wed"
elif weekday == 4:
    day = "Thu"
elif weekday == 6:
    day = "Sat"
else:
    day = "Sun"
if day in ["Mon","Tue","Wed","Thu","Fri"]:
    fare = 100
elif day == "Sat":
    fare = 60
else:
    fare = 80
print("Date:",date)
print("Day:",day)
print("Fare:",fare)