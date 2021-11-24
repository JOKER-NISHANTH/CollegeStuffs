
#  Using randint
from random import choice
from random import randint

names = ["Jack", "Jim", "Joker", "Tom", "Jerry", "Ben"]
verbs = ["was", "is", "are", "were", "ate",
         "kicked", "drank", "paid", "threw", "bought"]
nouns = ["playing a game", "watching television", "talking", "dancing",
         "speaking", "a cat", "a shopkeeper", "a ball", "a computer"]
while True:
    print(names[randint(0, len(names)-1)]+" "+verbs[randint(0,
          len(verbs)-1)]+" "+nouns[randint(0, len(nouns)-1)])
    break


#  Using choice
names = ["Jack", "Jim", "Joker", "Tom", "Jerry", "Ben"]
verbs = ["was", "is", "are", "were", "ate",
         "kicked", "drank", "paid", "threw", "bought"]
nouns = ["playing a game", "watching television", "talking", "dancing",
         "speaking", "a cat", "a shopkeeper", "a ball", "a computer"]
while True:
    a = (choice(names))
    b = (choice(verbs))
    c = (choice(nouns))
    print(a+" ", b+" ", c)
    break
