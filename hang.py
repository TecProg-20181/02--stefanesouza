import random
import string

WORDLIST_FILENAME = "palavras.txt"
GUESSES = 8

def loadWords():
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    return wordlist

def randomWords(wordlist):
    secretWord = random.choice(wordlist).lower()
    return secretWord

def inicialMessage():
    print "Loading word list from file..."
    filelist = loadWords()
    print "  ", len(filelist), "words loaded."


def isWordGuessed(secretWord, lettersGuessed):
    secretLetters = []

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def getGuessedWord(secretWord, lettersGuessed):
     guessed = ''

     for letter in secretWord:
         if letter in lettersGuessed:
             guessed += letter
         else:
             guessed += '_ '

     return guessed

def getAvailableLetters():
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase


    return available

def welcome_game(secretWord):
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'

def hangman():
    wordlist = loadWords()
    secretWord = randomWords(wordlist)

    guesses = 8
    lettersGuessed = []

    welcome = welcome_game(secretWord)

    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
        print 'You have ', guesses, 'guesses left.'

        available = getAvailableLetters()
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in lettersGuessed:

            guessed = getGuessedWord(secretWord, lettersGuessed)

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = getGuessedWord(secretWord, lettersGuessed)


            print 'Good Guess: ', guessed
        else:
            guesses -=1
            lettersGuessed.append(letter)

            guessed = getGuessedWord(secretWord, lettersGuessed)


            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'


hangman()
