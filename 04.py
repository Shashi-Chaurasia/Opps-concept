class Employee:
    increment= 1.5
    def __init__(self , fname , lname , salary) -> None:
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increment_salary(self):
        self.salary = int(self.salary * self.increment)
    @classmethod
    def update_salary(cls , new_Salary):
        cls.increment = new_Salary

    @classmethod
    def from_str(cls , emp_string):
        fname , lname , salary = emp_string.split("-")
        return cls(fname , lname , salary)

        

emp1 = Employee.from_str("shashi-chaurasia-89897")
print(emp1.lname)


# emp1 = Employee("Shashi" , "Chaurasia"  , 763746)
# emp2 = Employee("Rohan" , "dev"  , 30746)
# print(emp1.salary)
# emp1.increment_salary()
# print(emp1.salary)

