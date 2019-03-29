#verkefni2_4
import string
import re
def hangman(filename, state, guessed):

    words = []
    file = open(filename)
    for line in file:
        line = line.strip()
        if len(line):
            if line.isalpha() and len(line) == len(state):
                words.append(line)

    getAlpha = string.ascii_lowercase #all the available chars must be lowercase
    available = []
    for x in getAlpha:
        if x not in guessed:
            available.append(x)
    available = ''.join(available) #all the chars in alphabet that havent been guessed 

    leftovers = "[" + available + "]"
    regex = ''
    #regex fullmatch for all possible combinations on '-' to available alpha
    for char in state:
        if char == '-':
            regex = regex + str((leftovers)) #swap out the - for a regex input
        else:
            regex = regex + str(char)
    matches = []
    for word in words:
        if re.fullmatch(regex, word):
            matches.append(word)
    return list(set(matches))

#hangman('all_words.txt', '-e-a-a--a--', 'ae')
