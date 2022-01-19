

def stack():
    stack = []

    def pushit():
        stack.append(input("Enter the element : "))

    def popit():
        if len(stack) != 0:
            print(stack.pop(), " is removed stack")

    def view():
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Element is stack ", stack)

    def menu():
        print("\n Stack Operations")
        print("--"*10)
        print("\n 1. Push \n 2. Pop \n 3. Main menu \n 4. Exit")
        ch = int(input("Enter the choice : "))
        if (ch == 1):
            pushit()
            view()
            menu()

        elif (ch == 2):
            popit()
            view()
            menu()

        elif (ch == 3):
            main()

        elif (ch == 4):
            exit()

        else:
            print("Enter the valid choice ")
            menu()
    menu()


def queue():
    queue = []

    def ins():
        queue.append(input("Enter the element : "))

    def delete():
        if len(queue) != 0:
            print(queue.pop(0), " is removed from queue")

    def view():
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Element is queue : ", queue)

    def menu():
        print("\n Queue Operation")
        print("--"*10)
        print("\n 1. Insert \n 2.Delete \n 3. Main menu \n 4.Exit ")
        ch = int(input("Enter the choice : "))
        if ch == 1:
            ins()
            view()
            menu()

        elif ch == 2:
            delete()
            view()
            menu()

        elif ch == 3:
            menu()

        elif ch == 4:
            exit()

        else:
            print("Enter the valid choice : ")
            menu()
    menu()


def main():
    print("\n 1. Stack \n 2. Queue \n 3. Exit")
    ch = int(input("Enter the choice : "))
    if ch == 1:
        stack()
    elif ch == 2:
        queue()
    elif ch == 3:
        exit()
    else:
        print("Enter the valid choice ")
        main()


if __name__ == "__main__":
    main()
