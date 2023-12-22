f = open('day11.txt').read()
data = f.splitlines()


dataf = []
for line in data:
    if '#' in line:
        dataf.append(line)
    else:
        dataf.append(line)
        dataf.append(line)

rot = []
for i in range(0, len(dataf[0])):
    rot.append([])
for line in dataf:
    for i, char in enumerate(line):
        rot[i].append(char)

dataff = []
for line in rot:
    if '#' in line:
        dataff.append(line)
    else:
        dataff.append(line)
        dataff.append(line)

l = []
for j, line in enumerate(dataff):
    for i, char in enumerate(line):
        if char == '#':
            l.append([i, j])





tot = 0
for i, star in enumerate(l):
    for ostar in l:
        dist = abs((star[0] - ostar[0])) + abs((star[1] - ostar[1]))
        tot += dist
print(tot/2)