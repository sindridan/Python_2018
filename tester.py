#verkefni2_12
import re
from fractions import Fraction
def scale(s, ratio):
    get_numerals = re.findall(r"([0-9]?[r\/]*[0-9])", s)
    calculated = []
    for val in get_numerals:
        val = val + '*' + ratio
        val = eval(val)
        calculated.append(str(Fraction(val).limit_denominator()))

    #split_string = s.split()
    #print(split_string)
    #split_string = ' '.join(split_string)
    #print(split_string)
    print(calculated)
    
    formatted = re.sub(r"([0-9]?[r\/]*[0-9])", lambda match: calculated.pop(0), s)
    print(formatted)


scale('''Ingredients

    4 skinless, boneless chicken thighs
    1/2 cup soy sauce
    1/2 cup ketchup
    1/3 cup honey
    3 cloves garlic, minced
    1 teaspoon dried basil''', '1/2')