class Member:
    def _init_(self,name,age, phonenumber,address,salary):
        self.name = name
        self.age = age
        self.phonenumber = phonenumber
        self.address = address
        self.salary = salary
    
    name = ""
    age = 0
    phonenumber = 0
    address = ""
    salary = 0.0

    def printSalary(self):
        print("Salary is :", self.salary)


class Employee(Member):
    def _init_(self, name , age , pn , address , salary , spec):
        super()._init_(name, age, pn , address , salary)
        self.specialization = spec

    specialization = ""
    

class Manager(Member):
    def _init_(self, name, age, phonenumber, address, salary,depart):
        super()._init_(name, age, phonenumber, address, salary)
        self.department = depart
    department = ""


class Test:
    mukesh = Employee("Mukesh",23,123456789,"Ujjain",17000,"Sales")
    rakesh = Manager("Rakesh",34,123456789,"Ratlam",25000,"Marketing")

    rakesh.printSalary()
    
