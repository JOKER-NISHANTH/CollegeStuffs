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
moreThenLetter = []
sentence = list((input("Enter the sentence : ").lower()).split(" "))
for word in sentence:
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
        moreThenLetter.append(word)

masterList = [oneLetter, twoLetter, threeLetter, fourLetter, fiveLetter,
              sixLetter, sevenLetter, eightLetter, nineLetter, tenLetter, moreThenLetter]

for isEmpty in masterList:
    if isEmpty != []:
        print(isEmpty)
