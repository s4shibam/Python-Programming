class employee():
    def print_details(self):    # self represents the instance of the class.
        return f"Employee Name: {self.name}, Designation: {self.desg}, Salary: {self.salary}"

sunabha = employee()
pritam = employee()

sunabha.name = 'Sunabha Panda'
sunabha.desg = 'Cloud Eng.'
sunabha.salary = " 35 LPA"

pritam.name = 'Pritam Gain'
pritam.desg = 'Front End Developer'
pritam.salary = "29 LPA"

print(sunabha.print_details())  # Here "sunabha" named instance passes as a parameter under print_details().
print(pritam.print_details())
