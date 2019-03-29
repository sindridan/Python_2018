#verkefni2

#liður 1:
import itertools
from collections import defaultdict
#give ranks values
cards = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}

def rank_hand(hand):
    #check poker hands, starting from best to worst, returning highest possible number
    if royal_flush(hand):
        return 9
    if straight_flush(hand):
        return 8
    if four_of_a_kind(hand):
        return 7
    if full_house(hand):
        return 6
    if flush(hand):
        return 5
    if check_straight(hand):
        return 4
    if three_of_a_kind(hand):
        return 3
    if two_pair(hand):
        return 2
    if one_pair(hand):
        return 1
    if high_card(hand):
        return 0

def get_sorted_vals(hand):
    getValFromCards = list(card[0] for card in hand)
    cardsVal = list(x[0] for x in cards)
    compareCards = []
    for x in getValFromCards:
        for y in cardsVal:
            if x == y:
                compareCards.append(cards[x])
    sortedCards = []
    sortedCards = sorted(compareCards)
    return sortedCards

#get_sorted_vals([ 'JD', 'KD', 'TD', 'QD', 'AD' ])

def check_duplicates(hand):
    #split the hand for values:
    cardVals = [card[0] for card in hand]
    counter = defaultdict(lambda:0) #creating new dict to match the duplicates into same index
    for x in cardVals:
        counter[x] = counter[x] + 1 
    newSort = sorted(counter.values())

    return newSort
#check_duplicates([ 'JD', 'JH', 'JS', 'KC', 'KD' ])

#check straight and flush need to be on top to use as helper functions in straight flush etc
def check_straight(hand):
    getValFromCards = list(card[0] for card in hand)
    cardsVal = list(x[0] for x in cards)
    compareCards = []
    for x in getValFromCards:
        for y in cardsVal:
            if x == y:
                compareCards.append(cards[x])
    sortedCards = []
    sortedCards = sorted(compareCards)

    #extra check if ace is low
    if sortedCards == [2, 3, 4, 5, 14]:
        return True
    else:
        x = 0
        for x in range(len(sortedCards)):
            if sortedCards[x + 1] == sortedCards[x] + 1:
                x += 1
                if x == 4:
                    return True
            else:
                return False

#check_straight([ 'JD', 'KD', 'TD', 'QD', 'AD' ]) 
#check_straight([ 'AD', '2D', '3D', '4D', '5D' ]) 

def flush(hand):
    suits = list(h[1] for h in hand)
    isolateSuits = set(suits)
    if len(isolateSuits) == 1:
        return True
    return False
#flush([ 'JD', 'KD', 'TD', 'QD', 'AD' ]) 

def royal_flush(hand):
    if flush(hand) and check_straight(hand):
        getValFromCards = list(card[0] for card in hand)
        cardsVal = list(x[0] for x in cards)
        compareCards = []
        for x in getValFromCards:
            for y in cardsVal:
                if x == y:
                    compareCards.append(cards[x])
        sortedCards = []
        sortedCards = sorted(compareCards)
        if sortedCards == [10, 11, 12, 13, 14]:
            return True
    return False

#royal_flush([ '7D', 'KD', 'TD', 'QD', 'AD' ])

def straight_flush(hand):
    if check_straight(hand) and flush(hand):
        return True
    return False

#straight_flush([ 'JD', 'KD', 'TD', 'QD', 'AD' ])

def four_of_a_kind(hand):
    cardsSorted = list(get_sorted_vals(hand))
    for x in cardsSorted:
        if cardsSorted.count(x) == 4: #if any variation of x appears atleast 4 times as same value
            return True
    return False
#four_of_a_kind([ 'JD', 'JH', 'JS', 'JC', 'AD' ])


def full_house(hand):
    #split the hand for values:
    newSort = check_duplicates(hand)
    if newSort == [2,3]: # 2 duplicates, one of size 2 and anohter of size 3
        return True
    return False

#full_house([ 'JD', 'JH', 'JS', 'KC', 'KD' ])

def three_of_a_kind(hand):
    cardsSorted = list(get_sorted_vals(hand))
    for x in cardsSorted:
        if cardsSorted.count(x) == 3: #any variation of x that appears three times
            return True
    return False
#three_of_a_kind([ 'JD', 'JH', 'JS', 'KC', 'AD' ])

def two_pair(hand):
    sortedpaired = check_duplicates(hand)
    if sortedpaired == [1,2,2]: #when sorted, it should show values for 1 unique card, and two duplicate values of rest of cards
        return True
    return False

#two_pair([ 'JD', 'JH', 'QS', 'QC', 'AD' ])

def one_pair(hand):
    cardsSorted = list(get_sorted_vals(hand))
    #final check, this doesn't affect other checks since this doesn't affect other hand checks
    #because the best/better hand is already checked first
    for x in cardsSorted:
        if cardsSorted.count(x) == 2: #if x at any point appears again with same value
            return True
    return False
#two_pair([ 'JD', 'JH', 'QS', 'QC', 'AD' ])

def high_card(hand):
    return True

