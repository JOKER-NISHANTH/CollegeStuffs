
def towers(n, a, b, c):
    if(n == 1):
        return print('Move disk %d from pole %s to pole %s. ' % (n, a, c))

    towers(n - 1, a, c, b)
    print('Move disk %d from pole %s to pole %s. ' % (n, a, c))
    towers(n - 1, b, a, c)


n = int(input('Enter the number of disks: '))

towers(n, 'A', 'B', 'C')


'''
            OUTPUT

Enter the number of disk : 3
Move disk 1 from pole A to pole C.
Move disk 2 from pole A to pole B.
Move disk 1 from pole C to pole B.
Move disk 3 from pole A to pole C.
Move disk 1 from pole B to pole A.
Move disk 2 from pole B to pole C.
Move disk 1 from pole A to pole C.

'''
