file = open('day4.txt', 'r')
def part1(f):
    S = 0
    for line in f:
        a = 0
        sep = line.split("|")
        z = 0
        for side in sep:
            if z == 0:
                left = []
                sept = side.split()
                for i in range(2, len(sept)):
                    left.append(sept[i])
            else:
                right = []
                sept = side.split()
                for i in range(0, len(sept)):
                    right.append(sept[i])
            z += 1
        for number in left:
            if number in right and a == 0:
                a = 1
            elif number in right:
                a = 2*a
        S += a
    return S
#print(part1(f))


linenum = 0
S = 0
length = 0
dict = []
for line in file:
    length += 1
    dict.append(1)

file.seek(0)
for line in file:
    sep = line.split("|")
    z = 0
    for side in sep:
        if z == 0:
            left = []
            sept = side.split()
            for i in range(2, len(sept)):
                left.append(sept[i])
        else:
            right = []
            sept = side.split()
            for i in range(0, len(sept)):
                right.append(sept[i])
        z += 1
    count = 0
    for number in right:
        if number in left:
            count += 1
    index = 1
    for amount in range(0, count):
        dict[index+linenum] = dict[index+linenum] + dict[linenum] 
        index += 1
    linenum += 1
S = 0
for i in dict:
    S += i
print(S)
file.close()