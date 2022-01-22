def stack():
    stack = []

    def pushIt():
        stack.append(input("Enter the element : "))

    def popIt():
        if len(stack) != 0:
            print(stack.pop(), " is remove from stack")

    def view():
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Element in stack ", stack)

    def menu():
        print("Stack operation")
        print("--" * 15)
        print("1. Push \n 2. Pop \n 3. Main menu \n 4.Exit")
        ch = int(input("Enter the choice : "))
        if ch == 1:
            pushIt()
            view()
            menu()
        elif ch == 2:
            popIt()
            view()
            menu()
        elif ch == 3:
            main()

        elif ch == 4:

            exit()

        else:
            print("Invalid options ")
            menu()
    menu()


def queue():
    queue = []

    def insert():
        queue.append(input("Enter the element : "))

    def delete():
        if len(queue) != 0:
            print(queue.pop(0), " is remove from queue")

    def view():
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Element in queue ", queue)

    def menu():
        print("Queue operation")
        print("--" * 15)
        print("1. Insert \n 2. Delete \n 3. Main menu \n 4.Exit")
        ch = int(input("Enter the choice : "))
        if ch == 1:
            insert()
            view()
            menu()
        elif ch == 2:
            delete()
            view()
            menu()
        elif ch == 3:
            main()
        elif ch == 4:
            exit()
        else:
            print("Invalid Options ")
            menu()
    menu()


def main():
    print("Stack and Queue Operations")
    print("--"*15)

    print("\n 1. Stack \n 2. Queue  \n 3. Exit")
    ch = int(input("Enter your choice : "))

    if (ch == 1):
        stack()

    elif(ch == 2):
        queue()

    elif(ch == 3):
        exit()

    else:
        print("Invalid choice")
        main()


if __name__ == "__main__":
    main()
