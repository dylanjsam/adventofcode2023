f = open('day8.txt', 'r')

def instructions(file):
    p = []
    f.seek(0)
    instructions = [*f.readline().strip()]
    for i in instructions:
        if i == 'L':
            p.append(0)
        else:
            p.append(1)
    return p
def map(file):
    f.seek(0)
    map = {}
    f.readline()
    f.readline()
    for line in file:
        lines = ((((line.replace('=', '')).replace('(', '')).replace(',', '')).replace(')', '')).split()
        map[lines[0]] = (lines[1], lines[2])
    return map

map = map(f)
instructions = instructions(f)

og = 'AAA'
step = 0
while og != 'ZZZ':
    for dir in instructions:
        step += 1
        for i in map:
            if og == i:
                og = map[i][dir]
                break
print(step)
#part 2
start = []
end = []
for i in map:
    z = 0
    if [*i][2] == 'A':
        start.append(i)
    elif[*i][2] == 'Z':
        end.append(i)

p = False

while p == False:
    for dir in instructions:
        for i in start:
            for each in map:
                if i == each:
                    print(True)