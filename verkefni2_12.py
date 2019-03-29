#verkefni2_12
import re
from fractions import Fraction
def scale(s, ratio):
    get_numerals = re.findall(r"((\d\s)?[\d]\/?[\d]+|[\d])", s)
    calculated = []
    for val in get_numerals:
        val = re.sub(r"\s", '+', val[0])
        val = '(' + val + ')' 
        val = val + '*' + ratio
        val = eval(val)
        calculated.append(str(Fraction(val).limit_denominator()))

    check_denom = []
    for frac in calculated:
        check_denom.append(frac.split('/'))

    print(check_denom)
    for x in check_denom:
        if len(x) > 1:
            if int(x[0]) > int(x[1]): #check if numerator is bigger than denominator
                numerator = int(x[0])
                denominator = int(x[1])

                whole = numerator // denominator #need to fix bad fractions where num is bigger than nominator.
                fract = numerator % denominator
                x[0] = str(whole)
                if x[0] == 0:
                    x[0] = None
                x[1] = str(fract) + '/' + str(denominator)

    fix_lists = []
    for x in check_denom:
        if len(x) == 1 and ' ' not in x: #if it's a single digit without fraction
            fix_lists.append(''.join(x))
        else:
            if '/' in x[1]: #if it has a fraction but hasn't been split up, e.g. 1 1/2
                fix_lists.append(' '.join(x))
            else:
                fix_lists.append('/'.join(x)) #standard fraction

    #print(fix_lists)
    s = re.sub(r"((\d\s)?[\d]\/?[\d]+|[\d])", lambda match: fix_lists.pop(0), s) #swap out values in text
    s = re.sub(r"(\s0\s)", " ", s) #remove unnecessary 0's that might appear before fractions
    print(s)
    return s

scale('Irish Cream Chocolate Cheesecake\n\nRecipe By:Elaine\n"If you like Irish cream and chocolate, you\'ll love this recipe. After numerous attempts with the ingredients this is the recipe I now use."\nIngredients\n\n    1 1/2 cups chocolate cookie crumbs\n    1/3 cup confectioners\' sugar\n    1/3 cup unsweetened cocoa powder\n    1/4 cup butter\n    3 packages cream cheese, softened\n    1 1/4 cups white sugar\n    1/4 cup unsweetened cocoa powder\n    3 tablespoons all-purpose flour\n    3 eggs\n    1/2 cup sour cream\n    1/4 cup Irish cream liqueur\n', '3')