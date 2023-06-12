second_try = []

def taker():
    i = input("Enter the number (it comes one at a time): ")
    second_try.append(i)
    

limit = int(input("Enter the limit: "))
for item in range(0, limit):
    taker()

print(second_try)
