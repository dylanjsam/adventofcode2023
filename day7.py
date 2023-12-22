from collections import Counter
import operator

f = open('day7.txt')

def process(file):
    hands = {}
    for line in file:
        op = line.split()
        hands[op[0]] = int(op[1])
    return hands

def convert(dict):
    converted = {}
    for hand in dict:
        handc = ['23456789TJQKA'.index(i) for i in hand]
        p = tuple(reversed(sorted(handc)))
        converted[p] = [tuple(sorted((Counter(handc)).values())), dict[hand]]
    return converted

dict = convert(process(f))

def sorter(dict):
    pos = [(1,1,1,1,1),(1,1,1,2),(1,2,2),(1,1,3),(2,3),(1,4),(5,)]
    HC = []; OP = []; TP = []; TK = []; FH = []; FoK = []; FiK = []
    t = [HC, OP, TP, TK, FH, FoK, FiK]
    for hand in dict:
        i = pos.index(dict[hand][0])
        t[i].append(hand) 
    p = []
    for i in t:
        p.append(sorted(i, key=operator.itemgetter(0,1,2,3,4)))
    total = p[0] + p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
    return total
sorted = sorter(dict)
def count(dict, sorted):
    T = 0
    for i, hand in enumerate(sorted):
        T += (i+1)*dict[hand][1]
    return(T)
print(sorted)