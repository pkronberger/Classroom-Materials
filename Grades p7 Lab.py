def calculate(q1, q2, q3, q4, e1, e2):
    #Fix the line below by using WEIGHTED AVERAGES (quarter is 20%, exam 10%)
    final_average = q1 + q2 + q3 + q4 + e1 + e2
    print("The final average is", final_average)

def get_grades():
    #Add more lines of code to collect and store all the grades
    q1 = int(input("Please enter your quarter 1 grade : "))

    #replace the 100s with the names of the grades q1, q2, etc
    calculate(q1,100,100,100,100,100)

please_stop = ""
while please_stop != "stop":
    get_grades()
    please_stop = input("Do you want to calculate again? Type stop to end the program.")
