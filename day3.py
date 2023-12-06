f = open('day3.txt', 'r')
partsign = ["%", "#", "*", "/", "=", "$", "&", "-", "@", "+"]
def part1(file):
    S = 0
    lines = []
    for line in file:
        stripped = [*line]
        stripped[-1] = stripped[-1].strip()
        lines.append(stripped)
    
    for i in range(0, len(lines)+1):
        z = 0
        if i == 0:
            for char in lines[0]:
                if char.isdigit() == True:
                    if lines[1][z-1] in partsign or lines[1][z] in partsign or lines[1][z+1] in partsign:
                        print("Found star", char)
                z += 1
        



print(part1(f))