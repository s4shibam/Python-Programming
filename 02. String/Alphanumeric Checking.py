"""
Alphanumeric Checking --> The "isalnum()" method returns "True" if all characters in the string are alphanumeric
(either alphabets or numbers only). If not, it returns "False".
"""
s1 = "abc"
print(s1.isalnum())

s2 = "abc123"
print(s2.isalnum())

s3 = "123"
print(s3.isalnum())

s4 = "abc 123"  # Space present here, output will be "False"
print(s4.isalnum())
