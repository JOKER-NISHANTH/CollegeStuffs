# Declare the empty list
oneLetter = []
twoLetter = []
threeLetter = []
fourLetter = []
fiveLetter = []
sixLetter = []
sevenLetter = []
eightLetter = []
nineLetter = []
tenLetter = []
moreThenTenLetter = []

# get the input from user as a sentence -> convert to lowercase(for standard output) -> split the sentence based on space -> and finally convert string to list
sentence = list((input("Enter the sentence : ").lower()).split(" "))

# iterate the list
for word in sentence:
    # get the length of iteration word
    letter = len(word)

    if letter == 1:
        oneLetter.append(word)
    elif letter == 2:
        twoLetter.append(word)
    elif letter == 3:
        threeLetter.append(word)
    elif letter == 4:
        fourLetter.append(word)
    elif letter == 5:
        fiveLetter.append(word)
    elif letter == 6:
        sixLetter.append(word)
    elif letter == 7:
        sevenLetter.append(word)
    elif letter == 8:
        eightLetter.append(word)
    elif letter == 9:
        nineLetter.append(word)
    elif letter == 10:
        tenLetter.append(word)
    else:
        moreThenTenLetter.append(word)

# create new list and add the exciting lists to new list (like list of list) for remove the empty list :)
masterList = [oneLetter, twoLetter, threeLetter, fourLetter, fiveLetter,
              sixLetter, sevenLetter, eightLetter, nineLetter, tenLetter, moreThenTenLetter]

for isEmpty in masterList:
    if isEmpty != []:
        print(isEmpty)
