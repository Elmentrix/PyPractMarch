# Finding the difference of the maximum and minimum number in an array to the total sum of the array

# function to take inputs from user passed as an argument and work on
def minMaxSum(arr):
    arr.sort()
    # minSum_ = sum(arr[:4])
    # maxSum_ = sum(arr[-4:])

    # print(minSum_, " ", maxSum_)
    s = sum(arr)

    print("\n" + "Total Sum of the Input: " + str(s))
    print("The minimum difference with the total sum is " + str(s-min(arr)))
    print("The maximum difference with the total sum is " + str(s - max(arr)) + "\n")

arr = list(map(int, input("Enter a list of number separating with a space: ").rstrip().split()))
minMaxSum(arr)

# correct