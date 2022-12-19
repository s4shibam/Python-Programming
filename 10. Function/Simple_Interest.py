test = "Simple_Interest Function has been called."


def SI():
    p = int(input("Enter Principal Amount = "))
    r = int(input("Enter Rate of Interest = "))
    t = int(input("Enter Year Duration = "))
    print(f"  Principal = {p}")
    print(f"  Rate of Interest = {r}")
    print(f"  Years = {t}")
    return p*r*t/100

print("Name is ", __name__)
if __name__ == '__main__':

    success = "Yeah!! I am selected in Microsoft!!!"
    result = SI()
    print(f"Interest Amount = {result}")

