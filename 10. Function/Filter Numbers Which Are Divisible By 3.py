numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def is_div_by_3 (num):
    return num%3 == 0

div_by_3 = list(filter(is_div_by_3, numbs))
print(f"Numbers which are divisible by 3 are {div_by_3}")