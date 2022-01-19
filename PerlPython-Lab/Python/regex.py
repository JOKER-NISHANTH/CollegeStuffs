import imp
import re
from datetime import datetime


def rsplit():
    print("Spliting a sentence")
    print("--"*10)
    a = input("Enter a sentence to split : ")
    print(re.split(" ", a))


def rjoin():
    print("Join a sentence")
    print("--"*10)
    a = input("Enter a string : ")
    b = input("Enter a character to join : ")
    print(b.join(a))


def rsubn():
    '''subn(pattern, repl, string)'''
    print("Subn a sentence")
    print("--"*10)
    a = input("Enter a string : ")
    b = input("Enter a search String : ")
    c = input("Enter the replace string : ")
    print(re.subn(b, c, a))


def rfindall():
    '''findall(pattern, string)'''
    print("Findall a sentence")
    print("--"*10)
    a = input("Enter a sentence : ")
    b = input("Enter a word to find : ")
    c = re.findall(b, a)
    if c:
        print("The given word %s is found in %s" % (b, a))
    else:
        print("The given word %s is not found in %s" % (b, a))


def rsearch():
    '''search(pattern, string)'''
    print("Search a sentence")
    print("--"*10)
    a = input("Enter a sentence : ")
    b = input("Enter a word to search : ")
    c = re.search(b, a)
    if c:
        print("The given word %s is found in %s" % (b, a))
    else:
        print("The given word %s is not found in %s" % (b, a))


def rmatch():
    '''match(pattern, string)'''
    print("Match a sentence")
    print("--"*10)
    a = input("Enter a sentace : ")
    b = input("Enter a word to match : ")
    c = re.match(b, a)
    if c:
        print("The given word %s is found in %s" % (b, a))
    else:
        print("The given word %s is not found in %s" % (b, a))


def remail():
    '''sub(pattern,repl, string)'''
    print("Replace an Email Address")
    print("--"*10)
    a = input("Enter a current email id : ")
    b = input("Enter which has to replace : ")
    c = input("Enter what should be replace : ")
    email = re.sub(b, c, a)
    print("The old email id : %s" % (a))
    print("The replaced email id is %s" % (email))


def rdate():
    '''Print date'''
    print("Extracting current date")
    print("--"*10)
    now = datetime.now()
    print("Current date is %s " % now)
    c = now.strftime("%d %B %y ")
    print("Current date DD MM YY is %s" % c)


def main():
    print("\n 1. Split \n 2. Join \n 3. Subn \n 4. Findall \n 5. Search \n 6.Match \n 7.Replace an email address \n 8.Extract current Date \n 9. Exit")
    ch = int(input("Enter the choice "))

    if (ch == 1):
        rsplit()
        main()

    elif (ch == 2):
        rjoin()
        main()

    elif (ch == 3):
        rsubn()
        main()

    elif (ch == 4):
        rfindall()
        main()

    elif (ch == 5):
        rsearch()
        main()

    elif (ch == 6):
        rmatch()
        main()

    elif (ch == 7):
        remail()
        main()

    elif (ch == 8):
        rdate()
        main()

    elif (ch == 9):
        exit()

    else:
        main()


if __name__ == "__main__":
    main()
