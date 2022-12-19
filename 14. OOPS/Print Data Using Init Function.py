class employee():
    def __init__(self, nm, age, desg, sal):
        #
        self.name = nm
        self.age = age
        self.designation = desg
        self.salary = sal

    def print_details(self):    # self represents the instance of the class.
        return f"Employee Name: {self.name}, \tAge: {self.age} \tDesignation: {self.designation}, \tSalary: {self.salary}"


# This parameters are passing through __init__ function.
sunabha = employee('Sunabha Panda', 21, 'SWE II', '35 LPA')
pritam = employee('Pritam Gain', 18, 'SDE I', '29 LPA')

# Here "sunabha" named instance passes as a parameter under print_details().
print(sunabha.print_details())
print(pritam.print_details())
