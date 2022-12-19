import time
from datetime import datetime

now = datetime.now()

current_time = time.asctime(time.localtime())
current_time_2 = now.strftime("Date - %d-%m-%y \n"
                              "Time - %I:%M:%S %p")
print("Type 1: ")
print(current_time)
print()

print("Type 2: ")
print(current_time_2)
print("Day - ", datetime.today().strftime("%A"))
