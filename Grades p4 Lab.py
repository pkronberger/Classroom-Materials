def calculate(q1, q2, q3, q4, e1, e2):
    final_average = q1+q2+q3+q4+e1+e2
    print("Your final average is", final_average)

def get_grades():
    q1 = int(input("What is your Quarter 1 Average? : "))
    calculate(q1,100,100,100,100,100)

user_input = ""

while user_input != "stop":
    get_grades()
    user_input = input("Do you want to continue? Type stop to quit.")
