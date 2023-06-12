# first take the total limit
n = int(input("Enter the size of the list: ").strip())

# second take the list of values all at once
arr = list(map(int, input("Enter the values of the list seperating by space: ").rstrip().split()))

print("")
print(arr)
print("")

arr.sort()
print(arr)


# learn how to apply count sorting