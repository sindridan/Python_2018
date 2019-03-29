#k4
import re
def all_palindromes(txtfile):
    words = []
    file = open(txtfile)
    for line in file:
        line = line.strip()
        if len(line):
            words.append(line)
    file.close()

    palind = []
    #it = 0
    """for word in words:
        if word[it] == word[len(word) - 1]:
            if it == (len(word) - (it)):
                palind.append(word)
            it += 1"""
    for word in words:
        cleaned_word = re.sub("[ ']", "", word)
        #print(cleaned_word)
        rvrsd = cleaned_word[::-1] #reverses the string, starts reading it from -1 which is first char in reversed string order
        if rvrsd == cleaned_word:
            palind.append(cleaned_word)

    print(palind)
    return palind

all_palindromes('small_words.txt')