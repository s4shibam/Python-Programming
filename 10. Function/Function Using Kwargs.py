# The special syntax **kwargs in function definitions in python is used to pass a keyworded,
# variable-length argument list. We use the name kwargs with the double star. The reason is because
# the double star allows us to pass through keyword arguments (and any number of them).

def topper_boys(heading, **kwargs):
    print(heading)
    for name, company in kwargs.items():
        print(f"{name} placed in {company}.")


statement = "Placement Drive 2022:\n"
name_comp = {"Abhirup": "Uber", "Sunabha": "Google",
             "Srinjoy": "Sri Cement Constructions", "Shibam": "DE shaw",
             "Pritam": "Microsoft"}

topper_boys(statement, **name_comp)
