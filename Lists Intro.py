from random import *
goodThings = ("That's pretty cool!",
              "How exciting!",
              "Tell me more about that!")
badThings = ("Yikes on bikes...",
             "I'm sorry to hear that",
             "How unfortunate.")
neutralThings = ("That's not the worst.",
                 "Sounds interesting.",
                 "Hmmmmm")
def getResponse(options):
    response = options[randrange(0, len(options))]
    print(response)

userReply = input("How are you doing?")
if "bad" in userReply:
    getResponse(badThings)
elif userReply == "good":
    getResponse(goodThings)
else:
    getResponse(neutralThings)
