f = open('day6.txt', 'r')
time = []
dist = []

line1 = f.readline().split()
for i in line1:
    if i.isdigit():
        time.append(int(i))
line2 = f.readline().split()
for i in line2:
    if i.isdigit():
        dist.append(int(i))
print(time)
print(dist)

t = 1
for i in range(0, len(time)):
    S = 0
    for charging in range(0, time[i]):
        speed = charging
        distance = (time[i] - charging)*speed
        if distance > dist[i]:
            S += 1
    t = t*S
print(t)