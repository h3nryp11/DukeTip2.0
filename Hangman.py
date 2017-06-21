
import numpy


my_list = ["office", "Boss", "Michael", "Jim", "Pam", "Dwight", "Kevin", "Ryan", "Phyllis", "Stanely", "DunderMifflin",
           "Scranton"]

spaces=len(my_list)
print(my_list)


def printhangman(numberwrong):

    print("|-----|")
    if numberwrong>=1:
       print('  |     0')
    else:
        print("  |")
    if numberwrong >=2:
        print("  |     |")

    else:
        print("  |")
    if numberwrong>=3:
        print("  |    [|]")
    else:
        print("  |")
    if numberwrong>=4:
        print("  |     |")
    else:
        print("  |")
    if numberwrong==5:
        print("  |    !!")
    else:
        print("  |"
              "__________")

def printBlanks(word, correctLetters):
    solved = True
    for l in word:
        l = l.lower()

        if l in correctLetters:
            print l + " ",
        else:
            print "_ " ,
            solved = False
    print "";
    print "";
    return solved




correct_letters=[]

incorrect_guesses=0


word= numpy.random.choice(my_list)

while True:

    printhangman(incorrect_guesses)

    solved = printBlanks(word,correct_letters)

    if incorrect_guesses>=5:
        break;

    if solved:
        print('Winner!')
        break;

    letter = ""
    # Loop until they give a letter
    while letter == "":
        letter = raw_input("Input your guess: ")
    letter = letter[0].lower()
    # Check if the letter is in the word
    if letter in word.lower():
        print("Good Guess")
        correct_letters.append(letter)
    else:
        print("Nice Try");
        incorrect_guesses = incorrect_guesses + 1

print (word)





