import random
import string

WORDLIST_FILENAME = "palavras.txt"
GUESSES = 8

def load_words_list():
    in_file = open(WORDLIST_FILENAME, 'r', 0)
    line = in_file.readline()
    word_list = string.split(line)
    return word_list

def random_words(word_list):
    secret_word = random.choice(word_list).lower()
    return secret_word

def inicial_message():
    print "Loading word list from file..."
    filelist = load_words_list()
    print "  ", len(filelist), "words loaded."


def word_guessed(secret_word, letters_guessed):
    secretLetters = []

    for letter in secret_word:
        if letter in letters_guessed:
            pass
        else:
            return False

    return True

def get_guessed_word(secret_word, letters_guessed):
     guessed = ''

     for letter in secret_word:
         if letter in letters_guessed:
             guessed += letter
         else:
             guessed += '_ '

     return guessed

def get_available_letters():
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase


    return available


def welcome_game(secret_word):
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secret_word), ' letters long.'
    print '-------------'

def hangman():
    word_list = load_words_list()
    secret_word = random_words(word_list)

    guesses = 8
    letters_guessed = []

    welcome = welcome_game(secret_word)

    while  word_guessed(secret_word, letters_guessed) == False and guesses >0:
        print 'You have ', guesses, 'guesses left.'

        available = get_available_letters()
        for letter in available:
            if letter in letters_guessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in letters_guessed:

            guessed = get_guessed_word(secret_word, letters_guessed)

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secret_word:
            letters_guessed.append(letter)

            guessed = get_guessed_word(secret_word, letters_guessed)


            print 'Good Guess: ', guessed
        else:
            guesses -=1
            letters_guessed.append(letter)

            guessed = get_guessed_word(secret_word, letters_guessed)


            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        if word_guessed(secret_word, letters_guessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secret_word, '.'


hangman()
