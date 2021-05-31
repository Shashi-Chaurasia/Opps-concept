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


emp1 = Employee("Shashi" , "Chaurasia"  , 763746)
emp2 = Employee("Rohan" , "dev"  , 30746)

Employee.update_salary(2)
emp1.increment_salary()
print(emp1.salary)

