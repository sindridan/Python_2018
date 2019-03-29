#liður 1:
#break input into indices where the line breaks
#append into new sortedlist
#sort the list

def cdo(input):
    sorts = input.split(" ") #seperates each word in string by spaces and lists them
    sorts.sort()
    newstr = " ".join(sorts) #create a unified string and form a space between every word
    return newstr
 
cdo('in theory there is no difference between theory and practice')

#liður 2:
def duplicates(s):
    dup = []
    found = {} #used for comparing seen duplicate elements

    for x in s:
        if x not in found:
            found[x] = True #if the element hasn't been seen before in input list
        else:
            if found[x] == True: #after comparison, if element has been seen in found, add it to the duplicate list
                dup.append(x)
    return list(set(dup)) #cleans out duplicates from the list
duplicates([1337, 42, 5318008, 1337, 5318008, 5885522])
duplicates([1337, 1337, 42, 42, 42, 5318008, 1337, 5318008, 5885522, 42])

#liður 3:
def flatten(lis):
    sortLis = list(sorted(lis))

    m = {} 
    for index, value in enumerate(sortLis): #create enumerated list [(0,4), (1,6), (2,8)]
        m[value] = index #map the indexes to the values

    returnList = []
    for value in lis: 
        returnList.append(m[value]) #use the map to access the index associated with the value and add it to the returning list

    return returnList

flatten([984, 523, 653, 503, 557, 170, 336, 552, 511, 768, 184, 565, 564, 133, 277, 966, 37, 427, 351, 62, 500, 131, 160, 12, 304, 972, 725, 14, 46, 346, 820, 671, 24, 726, 300],)

#liður 4:
def rm_duplicates(lis):
    s = set(lis) #removes duplicates because of set
    newList = list(s) #convert back to list
    return sorted(newList)

rm_duplicates([18, 7, 1, 15, 15, 1, 19])

#liður 5:
#zip indexes 1 to n-1 for L

def scramble(original, keys):
    indices = list(range(0, len(original))) #create index list 
    originalMatched = list(zip(original, indices)) #no sorting, map original to indexes 0 to n-1
    newList = []

    for x in keys: #iterate through keys, comparing them with originalmatched to find match, then append in keys order
        for y in originalMatched:
            if x == y[1]: #if index in originalmatched matches the key, append value to newlist
                newList.append(y[0])
    return newList

scramble([100, 42, 4, 1337], [1,3,2,0])

#liður 6:
import math
def excel_index(s):
    chars = []
    for x in s:
        charval = ord(x) - 64 #find ascii val, take away 64 to get A = 1
        chars.append(charval)
    totalVal = 0
    i = 0
    for i in range(len(chars)):
        exp = math.pow(26, len(chars) - (i+1)) #get the correct power for the amount of chars in input, if AA, then power is 26^1 because we've exceeded the complete first list, else 26^0 if only single char in input
        totalVal = (totalVal + exp * chars[i])
    return int(totalVal) #comes originally out as a float

excel_index('CA')
excel_index('AA')
excel_index('LOL')
 
#liður 8:
import re #regex
def birthdays(s):
    s = s.split('\n') #splits the input on newlines
    birthdays = []
    for x in s:
        birthdays.append(x[0:4]) #list containing first four letters, indicating birthdays
        
    finalList = []
    for day in duplicates(birthdays): #reusing duplicates function, filters out kennitalas with same birthdate: only checking where there is more than one same birthdate
        kt = tuple(filter(lambda x : day == x[:4] , s)) #tuples together those with the same birthdate (first four digits) as the 'day' variable. 
        finalList.append(kt)
    
    return finalList
            
birthdays('''0212862149
0407792319
0212849289
1112792819
0407992939
0212970299''')

import re
def process_ls(s):
    lines = s.splitlines() #removes newlines from the input
    l = []
    for line in lines:
        l.append(list(re.split(r'\s{2,}', line))) #regex split, only splits where there is more than 2 whitespaces between words
    retList = [] 
    for j in range(len(l[0])): #starts at first list index
        for i in range(len(l)):
            if(len(l[0]) > len(l[i]) and j == len(l[0]) - 1): #to avoid index out of bounds
                return retList
            retList.append(l[i][j]) #2d array iterate, appending in a vertical order
    return retList

process_ls("""ac pid.pid     console-kit-daemon.pid  lock        pm-utils      sdp                      upstart-socket-bridge.pid
acpid.socket  crond.pid               mdm.pid     postgresql    sendsigs.omit.d          upstart-udev-bridge.pid
apache2       crond.reboot            mdm_socket  pppconfig     shm                      user
apache2.pid   cups                    motd        resolvconf    udev                     utmp
avahi-daemon  dbus                    mount       rsyslogd.pid  udisks                   wicd
console       dhclient.pid            network     samba         udisks2                  wpa_supplicant
ConsoleKit    initramfs               plymouth    screen        upstart-file-bridge.pid""",)
