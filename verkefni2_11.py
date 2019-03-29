#verkefni2_11
def sort_names(lis):
    #whitespace included in alphabet because substring error returns when string has whitespace in it
    ice_alpha = "' 'aábcdðeéfghiíjklmnoópqrstuúvwxyýzþæö" 
    arr = []
    for name in lis:
        names = name.split(" ")
        if(len(names) > 2): #if there are names between first name and paternal name, they should be added behind paternal name
            name =  names[0] + " " + names [len(names) - 1]
            for index in range (1, len(names)-1):
                name = name + " " + names[index]
        arr.append(name)

    sorted_names = list(sorted(arr, key = lambda name: [ice_alpha.index(it.lower()) for it in name[0:]]))
    returnArr = []
    for name in sorted_names:
        names = name.split(" ")
        if(len(names) > 2): #recovering the middle names after paternal name and inserting them into correct position of name
            name = names[0]
            for index in range (2, len(names)):
                name = name + " " + names[index]
            name = name + " " + names[1]
        returnArr.append(name)
    return returnArr

sort_names(['Þórir Jakob Olgeirsson',
    'Quintin Tarantínó',
    'Winston Wortel',
    'Arnar Björn Pálsson',
    'eyþór snár tryggvason',
    'Eyþór Snær Tryggvason',
    'Eyþór Snær Helgi Tryggvason',
    'Arnar Jóhannsson',
    'Eyþór Traustason',
    'Arnar Bjarni Arnarson',
    'Þórhildur Þorleiksdóttir',
    'Sindri Dan Garðarsson',
    'Ægir Helgi Davíðsson'])

