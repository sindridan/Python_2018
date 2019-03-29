#verkefni2_9

import re
import datetime

def jam(data): 

	newLineSplit = data.split('\n')
	allNames = []
	for line in newLineSplit:
		commaSplit = line.split(',')
		for index in range(1, len(commaSplit) - 1): #names never appears first in the string neither last
			names = re.split(' and | with ', commaSplit[index]) #delimiters that indicate names inbetween
			for name in names:
				name = name.replace('plus ','') #some names come aftur 'plus '
				name = name.strip()
				allNames.append(name)
	
	s = set()
	m = {}
	for name in sorted(allNames):
		if name in s:
			m[name] += 1
		else:
			m[name] = 1
			s.add(name)
	#print(m)
	return m


jam("""1/1/1 22 December 1967, Nicholas Parsons with Derek Nimmo, Clement Freud, Wilma Ewart and Beryl Reid, excuses for being late.
	2/1/2 29 December 1967, Nicholas Parsons with Derek Nimmo, Clement Freud, Sheila Hancock and Carol Binstead, bedrooms.
	3/1/3 5 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Betty Marsden and Elisabeth Beresford, ?
	4/1/4 12 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Isobel Barnett and Bettine Le Beau, ?
	5/1/5 20 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Andree Melly and Prunella Scales, the brownies
	6/1/6 27 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Marjorie Proops and Millie Small, ?
	7/1/7 2 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Aimi Macdonald and Una Stubbs,plus Agnes, my honeymoon.
	8/1/8 9 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Lucy Bartlett and Anona Winn, bloomer.
	9/1/9 17 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Andree Melly and Charmian Innes, ?
	10/1/10 23 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Barbara Blake and Renee Houston, my first grown-up dress.""")