def sq(x):
    return x**2


def cb(x):
    return x**3


func = [sq, cb]

for i in range(10):
    result = list(map(lambda x: x(i), func))
    print(f"For {i} --> {result}")
