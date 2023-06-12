# A BMI calculator console system using 3 different functions and main
# BMI - Means Body Mass Index

# function for getting weight and height
def get_info():
    weight = int(input("Enter weight [pounds]: "))
    height = int(input("Enter height [inches]: "))
    print("")
    return weight, height

# function for calculating bmi based on weight and height
def _bmi_cal(weight, height):
    bmi = 703 * weight / (height ** 2)
    return bmi

# function for displaying bmi
def show_bmi(bmi):
    print("Your bmi is ", bmi)
    print("")

# main function for invoking all the other functions
def main():
    w, h = get_info()
    bmi = _bmi_cal(w, h)
    show_bmi(bmi)

# calling the main function
main()