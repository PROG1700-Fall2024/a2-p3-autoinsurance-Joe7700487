#Program 3 – Auto Insurance
#Write a program that computes monthly insurance according to the provided schedule. 

#Student #:     0500154
#Student Name:  Joseph Petrash

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # init variables
    gender = input("Are you Male or Female: ").lower()
    age = int(input("Enter your age: "))
    price = float(input("Enter the purchase price of the vehicle: "))
    insurance = 0

    # if gender is male calculate insurance based on the age range
    if (gender == "male"):
        if (age >= 15 and age < 25):
            insurance = price * 0.25 / 12
        elif (age >= 25 and age < 40):
            insurance = price * 0.17 / 12
        elif (age >= 40 and age < 70):
            insurance = price * 0.10 / 12
        else:
            print("Invalid age")
    # if gender is female calculate insurance based on the age range
    elif (gender == "female"):
        if (age >= 15 and age < 25):
            insurance = price * 0.20 / 12
        elif (age >= 25 and age < 40):
            insurance = price * 0.15 / 12
        elif (age >= 40 and age < 70):
            insurance = price * 0.10 / 12
        else:
            print("Invalid age")
    # if neither print invalid
    else:
        print("Invalid gender")
    
    # display monthly insurance
    print("Your monthly insurance will be ${0:.2f}".format(insurance))
    # YOUR CODE ENDS HERE
main()