"""

    Ask your friend for an initial word
    Repeatedly ask them for an index and a letter
        You should replace the letter at the index they provided with the letter they enter
        You should then print the new word
    Stop asking for input when the user enters -1 for the index

Here’s what should be happening behind the scenes:

    You should have a function, get_index, that repeatedly asks the user for an index until they enter a valid integer that is within the acceptable range of indices for the initial string. (If they enter a number out of range, you should reply invalid index.)
    You should have another function, get_letter, that repeatedly asks the user for a letter until they enter exactly one lowercase letter. (If they enter more than one character, you should reply Must be exactly one character!. If they enter a capital letter, you should reply Character must be a lowercase letter!.)
    You should store a list version of the current word in a variable. This is what you should update each time the user swaps out a new letter.
    Each time you have to print the current word, print the string version of the list you are keeping in your variable.
1. Ask for an initial word
2. Write a function get_index that asks for a user index until a valid index is typed in
    a. If the index is invalid, print "Invalid index" and call the function again
    b. If the index is valid, return the entered index
3. Write a function get_letter that asks for a letter until a valid letter is entered
    a. If the letter is invalid, print "Invalid letter" and call the function again
    b. If the letter is valid, return the entered letter
4. Inside a while loop, call the functions from 2 and 3 until the user enters
5. "Listify" the entered string. Use the results of get_letter and get_index to update your list.
6. Stringify your modified word and print it.
"""
def get_index(length):
    index = int(input("Enter an index (type -1 to quit): "))
    if index == -1:
        return -1
    elif index < 0 or index >= length:
        print ("Please enter a valid index.")
        get_index(length)
    else:
        return index

def get_letter():
    letter = input("Enter a letter: ")
    if len(letter) != 1 or letter.isupper():
        print ("Please enter a lowercase letter.")
        get_letter()
    else:
        return letter

word = input("Enter a word : ")
index = get_index(len(word))
if index != -1:
    letter = get_letter()
while index != -1:
    word = list(word)
    word[index] = letter
    word = "".join(word)
    print (word)
    index = get_index(len(word))
    if index != -1:
        letter = get_letter()
    
