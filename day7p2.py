from collections import Counter
import operator
f = open('day7.txt').read()
hands = f.split('\n')
def convert(hands):
    hands1 = hands.split()
    hand = ['J23456789TQKA'.index(i) for i in hands1[0]]
    return([hand, int(hands1[1])])

def jokertime(hand):
    bet = hand[1]
    hand = hand[0]
    p = []
    newcard = 0
    if 0 in hand and Counter(hand)[0] != 5:
        for card in hand:
            if card != 0:
                p.append(card)
        l = Counter(p)
        x = max(l.values())
        for i in l:
            if l[i] == x:
                newcard = i
    q = []
    for card in hand:
        if card == 0:
            q.append(newcard)
        else:
            q.append(card)
    return [tuple(q), bet]
dict = {}
for hand in hands:
    dict[tuple(convert(hand)[0])] = jokertime(convert(hand))
dict1 = {}
for hand in hands:
    dict1[tuple(convert(hand)[0])] = int(hand.split()[1])

def sort(converted):
    HC = []; OP = []; TP = []; TK = []; FH = []; FoK = []; FiK = []
    t = [HC, OP, TP, TK, FH, FoK, FiK]
    ts = [(1, 1, 1, 1, 1), (1, 1, 1, 2),(1, 2, 2),(1, 1, 3),(2, 3),(1, 4),(5,)]
    for i in converted:
        index = ts.index(tuple(sorted(Counter(converted[i][0]).values())))
        t[index].append(i)
    q = []
    for i in t:
        a = sorted(i, key=operator.itemgetter(0,1,2,3,4))
        q.append(a)
    t = []
    for i in range(0, 7):
        t+= q[i]
    return(t)

sorted1 = sort(dict)
print(sorted1)
def count(dict, list):
    T = 0
    for i, hand in enumerate(list):
        T+= dict[hand]*(i+1)
    return(T)

print(count(dict1, sorted1))


