class Employee:
    def __init__(self , fname , lname , salary) -> None:
        self.fname = fname
        self.lname = lname
        self.salary = salary


emp1 = Employee("Shashi" , "Chaurasia"  , 763746)
emp2 = Employee("Rohan" , "dev"  , 30746)
print(f"{emp1.fname}  :  {emp1.salary}   {emp2.fname}  : {emp2.salary}")