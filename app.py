import functions


def hangman(secretWord):
    print("Welcome to the game Hangman!")
    secretWord = secretWord.lower()

    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-----------")
    lettersGuessed = ""
    lettersUsed = []

    numguesses = 8

    while not functions.isWordGuessed(secretWord, lettersGuessed) and numguesses != 0:
        print("You have " + str(numguesses) + " guesses left.")
        print("Available letters: " + functions.getAvailableLetters(lettersGuessed))
        letter = input("Please guess a letter(or guess the word): ")

        if len(letter)>=2:
            if letter == secretWord:
                print ("Good guess. You have won the game!")
            else:
                print("Oops. Not the right word!")
                numguesses -= 1

        if letter in lettersUsed:
            print("Oops! You've already guessed that letter: " + str(functions.getGuessedWord(secretWord, lettersUsed)))
            print("-------------")
        elif secretWord.find(letter) != -1:
            lettersGuessed += letter
            lettersUsed.append(letter)
            print("Good guess: " + str(functions.getGuessedWord(secretWord, lettersUsed)))
            print("-------------")
        elif numguesses == 0:
            break


        else:
            numguesses -= 1
            print("Oops! That letter is not in my word: " + str(functions.getGuessedWord(secretWord, lettersUsed)))
            print("-------------")
            lettersGuessed += letter
            lettersUsed.append(letter)

    if functions.isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!:")
    elif functions.isWordGuessed(secretWord, lettersGuessed) == False or numguesses == 0:
        print("Sorry, you ran out of guesses. The word was " + secretWord + ".")


hangman(functions.chooseWord(functions.loadWords()))
