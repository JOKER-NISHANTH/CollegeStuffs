
class Employer:
    def __init__(self, id=0, name="", salary=0):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print("ID : ", self.id)
        print("Name : ", self.name)
        print("Salary : ", self.salary)


class MyClass:
    @staticmethod
    def myMethod(e):
        e.salary += 1000
        e.display()


eid = int(input("Enter the Id : "))
ename = input("Enter the name : ")
esalary = int(input("Enter the salary : "))
emp = Employer(eid, ename, esalary)
MyClass.myMethod(emp)
