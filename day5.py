f = open('day5.txt', 'r')
def findseeds(file):
    file.seek(0)
    seeds = []
    for i in file.readline().split():
        if i.isdigit():
            seeds.append(i)
    return seeds

def findmaps(file):
    z = 1
    file.seek(0)
    maps = {}
    file.readline()
    file.readline()
    lines = file.readlines()
    name = "blank"
    map = []
    for line in lines:
        z += 1
        if line.strip():
            if line.split()[0].isdigit() == False or z == 196:
                maps[name] = map
                map = []
                name = line.strip()
            else:
                map.append(line.split()) 
    return(maps)

def inputoutput(input, map):
    output = input
    for line in map:
        if int(input) >= int(line[1]) and int(input) < int((int(line[1])+int(line[2]))):
            output = int(line[0]) + int(input) - int(line[1])
            break
    return output

maps = findmaps(f)
locations = []

def newseeds(s):
    seeds = []
    for i in range(0, len(s)):
        if i % 2 != 0:
            for l in range(0, int(s[i])):
                seeds.append(int(s[i-1])+l)
    return seeds

print(newseeds(findseeds(f)))



for seed in findseeds(f):
    input = int(seed)
    for name in maps:
        input = inputoutput(input, maps[name])
    locations.append(input)
print(min(locations))


