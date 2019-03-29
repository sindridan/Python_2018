#verkefni2_2, gera set úr permutations af orðinu og set af öllum orðunum, nota síðan intersection!
import itertools
def countdown(filename, input):
    words = []
    file = open(filename)
    for line in file:
        line = line.strip()
        if len(line):
            words.append(line)
    file.close()
    filtered_words = []
    for word in words:
        if len(word) > 3: #only get words that are longer than 4
            filtered_words.append(word)
    permutate = []
    i = len(input)
    while i >= 4: #create variations of the same input with decrementing size
        for word in itertools.permutations(input, r = i):
           permutate.append(''.join(word))
        i = i-1
    
    permutate = set(permutate) #remove duplicates
    filtered_words = set(filtered_words) #same

    matches = filtered_words.intersection(permutate) #get only words that are same in both lists
    return sorted(matches)
#countdown('words.txt', 'pythonxyz')

