def towers(n, a, c, b):
    if n == 1:
        print("Move disk %i from pole %s to pole %s" % (n, a, c))
    else:
        towers(n-1, a, b, c)
        print("Move disk %i from pole %s to pole %s" % (n, a, c))
        towers(n-1, b, c, a)


n = int(input("Enter the number of disk : "))
towers(n, 'A', 'B', 'C')

'''
            OUTPUT

Enter the number of disk : 3
Move disk 1 from pole A to pole B
Move disk 2 from pole A to pole C
Move disk 1 from pole B to pole C
Move disk 3 from pole A to pole B
Move disk 1 from pole C to pole A
Move disk 2 from pole C to pole B
Move disk 1 from pole A to pole B


'''
