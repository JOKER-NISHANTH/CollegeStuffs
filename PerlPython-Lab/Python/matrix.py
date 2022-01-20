

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Display the list as it is \2")
print(mat)

print("Display row by row")
for r in mat:
    print(r)

print("Display each column in row 0 ")
for i in mat[0]:
    print(i, end=" ")
print()

print("Display each column in row 1 ")
for i in mat[1]:
    print(i, end=" ")
print()

print("Display each column in row 2 ")
for i in mat[2]:
    print(i, end=" ")
print()

print("Display all elements using for : ")
for r in mat:
    for c in r:
        print(c, end=" ")
    print()

'''
        OUTPUT

Display the list as it is
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Display row by row
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Display each column in row 0
1 2 3

Display each column in row 1
4 5 6

Display each column in row 2
7 8 9

Display all elements using for :
1 2 3
4 5 6
7 8 9

'''
