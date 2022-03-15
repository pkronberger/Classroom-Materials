def fill_blanks():
    #create more lines asking for user input (AT LEAST 5 BLANKS)
    noun = input("Enter a noun : ")
    while is_bad(noun):
        noun = input("Enter a noun : ")
    #add parameters here as well for each blank
    story_time(noun)

#add a parameter for every blank
def story_time(noun):
    print("Once upon a time there was a", noun, end = ". ")

def is_bad(word):
    if (word == "heck" or word == "stupid" or word == "frick" or word == "Stupid"
        or word =="STUPID"):
        print("No hecks or fricks in my classroom minecraft server.")
        return True
    elif word == "":
        print("Please enter a word. I'm so lonely. It's dark in here.")
        return True
    else:
        return False

fill_blanks()



















