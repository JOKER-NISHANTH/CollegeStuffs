elements = [1, 2, 3, 4, 5, 2, 3, 4, 7, 9, 5]

res = []

print("Duplicate value in the given list")

for item in elements:
    if item not in res:
        res.append(item)
    else:
        print(item, end=" ")
