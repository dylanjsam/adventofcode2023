from collections import Counter
import operator
f = open('day7.txt').read().split('\n')

def convert(f):
    p = {}
    for line in f:
        hand = ['23456789TJQKA'.index(j) for j in line.split()[0]]
        p[tuple(hand)] = int(line.split()[1])
    return p

converted = convert(f)

def sort(converted):
    HC = []; OP = []; TP = []; TK = []; FH = []; FoK = []; FiK = []
    t = [HC, OP, TP, TK, FH, FoK, FiK]
    ts = [(1, 1, 1, 1, 1), (1, 1, 1, 2),(1, 2, 2),(1, 1, 3),(2, 3),(1, 4),(5,)]
    for i in converted:
        index = ts.index(tuple(sorted(Counter(i).values())))
        t[index].append(i)
    q = []
    for i in t:
        a = sorted(i, key=operator.itemgetter(0,1,2,3,4))
        q.append(a)
    t = []
    for i in range(0, 7):
        t+= q[i]
    return(t)
sorted = sort(converted)
def count(dict, list):
    T = 0
    for i, hand in enumerate(list):
        T+= dict[hand]*(i+1)
    return(T)

