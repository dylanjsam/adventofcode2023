f = open('day4.txt', 'r')

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
def part2(f):
    linenum = 1
    S = 0
    length = 0
    dict = {}
    for line in f:
        length += 1
        dict[str(length)] = int(1)
    
    for line in f:
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

        count = 0
        for number in left:
            if number in right:
                count += 1
            print(count)
        index = 1
        for amount in range(0, count):
            dict.update({str(index+linenum): int(dict[str(index+linenum)]) + 1})
            index += 1
        linenum += 1
print(part2(f))