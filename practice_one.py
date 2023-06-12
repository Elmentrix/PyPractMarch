"""
Q1. A code to to take a collection of input from a user, seperate it and store into a list. The code is to
check through the given list and check for the total number of positive number, negative numbers, and
zeros. find the ratio of the positves, negative and zeroes against the total number of items in the main
list. Display the results in 2 decimal places.
"""

"""
Q2. Develope a a form webpage to take inputs from students and a tabble to display the information.
All on the same webpage. Namely:

Biography form - name, age, email, contact, city and address
Purchase form - name of item, number of item bought, amount per unit and total amount.

Table - It should display the information of all the inputs that would be taken by the
form. For now use hard typed data.
"""

# Solving the above question.
positive_numbers = []
negative_numbers = []
zeros = []


def checker(pos, neg, zero, all_):
    print("Entire list: ", all_)
    print("The total number of items in the list: ", len(all_))
    print("")
    print("Positive list: ", pos)
    print("The total number of items in the positive list: ", len(pos))
    print("Ratio of positves to total: ", len(pos)/len(all_))
    print("")
    print("Negative list: ", neg)
    print("The total number of items in the negative list: ", len(neg))
    print("Ratio of negatives to total: ", len(neg)/len(all_))
    print("")
    print("Zero list: ", zero)
    print("The total number of items in the zero list: ", len(zero))
    print("Ratio of zeroes to total: ", len(zero)/len(all_))
    print("")

# taking input from user and storing into a list in the process
print("Please enter the numbers seperating them with a comma")
print("")
drag = input("Enter the numbers to check: ").split(",")
print(drag)
for item in drag:
    i = int(item)
    if i > 0: 
        positive_numbers.append(i)
    elif i < 0: 
        negative_numbers.append(i)
    else:
        zeros.append(i)
  

checker(positive_numbers, negative_numbers, zeros, drag)