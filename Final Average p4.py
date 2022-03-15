def calculate(q1, q2, q3, q4, e1, e2):
    #you need to correct the line below to calculate the weighted average
    average = q1 + q2 + q3 + q4 + e1 + e2
    print("Your average is ", average)

def get_grades():
    #Finish getting user input for all the grades
    grade_q1 = int(input("Please enter your Quarter 1 grade : "))

    #plug in user input for the parameters below
    calculate(grade_q1, 100, 100, 100, 100, 100)

user_input = ""
while user_input != "stop":
    get_grades()
    user_input = input("Would you like to continue? Type stop to quit.")
