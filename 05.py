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

    def __add__(self , other):
        return self.salary + other.salary

    def __repr__(self) -> str:
        return 'Employee({} , {} , {})'.format(self.fname , self.lname , self.salary)


    def __str__(self) -> str:
        return "The salary of shashi is : {}".format(self.salary)



        

emp1 = Employee.from_str("shashi-chaurasia-89897")
print(repr(emp1))
print(emp1)
