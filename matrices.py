# Working with matrices
matrices = []

# taken info in the row and column of the matrix
# class for takinng row and column values
def input_matrix():
    row = list(map(int, input("Enter the values of the row: ").strip().split()))
    return row

def checker(col_size, row):
    # checking for the col size 
    if len(row) == col_size:
        matrices.append(row)
    else:
        print("The size of the values entered is not the same as the column size you specified")
        print("The column size is " + str(col_size) + " and the values you just entered sums up to " + str(len(row)))
        print("Please retry")
        input_matrix()

# function for display of matrices
def matrix():
    for item in matrices:
        print(item)

# row
row_size = int(input("Enter the size of the row (row x column): ").strip())
col_size = int(input("Enter the size of the column (row x column): ").strip())
print("")

print("One row at a time. Column is equal to the size of the array.")
for value in range(0, row_size):
    result = input_matrix()
    re_s = checker(col_size, result)
matrix()
# second level
def difference(matrices, n):
 
    # Initialize sums of diagonals
    d1 = 0
    d2 = 0
 
    for i in range(0, n):
     
        for j in range(0, n):
            # finding sum of primary diagonal
            if (i == j):
                d1 += matrices[i][j]
 
            # finding sum of secondary diagonal
            if (i == n - j - 1):
                d2 += matrices[i][j]
         
    # Absolute difference of the sums across the diagonals
    return abs(d1 - d2)

print("\n" + "This is a " + str(row_size) + " x " + str(col_size) + " matrix")
print("BELOW IS THE DIAGONAL SUMMATION OF THE MATRIX ABOVE")
sumation = difference(matrices, row_size)

print("Absolute difference of the matrix: " + str(sumation))

# summing the left to right and right to left diagonals
