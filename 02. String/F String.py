apple = 3
banana = 2
pomegranate = 1
guava = 3
mango = 10

# Using "f" before a string or before a double-quoted statement("abc def g") makes it F-string.
# This is helpful, if there are a lot of variables to print.

fruits = f"I have {apple} Apples, {banana} Bananas, {pomegranate} Pomegranate, {guava} Guavas, {mango} Mangoes. "\
         f"So, I have {apple + banana + pomegranate + guava + mango} fruits in total!!"

print(f"{fruits}\n\nYay!! I am a fruit seller!!")
