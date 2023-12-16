d = open('day3.txt').read().splitlines()
map = []
S = 0
for line in d:
    p = [*line]
    map.append(p)
for j, row in enumerate(map):
    p = 0
    for i, char in enumerate(reversed(row)):
        if i != 0 or i != (len(row) - 1) or j != 0 or j != (len(map)-1):
            if char == '.':
                z = 0
                l = p
            elif char.isdigit:
                p += int(char)*10**z
                z += 1
            if reversed(map[j-1])[i-1] in
