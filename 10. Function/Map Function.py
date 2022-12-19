numbs = ["24", "89", "12", "76", "69", "5", "15"]

# for i in range (len(numbs)):
#     numbs[i] = int(numbs[i])

numbs = list(map(int, numbs))
# map() function returns a map object(which is an iterator) of the results after applying the given function to each
# item of a given iterable (list, tuple etc.)
# map(fun, iter) --> Format

print(f"{numbs[1]} + {numbs[2]} = {numbs[1] + numbs[2]}")
print(f"{numbs[2]} + {numbs[3]} = {numbs[2] + numbs[3]}")


numbs_sq = list(map(lambda x: x**2, numbs))

print(f"Square = {numbs_sq}")
