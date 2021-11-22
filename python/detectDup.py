myList = []
while(True):
    number = int(input("Enter the number : "))
    if(number not in myList):
        myList.append(number)
    else:
        print("Given number is already exists :) ")
        choice = int(
            input("Enter 1 for break 2 for continue any key for exit : "))
        if choice == 1:
            break
        elif choice == 2:
            continue
        else:
            exit()
