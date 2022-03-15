def calculate(q1, q2, q3, q4, e1, e2):
    #Fix this line below so it calculates correctly
    final_average = q1 + q2 + q3 + q4 + e1 + e2
    print("Your final average is",final_average)

def get_grades():
    #add to the lines below to get all the needed grades from the user
    q1 = int(input("Please type in your quarter 1 grade : "))

    #Fix the line below so that it uses the input from the user
    calculate(q1,100,100,100,100,100)

user_input = ""

while user_input != "stop":
    get_grades()
    user_input = input("Do you want to continue? Enter stop to quit.")
