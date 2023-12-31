# Python program to convert time from 12 hour to 24 hour format

# Function to convert the date format
def convert24(str1):
	
	# Checking if last two elements of time
	# is AM and first two elements are 12
	if str1[-2:] == "AM" and str1[:2] == "12":
		return "00" + str1[2:-2]
		
	# remove the AM	
	elif str1[-2:] == "AM":
		return str1[:-2]
	
	# Checking if last two elements of time is PM and first two elements are 12
	elif str1[-2:] == "PM" and str1[:2] == "12":
		return str1[:-2]
		
	else:
		# add 12 to hours and remove PM
		return str(int(str1[:2]) + 12) + str1[2:5]

# first take an input 
time_in = input("Enter the time: ").upper().replace(" ", "").strip()
print("\n" + "12 hours time: " + time_in)
print("24 hours time: " + convert24(time_in) + "\n")

