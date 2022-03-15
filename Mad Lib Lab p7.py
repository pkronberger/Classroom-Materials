def fill_blanks():
    #add more lines of code below to take in AT LEAST 5 different values
    noun = input("Type in a noun : ")
    while is_bad(noun):
        noun = input("Type in a noun : ")

    adjective = input("Type in a adjective : ")
    while is_bad(adjective):
        adjective = input("Type in a adjective : ")
        
    #update the parameters so that all input is passed on
    story_time(noun, adjective)

#update the parameters so that all input is passed on
def story_time(noun, adjective):
    print("Once there was a", noun, end = ". ")
    print("The", noun, "was", adjective, end = ".")

def is_bad(word):
    if word == "heck" or word == "HECK":
        print("That's a bad word.")
        return True
    elif word == "stupid" or word == "Stupid" or word == "STUPID":
        print("That's a bad word.")
        return True
    elif word == "":
        print("Bad choice. Say something.")
        return True
    else:
        return False


fill_blanks()


















