from datetime import datetime

# datetime object containing current date and time
now = datetime.now()


def dt():
    return now.strftime("%d/%m/%Y at %H:%M:%S")


def add_data():
    """
     This function is made to receive data regarding exercise or food from user.
     :return: 0
    """
    print("\nEnter details to save your data: ")
    add_type = int(input("   Have you exercised? --> Press 1\n"
                         "   Have you eaten? --> Press 2\n      Your Choice? "))
    if (add_type == 1):
        exercise = input("   What exercises have been done? ")
        with open(f"{name}_exercise.txt", "a") as f:
            f.write(f"On {str(dt())} I had done {exercise}.\n")

        print("----------------------------")
        print("Data successfully uploaded!!")

    elif add_type == 2:
        food = input("   Which food was eaten? ")
        with open(f"{name}_food.txt", "a") as f:
            f.write(f"On {str([str(dt())])} I had eaten {food}.\n")

        print("----------------------------")
        print("Data successfully uploaded!!")

    else:
        print("\nWrong input!!")

    return 0


def get_data():
    """
         This function is made to show data regarding exercise or food from user.
         :return: 0
    """
    print("\nEnter details to fetch your data: ")
    add_type = int(input("   I want to know what exercises I did! --> Press 1\n"
                         "   I want to know which food I ate! --> Press 2\n        Your Choice? "))
    if add_type == 1:
        print("-----------------\n")
        with open(f"{name}_exercise.txt") as f:
            for i in f:
                print(i, end="")
        print("\n-------\nDone!!")

    elif add_type == 2:
        print("-----------------\n")
        with open(f"{name}_food.txt") as f:
            for i in f:
                print(i, end="")
        print("\n-------\nDone!!")

    else:
        print("\nWrong input!!")

    return 0


print("----------------------------")
print("  Health Management System  ")
print("----------------------------\n")

print("Who are you?")
name = input("My name is ")

print(f"Hello {name}, What do you want to do now?\n")

opt = int(input("Press (1) to Add Data in our system!\n"
                "Press (2) to Retrieve Data from our system!\n   Your Choice? "))

if opt == 1:
    add_data()
elif opt == 2:
    get_data()
else:
    print("\nWrong input!!")
