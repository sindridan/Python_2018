#k1.py

def check_parant_count(parants):
    openCount = 0
    closeCount = 0

    for par in parants:
        if par == '(':
            openCount += 1
        else:
            closeCount +=1
    
    if openCount == closeCount:
        return True
    return False

def index_parant(parants):
    for 

def balanced(parant):
    if check_parant_count(parant):
        print('True')


balanced('((()()))()')
#balanced('(()())()')
#balanced('(())())()')