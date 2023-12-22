f = open('day11.txt').read()
data = f.splitlines()

rows = []
columns = []
for i, line in enumerate(data):
    if '#' not in line:
        rows.append(i)

rot = []
for i in range(0, len(data[0])):
    rot.append([])
for line in data:
    for i, char in enumerate(line):
        rot[i].append(char)

dataff = []
for i, line in enumerate(rot):
    if '#' not in line:
        columns.append(i)

print(rows, columns)

p = []
for j, row in enumerate(data):
    for i, char in enumerate(row):
        if char == '#':
            p.append([i, j])

q = []
for point in p:
    p1 =[]
    c = point[0]
    r = point[1]
    for column in columns:
        if point[0] > column:
            c += 1000000
    p1.append(c)
    for row in rows:
        if point[1] > row:
            r += 1000000
    p1.append(r)
    q.append(p1)

tot = 0
for star in q:
    for ostar in q:
        dist = abs((star[0] - ostar[0])) + abs((star[1] - ostar[1]))
        tot += dist
print(tot/2)