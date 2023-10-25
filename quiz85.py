class Citizen:
    def __init__(self,name,city,status) -> None:
        self.name = name
        self.city = city
        self.status = status

    def getName(self):
        return self.name
    
    def getCity(self):
        return self.city
    
    def getStatus(self):
        return self.status
    
class Employee(Citizen):
    def __init__(self, name, city, status, annual_salary) -> None:
        super().__init__(name, city, status)
        self.annual_salary = annual_salary

    def getSalary(self):
        return self.annual_salary
    
class PartTimeEmployee(Employee):
    def __init__(self, name, city, status, annual_salary, fraction, union_member) -> None:
        super().__init__(name, city, status, annual_salary)
        self.fraction = fraction
        self.union_member = union_member

bob = Citizen("Bob",'Tokyo','Alive')
alice = Employee("Alice", "Kyoto", "Alive", 100000)
joe = PartTimeEmployee("Joe","Nagano","Alive",50000,0.5,False)

print(bob.getName())
print(alice.getName())
print(joe.getName())