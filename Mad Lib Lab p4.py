def fill_blanks():
    #Add more lines here to fill in all the blanks you need
    noun = input("Put a noun here, sir or madam : ")
    while is_bad(noun):
        noun = input("Put a noun here, sir or madam : ")
    #call story_time on the line below
    story_time(noun)
    
def story_time(noun):
    print("I like to eat",noun,end=". ")
    print("this should be on the same line")

def is_bad(word):
    if (word == "heck"
        or word == "Heck"
        or word == "HECK"):
        print("Sowwy das a bad word. Please enter something appropriate.")
        return True
    elif word == "stupid":
        print("Sowwy das a bad word. Please enter something appropriate.")
        return True
    elif word == "":
        print("Put something in the blank. Blanks can't be blank!")
        return True
    else:
        return False

fill_blanks()



















