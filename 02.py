class Employee:
    increment= 1.5
    def __init__(self , fname , lname , salary) -> None:
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increment_salary(self):
        self.salary = int(self.salary * self.increment)
    

emp1 = Employee("Shashi" , "Chaurasia"  , 763746)
emp2 = Employee("Rohan" , "dev"  , 30746)
print(emp1.salary)
emp1.increment_salary()
print(emp1.salary)


