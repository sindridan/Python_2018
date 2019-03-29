#sorp
#liður 8:
import re #regex
def birthdays(s):
    #splitList = []
    #splitList = list(re.findall('..........', s)) #slice for every 10th char
    newList = []
    s = s.split('\n')
    for x in s:
        if s.count(x[0:3]) > 1:
                newList.append(x)
    #if any(entry[0:1] in entry for entry in splitList):
        #newList.append(entry)
    return newList

birthdays('''0212862149
0407792319
0212849289
1112792819
0407992939
0212970299''')

def duplicates(s):
    dup = []
    for x in s:
        if s.count(x) > 1:
            dup.append(x)
    return list(set(dup))

#liður 3:
def flatten(lis):
    """indices = list(range(0, len(lis)))"""
    sortLis = list(sorted(lis))

    m = {}
    for index, value in enumerate(sortLis): 
        m[value] = index 

    returnList = []
    for value in lis: 
        returnList.append(m[value])
    """zippedSorted = list(zip(sortLis, indices))
    newList = []
    for x in lis:
        for y in zippedSorted:
            if x == y[0]:
                newList.append(y[1])"""
    return returnList

flatten([984, 523, 653, 503, 557, 170, 336, 552, 511, 768, 184, 565, 564, 133, 277, 966, 37, 427, 351, 62, 500, 131, 160, 12, 304, 972, 725, 14, 46, 346, 820, 671, 24, 726, 300],)


    #fswp = list(filter(None, re.split(r'\s{2,}', x)) for x in splits) #filter single white spaces in list
    #returnList = []
    #for line in splits
    #fswp = re.split('\s{2,}|\n', s) #filter single white spaces in list
    
    
    
    #return sorted(fswp, key=lambda s: s.casefold())
    #newFSWP = list([y for x in fswp for y in x.split(' ')])
    #maps = list(map(str.strip, fswp))
    #formatList = list(filter(None, re.split(r'\s', item)) for item in zip_longest(*fswp))
    #unsorted = []
    #for item in fswp:
    #    for subItem in item:
    #        unsorted.append(subItem)
    #retList = list(sorted(unsorted, key=lambda s: s.casefold()))
    #retList = unsorted


import itertools
itertools.product([1, 2], ['a','b'])
list(_)



ld = [0, 3 , 5]
lk = [2, 6, 7, 9, 10]

pt = list(zip(ld,lk))

print(pt)

    """ranks = '23456789TJQKA'
    print(ranks)
    suits = 'HSDC'
    deck = list(itertools.product(suits, ranks))
    """

re.findall í minute

import string
str1 = 'very good'
str2 = 'notGood'
if str1.isspace() == True:
    print('yes space')
if str2.isspace():
    print('nospace')