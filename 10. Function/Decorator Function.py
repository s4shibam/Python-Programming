from time import sleep


def decot(func1):
    def nowexe():
        print("Executing now....")
        sleep(1)
        func1()
        print("Executed!!")
    return nowexe


@decot
def shibam():
    print("Shibam is a programmer!")


shibam()
