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
    print(S)
print(part1(f))