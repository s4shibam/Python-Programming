class employee():
    no_of_leaves = 5

    def __init__(self, nm, age, desg, sal):
        self.name = nm
        self.age = age
        self.designation = desg
        self.salary = sal

    def print_details(self):  # self represents the instance of the class.
        return f"Employee Name: {self.name}, \tAge: {self.age} \tDesignation: {self.designation}, \tSalary: {self.salary}"

    @classmethod
    def change_leaves(cls, new_leaves):  # Parameters --> Class of the instance variable, another parameter.
        cls.no_of_leaves = new_leaves

    @classmethod
    def from_slash(cls, str):
        """
        Takes a single string input and returns multiple string for parameter in class employee, __init__ function.
        """
        # params = str.split("/")
        # return cls(params[0], params[1],params[2], params[3])

        # Single line code for the previous 2 commented lines.
        return cls(*str.split("/"))




sunabha = employee('Sunabha Panda', 21, 'SWE II', '35 LPA')  # These parameters are passing through __init__ function.
pritam = employee('Pritam Gain', 18, 'SDE I', '29 LPA')

# Calls from_str() to convert the single string input into multiple string for __init__ function parameters.
shibam = employee.from_slash("Shibam Saha/29/SDE III/47 LPA")

print(sunabha.print_details())  # Here "sunabha" named instance passes as a parameter under print_details().
print(pritam.print_details())
print(shibam.print_details())
print()

print("Before change: No of leaves under employee class = ", employee.no_of_leaves)

sunabha.change_leaves(12)

print("After change: No of leaves under employee class = ", employee.no_of_leaves)
print("Sunabha's No. of Leaves = ", sunabha.no_of_leaves)
