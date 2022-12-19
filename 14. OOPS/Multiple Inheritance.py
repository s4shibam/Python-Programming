class employee():
    holiday = 150

    def __init__(self, nm, age, desg, sal):
        #
        self.name = nm
        self.age = age
        self.designation = desg
        self.salary = sal

    def print_details(self):  # self represents the instance of the class.
        return f"Employee Name: {self.name}, \tAge: {self.age} \tDesignation: {self.designation}, \tSalary: {self.salary}"


class special_employee(employee):
    holiday = 160

    def __init__(self, nm, age, desg, sal, webd):
        self.name = nm
        self.age = age
        self.designation = desg
        self.salary = sal
        self.webd = webd

    def print_freelancer(self):
        return f"Employee Name: {self.name}, \tAge: {self.age} \tDesignation: {self.designation}, \tSalary: {self.salary} " \
               f"Freelancer: {self.webd}"


class player(special_employee):
    holiday = 170

    def __init__(self, nm, game):
        self.name = nm
        self.game = game

    def print_player(self):
        return f"{self.name} Plays: {self.game}"


# These parameters are passing through __init__ function.
sunabha = employee('Sunabha Panda', 23, 'SWE II', '35 LPA')
pritam = employee('Pritam Gain', 22, 'SDE I', '29 LPA')
shibam = special_employee('Shibam Saha', 26, 'SDE III',
                          '63 LPA', 'MERN Stack Dev, Blockchain Specialist')
johnny = player('Johnny Sarkar', 'Football')

# Here "sunabha" named instance passes as a parameter under print_details().
print(sunabha.print_details())
print(pritam.print_details())
# Here "shibam" named instance passes as a parameter under print_freelancer().
print(shibam.print_freelancer())
print("Holiday for Shibam", shibam.holiday)
print(johnny.print_player())
