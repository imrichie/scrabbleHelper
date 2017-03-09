from scrabbleGame import ScrabbleDictionary

# Create the main function
def main():
    scrabblerObject = ScrabbleDictionary()
    choice = "none"
    while choice.lower() != "q":
        print()
        print("Welcome to Scrabbler Helper! ")
        print("Please enter a choice: ")
        print("\t1 -> Get Two Letter Words")
        print("\t2 -> Letters 'X' or 'Z'")
        print("\t3 -> Words that start with a 'Q' but are not followed by a 'u'")
        print("\t4 -> Word Verifier")
        print("\t5 -> All the 3-letter words from input")
        print("\t6 -> Display the point values")
        print("\t7 -> Words that begin with certain letter")
        print("\t8 -> Words that end with certain letter ")
        print("\tQ -> Quit\n")
        choice = input("Please make a selection: ")
        if choice == "1":
            print("The following are 2 letter words:\n\t",
                  scrabblerObject.getTwoLetterWords())

        elif choice == "2":
            enterLetter = input("Enter a letter(s): ")
            print("The following are words containing '"+ enterLetter +"' and X or Z:\n\t",
                  scrabblerObject.allXOrZWords(enterLetter))

        elif choice == "3":
            print("The following are words that start with "
                  "a 'Q' but not followed by a 'u'\n\t",scrabblerObject.getQWords())

        elif choice == "4":
            verifyWord = input("Choose a word to verify: ")
            scrabblerObject.wordVerifier(verifyWord)

        elif choice == "5":
            threeLetters = input("Enter a letter(s) ")
            print("The following are three letter words containing '" + threeLetters + "'\n\t",
                  scrabblerObject.threeLetterWords(threeLetters))

        elif choice == "6":
            wordValue = input("Enter a word for value: ")
            print("The value of '"+ wordValue +"' is:",scrabblerObject.wordPoints(wordValue))

        elif choice == "7":
            userInput7 = input("Enter a letter: ")
            print("The following are words that begin with '"+ userInput7 + "':\n\t",
            scrabblerObject.initialLetters(userInput7))

        elif choice == "8":
            userInput8 = input("Enter a letter: ")
            print("The following are words that end with '"+ userInput8 + "':\n\t",
            scrabblerObject.endingLetters(userInput8))

        else:
            break
    print("Thank You for playing. Goodbye!")

# Call Main
main()