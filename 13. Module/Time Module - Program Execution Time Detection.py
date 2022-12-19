import time

start = time.time()  # Storing the starting time in a variable
print(start)
for i in range(450):
    print("Salman Weds Katrina is a dream for Bhai fans")

# Prints (current time - starting time)
print(f"For loop execution time = {time.time() - start} secs.")

start = time.time()  # Resetting the starting time

k = 0
while k < 450:
    print("Salman Weds Katrina is a dream for Bhai fans")
    k += 1

# Prints (current time - starting time)
print(f"While loop execution time = {time.time() - start} secs.")
