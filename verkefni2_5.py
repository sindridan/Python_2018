#verkefni2_5
import datetime

#check if date is valid with datetime
def check_birthdate(kt):

    day = int(kt[0:2])
    month = int(kt[2:4])
    year = 0
    if int(kt[9]) == 9:
        year = '19' + kt[4:6]
    if int(kt[9]) == 0:
        year = '20' + kt[4:6]
    year = int(year)
    try:
        datetime.datetime(year, month, day) #verifies if datetime is valid
    except ValueError:
        return False
    else:
        return True

#check_birthdate('0212862149')

def check_checksum(kt):
    #D1 D2 M1 M2 Y1 Y2 R1 R2 C M
    #C = 11 - ((3xD1 + 2xD2 + 7xM1 + 6xM2 + 5xY1 + 4xY2 + 3xR1 + 2xR2) mod 11)
    get_checksum = 11-((3*int(kt[0]) + 2*int(kt[1]) + 7*int(kt[2]) + 6*int(kt[3]) + 5*int(kt[4]) + 4*int(kt[5]) + 3*int(kt[6]) + 2*int(kt[7]))%11)
    if get_checksum == int(kt[8]):
        return True
    return False

#check_checksum('0212862149')

def check_random(kt):
    rndom = int(kt[6:8])
    if rndom >=20 and rndom < 100:
        return True
    return False

#check_random('0212862149')

#if final digit corresponds to the right 
def check_last_digit(kt):
    if int(kt[9]) ==  0 or int(kt[9]) == 9:
        return True
    return False
#check_last_digit('0212862149')

def valid(kt):
    if check_birthdate(kt) and check_checksum(kt) and check_random(kt) and check_last_digit(kt):
        return True
    return False
    
valid('0212862149')
valid('1803442379')