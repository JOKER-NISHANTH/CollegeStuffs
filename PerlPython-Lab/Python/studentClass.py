class Student:
    def __init__(self, name="", mark=0):
        self.name = name
        self.mark = mark

    def display(self):
        print("Hai ", self.name)
        print("Your mark ", self.mark)

    def calculate(self):
        if(self.mark >= 90):
            print("You got first grade")
        elif(self.mark >= 75):
            print("You got second grade")
        elif(self.mark >= 50):
            print("You got third grade")
        else:
            print("You are failed")


i = 0
n = int(input("How many students ? "))
while(i < n):
    name = input("Enter the name : ")
    mark = int(input("Enter the mark : "))

    s = Student(name, mark)
    s.display()
    s.calculate()

    i += 1
    print("--"*15)
