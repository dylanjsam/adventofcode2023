f = open("day1.txt", "r")
N = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
n = [1,2,3,4,5,6,7,8,9]
S = 0
page = 1
for line in f:
    page += 1
    z = ""
    p = []
    for letter in [*line]:
        if letter.isdigit() == True:
            p.append(letter)
        else:
            z += str(letter)
        counter = 0
        for i in N:
            if i in z:
                p.append(n[counter])
                z = str(letter)
            counter += 1
    if len(p) != 2:
        q = []
        q.append(p[0])
        q.append(p[len(p)-1])
        p = q
    number = int(str(p[0])+str(p[1]))
    S += number
print(S)