S = 0
f = open('day9.txt', 'r')

for line in f:
    tal = 0
    lines = line.split()
    d = []
    for i in lines:
        d.append(int(i))
    q = [d]
    while min(d) != 0 and max(d) != 0:
        p = []
        if len(d) > 1:
            for i in range(0, len(d)-1):
                p.append(d[i]-d[i+1])
        else:
            p = [0, 0]
        d = p
        q.append(d)
    for i in range(1, len(q)):
        q[-1-i].append(q[-i][-1]+q[-1-i][-1])
        S += q[-i][-1]+q[-1-i][-1]
print(S)
