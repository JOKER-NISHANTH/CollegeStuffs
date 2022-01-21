
class Bank:

    def __init__(self, name="", balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withDraw(self, amount):
        if amount > self.balance:
            print("Balance amount is less , so no withdrawal.")
        else:
            self.balance -= amount
        return self.balance


name = input("Enter the name : ")
b = Bank(name)

while(True):
    print(' d -Desposit , w -Withdraw , e -Exit')
    choice = input("Enter your choice : ").lower()

    if choice == 'e':
        exit()

    amt = float(input("Enter the amount : "))

    if choice == 'd':
        print("Balance after deposit : ", b.deposit(amt))

    elif choice == 'w':
        print("Balance after withdraw : ", b.withDraw(amt))
    else:
        print("Invalid Option")
