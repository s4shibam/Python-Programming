"""
Factorial logic:
# n! = n * n-1 * n-2 * n-3.......1
# n! = n * (n-1)!
"""


# Function for Factorial using Iterative Method
def factorial_iterative(n):
    # i = 1
    fac = 1
    if n == 1 or n == 0:
        return 1
    else:
        for i in range(n):
            # Initial "i" would be 0, that is why 1 is added to get proper result
            fac = fac * (i + 1)
    return fac


# Function for Factorial using Recursive Method
def factorial_recursive(n):
    """
    :param n: Integer
    :return:  n * n-1 * n-2 * n-3.......1

    Recursion Logic (Dry Run Output for input (3):
    factorial(3)          # 1st call with 3
    3 * factorial(2)      # 2nd call with 2
    3 * 2 * factorial(1)  # 3rd call with 1
    3 * 2 * 1             # return from 3rd call as number=1
    3 * 2                 # return from 2nd call
    6                     # return from 1st call
    """
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


n = int(input("Enter a number = "))
# Output after using Iterative Method
print(f"Factorial of {n} using Iterative Method = ", factorial_iterative(n))

# Output after using Recursive Method
print(f"Factorial of {n} using Recursion Method = ", factorial_recursive(n))
