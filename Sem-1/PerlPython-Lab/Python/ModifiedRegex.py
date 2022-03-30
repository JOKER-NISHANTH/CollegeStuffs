import re

from datetime import datetime


def rsplit():
    print("Split String")
    print(" -- " * 15)
    print(re.split(" ", input(" Enter the sentance : ")))


def rjoin():
    print("Join String")
    print(" -- " * 15)
    print(input(" Enter the string : ").join(input("Enter the sentance : ")))


def rsubstr():
    print(" Substrig ")
    a = input("Enter the sentance : ")
    print(re.subn(input("Enter the word to search : "),
          input("Enter the word to replace : "), a))


def rfindall():
    a = input("Enter the sentance : ")
    print(re.findall(input(" Enter the word to search "), a))


def rsearch():
    a = input("Enter the sentance : ")
    c = re.search(input(" Enter the word to search : "), a)
    if c:
        print("Searching value is found")
    else:
        print("Searching value is not found")


def rmatch():
    a = input("Enter the sentance : ")
    c = re.match(input(" Enter the word to search : "), a)
    if c:
        print("Matching value is found")
    else:
        print("Matching value is not found")


def remail():
    a = input("Enter the current email : ")
    email = re.sub(input("Enter the word to search : "),
                   input("Enter the word to replace : "), a)
    print("Old email : %s " % a)
    print("New email : %s " % email)


def rdate():
    cdate = datetime.now().strftime("%d %B %y")
    print("Current time : %s" % cdate)


def main():
    print("  Regex Operations  ")
    print(" -- " * 15)
    print("\n 1. Split \n 2. Join \n 3. Substring \n 4. Findall \n 5. Search \n 6. Match \n 7. Replace email \n 8. Extract current date \n 9. Exit")
    ch = int(input(" Enter the choice : "))

    if ch == 1:
        rsplit()
        main()
    elif ch == 2:
        rjoin()
        main()
    elif ch == 3:
        rsubstr()
        main()
    elif ch == 4:
        rfindall()
        main()
    elif ch == 5:
        rsearch()
        main()
    elif ch == 6:
        rmatch()
        main()
    elif ch == 7:
        remail()
        main()
    elif ch == 8:
        rdate()
        main()
    elif ch == 9:
        exit()
    else:
        print("Invalid choice")
        main()


if __name__ == "__main__":
    main()
