#project0

#liður 1:
def sum_two(a,b):
    return a + b

sum_two(5,7)

#liður 2:
def mod_sum(n):
    sums = 0
    for i in range(0, n):
        if i%3 == 0 and i%5 == 0:
            sums = i + sums
        elif i%3 == 0:
            sums = i + sums
        elif i%5 == 0:
            sums = i + sums
    return sums

mod_sum(15)

#liður 3:
def sum_no_3(intList):
    total = 0
    for element in intList:
        if element%10 != 3:
            total = total + element
    return total

sum_no_3([1, 13, 15, 1])

#liður 4:
def sum_first(lis, n):
    return sum(lis[0:n])
    
sum_first([1, 13, 15, 1], 1)
sum_first([1, 13, 15, 1], 4)

#liður 5:
def list_product(lis1, lis2):
    sum_of_ab = [a*b for a,b in zip(lis1, lis2)] #multiplies index i in first list with index j in second list, repeating for both lists
    return sum_of_ab

list_product([1, 13], [4, 2])
list_product([1, 13, 15, 1], [4, 3, 2, 1])
list_product([1], [1])

#liður 6:
def remove_empty(stringlis):
    stringlis = list(filter(None, stringlis)) #removes the empty spaces from the list
    return stringlis

remove_empty(['python', '', 'is', 'awesome', ''])

#liður 7:
def decrypt(encrypted):
    newstring = ''
    i = 0
    for char in encrypted:
        if(i%3 == 0):
            newstring = newstring + char #appends every third char into a new string
        i = i+1 
    return newstring

decrypt('AQltQptoAaQPcmokPY ToaFKtBe WEdvAagrwpknDJ!yX')

#liður 8
def gymnastics(records):
    if len(records) > 2:
        records.remove(max(records)) #finds max val and deletes from list
        records.remove(min(records)) #same with min val
    total = 0
    for i in records:
        total = i + total
    return int(total / len(records))

gymnastics([2, 13])
gymnastics([1, 13, 15, 2])

#liður 9
def boom(n):
    #lis = list(range(n))
    strlist = []
    i = 1
    while i <= n:
        if i%7 == 0 or '7' in str(i):
            strlist.append(str('boom!'))
        else:
            strlist.append(str(i)) #convert the values to string
        i+= 1
    return strlist
boom(0)
boom(20)
