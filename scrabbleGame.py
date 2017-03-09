from collections import defaultdict

# Create a class to manage the Scrabble dictionary
class ScrabbleDictionary(object):
    # constructor
    def __init__(self, fileName = "words.txt"):
        openFile = open(fileName, "r")

        # Scrabbler points
        self.__scrabblerPoints = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1,
                                  "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1,
                                  "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10, "Blank": 0}

    # Create dictionary of words grouped by length
        self.__wordLength = defaultdict(lambda: [])

        self.__words = {}

        for line in openFile:
            line = line.strip("\n")
            #if line not ""
            if line != " ":
                wordLength = len(line)

                self.__wordLength[wordLength].append(line)

                self.__words[line] = wordLength

        # close file
        openFile.close()

# !!!! Start of defining functions/features (8) !!!!

    # 1st Feature
    # Function that returns all two letter words from the dictionary
    def getTwoLetterWords(self):
        return self.__wordLength[2]

    # 2nd Feature
    # Ask user to enter a letter and then show all words containing
    # the letters “X” or “Z” and the input tile.
    def allXOrZWords(self, words):
        """
        # pass in 'words' as string tile
        :param words: string of length 1
        :return: list of strings
        """
        xOrZWords = []

        for word in self.__words.keys():
            if "x" in word.lower() or "z" in word.lower():
                if words in word:
                    xOrZWords.append(word)
        return xOrZWords

    # 3rd Feature
    #List all words that start with a “Q” but are not followed by a “u”.
    def getQWords(self):
        qWords = []
        for word in self.__words.keys():
            # error checking
            if self.__words[word] >= 2:
                if word[0].lower() == "q" and word[1].lower() != "u":
                    qWords.append(word)
        return qWords

    # 4th Feature
    # Word verifier: Ask user for input and then verify that it exists
    # within the Scrabble dictionary
    def wordVerifier(self, word):
        if word in self.__words.keys():
            print("Yes '" + word + "' is in the dictionary\n")
        else:
            print("No '"+ word + "' is not in the dictionary\n")

    # 5th Feature
    # Ask user for a letter and then show all the 3-letter words containing
    # that given input tile.
    def threeLetterWords(self, wordInput):
        threeWords = []
        for word in self.__wordLength[3]:
            if wordInput in word:
                threeWords.append(word)
        return threeWords

    # 6th Feature
    # Whenever you display possible words to the user, also display the point values.
    def wordPoints(self, word):
        points = 0
        for i in word:
            points += self.__scrabblerPoints[i.upper()]
        return points

    # 7th Feature
    # Ask user to enter one or more letters and then show all words that begin with that
    # group of letters.
    def initialLetters(self, begLetters):
        words = []
        for word in self.__words.keys():
            if word[0] in begLetters:
                words.append(word)
        return words

    # 8th Feature
    # Ask user to enter one or more letters and then show all words that end with that
    # group of letters.
    def endingLetters(self, endLetters):
        words = []
        for word in self.__words.keys():
            if word[-1] in endLetters:
                words.append(word)
        return words