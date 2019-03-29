#verkefni2_3, eval(x)
#all possible combinations with operators
#gera öll mismunandi combinations
#eval(x) og fá út gefna töluna
import itertools
def insert_operators(seq, target):

    try:
        for op in itertools.product(('+','-',''), repeat=(len(seq)-1)): #creates different combinations of the three operators
            #cant insert any operator before the first char in seq and none after the last
            #zip together the operators with the following digits in seq
            #has to keep the order of digits in sequence, the '' operator splashes together digits in the seq
            #zip(op,seq[1:]) combines the operators with one or more digits from seq
            #tests every combination until eval has discovered the output value matching the target
            lis = str(seq[0]) + ''.join(op + str(val) for op, val in zip(op,seq[1:]))
            if eval(lis) == target:
                return lis + '=' + str(target)
    except:
        return None


insert_operators([14,8,2,17,5,9],83)
insert_operators([34,9,82,21,32],32850)
insert_operators([1,2,3],5)
