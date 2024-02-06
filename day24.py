import numpy as np
f = open('day24.txt').read()
l = f.split('\n')
snowballs = {}
for i, line in enumerate(l):
    data = line.split('@')
    start = [int(i) for i in data[0].split(',')]; vel = [int(i) for i in data[1].split(',')]
    k = vel[1]/vel[0]
    n = start[1] - k*start[0]
    snowballs[i] = [[start[0], start[1]], k, n, int(vel[0]/abs(vel[0]))]
checked = []
P = 0
for s1 in snowballs:
    for s2 in snowballs:
        if s1 != s2 and sorted([s1, s2]) not in checked:
            checked.append([s1, s2])
            n1 = snowballs[s1][2]; k1 = snowballs[s1][1]
            n2 = snowballs[s2][2]; k2 = snowballs[s2][1]
            if k1 != k2:
                x = (n2 - n1)/(k1-k2)
                y = k1*x+n1
                t1 = (x - snowballs[s1][0][0]); t2 = (x - snowballs[s2][0][0])
                if t1/abs(t1) == snowballs[s1][3] and t2/abs(t2) == snowballs[s2][3]:
                    if x >= 200000000000000 and x <= 400000000000000 and y >= 200000000000000 and y <= 400000000000000:
                        P += 1
print(P)