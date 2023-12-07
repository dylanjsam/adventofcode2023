f = open('day5.txt', 'r')
def findloc(seed, maps):
        print(seed)

def inputoutput(input, map):
    for line in map:
          output = input
          if input >= line[1] and input <= (line[1]+line[2]):
                output = line[0] + input - line[1]
    return output

print(inputoutput(500, [[50, 450, 100], [30, 500, 50]]))