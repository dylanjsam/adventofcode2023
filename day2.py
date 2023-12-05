f = open('day2.txt', 'r')
S = 0
for i in f:
    ballsd = {"red":0, "green":0, "blue":0}
    gamesr = i.split(":")
    ID = int(gamesr[0].split()[1])
    games = gamesr[1].split(";")
    for balls in games:
        each = balls.split(",")
        for ball in each:
            amount = ball.split()
            if int(amount[0]) > int(ballsd[amount[1]]):
                ballsd[amount[1]] = int(amount[0])
    power = int(ballsd["red"])*int(ballsd["green"])*int(ballsd["blue"])
    S += power
    #ok
print(S)