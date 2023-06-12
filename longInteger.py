"""
Given an array of integers, where all the elements but one occur twice,
fine the unique element.

Eg: a = [1, 2, 3, 4, 3, 2, 1]
The unique element is 4
"""

# function for checking for the unique value
def lonelyInteger(a, n):
    a.sort()
    ans=0
    for i in range(n):
        ans=ans^a[i]
    return ans



# first take input from user
n = int(input("Enter the size of the list: ").strip())
a = list(map(int, input("Enter the values separating them with space: ").strip().split()))

result = lonelyInteger(a, n)
print(result)


"""
Ulternative

    sum_of_a = sum(a)
    set_sum_of_a = sum(set(a))
    res = (2 * set_sum_of_a) - sum_of_a
"""