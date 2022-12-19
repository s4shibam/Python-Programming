class student:
    college = 'IEM'
    # If user do not want to execute any type of action then "pass" command should be used.
    pass


# Instance − An individual object of a certain class. Here, the following variable are instance variables.
s1 = student()  # s1 is derived under "student" class
s2 = student()  # s2 is derived under "student" class
s3 = student()  # s3 is derived under "student" class

print(s1)
print(s2)

# Object_name.variable_name = “abc”
s1.name = "Shibam Saha"
s1.stream = 'CSE'
s1.year = 2

# Object_name.variable_name = 123
s2.name = "Sunabha Panda"
s2.stream = 'CS IT'
s2.year = 3

# Object_name.variable_name = 12.34
s3.name = "Soumyadeep Roy"
s3.stream = 'AIML'
s3.year = 1

print("\nObject_name.variable_name -->\n")
print(s1.name, s1.stream, s1.year, s1.college)
print(s2.name, s2.stream, s2.year, s2.college)
print(s3.name, s3.stream, s3.year, s3.college)

print("\nObject_name.__dict__ -->\n")
print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)
print()
print("College name under Student Class = ", student.college)
print(student.__dict__)

student.college = 'Jadavpur University'

print('\nAfter changing the value of student.college variable.')
print(s1.name, "--> ", s1.college)

print('\nAfter changing the value of s2.college variable.')
s2.college = 'IIT Bombay'
print(s2.name, "--> ", s2.college)
