# Finding all posible values that appears only once in an array
unique_ones = []
def unique(arr):
    size_arr = len(arr)
    new_arr_set = set(arr)

    print("Collcted Values: " + str(arr))
    print("Total Number of Collected Values: " + str(size_arr))
    print("Main Values: " + str(new_arr_set))

    # checking and counting the unique ones
    for value in new_arr_set:
        num_count = arr.count(value)
        # print(num_count)
        # print(type(new_arr_set))
        # print("")

        # making decision based on counts of the items in the set to the arr
        if num_count == 1:
            unique_ones.append(value)
    
    if len(unique_ones) == 0:
        print("")
        print("There is no value occuring once from the values you inputed.")
    
    return unique_ones

# first take the input from the user
arr = list(map(int, input("Enter the number values you wish to check separating with a space for each value: ").strip().split()))
print("")
result = unique(arr)
print("Unique Values: " + str(result))
print("Total Number of Unique Values: " + str(len(result)))