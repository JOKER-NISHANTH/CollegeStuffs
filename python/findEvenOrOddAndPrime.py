choice = int(input('''
    1 for Odd or Even
    2 for Prime or Not

    Enter the choice : '''))

if choice == 1:
    num = int(input("Enter the number : "))
    if num % 2 == 0:
        print(num, " is Even")
    else:
        print(num, " is Odd")
elif choice == 2:
    num = int(input("Enter the number : "))
    if num > 1:

        for i in range(2, int(num/2)+1):
            if(num % i) == 0:
                print(num, " is not a prime")
                break
        else:
            print(num, " is a prime")

    else:
        print(num, " is not a prime")

else:
    print("Invalid choice , \n please enter correct choice :)")
