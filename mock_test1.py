# median of a list taken the size as well

# function for median
def Median_Function(list_set):
    print("Input Data: " + str(list_set))
    # first take the list size and sort the list in ascending order
    n = len(list_set)
    list_set.sort()
    print("Sorted Data: " + str(list_set))

    # control the flow for even or odd data set
    if n % 2 == 0:
        # working out the median when the data set is even
        second_num = n/2
        first_num = second_num - 1

        median_ = (list_set[int(first_num)] + list_set[int(second_num)])/2
        print("Median: " + str(median_))
    else:
        # working out the median when the data set is odd
        median_ = int(((n + 1)/2) - 1)
        print("Median: ", str(list_set[median_]) + "\n")

# taking inputs from user
list_set = list(map(int, input("Enter the values of the list separating by a space: ").strip().split()))
Median_Function(list_set)