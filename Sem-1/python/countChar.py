# Python 3.x.x
sentence = input("Enter the sentence : ")
# Python 2.7.x
# sentence = raw_input("Enter the sentence : ")

count = {}
for letter in sentence:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1

print("Count of all characters in : " + sentence + " is :\n "
      + str(count))
