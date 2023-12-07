time = 48938595
dist = 296192812361391

t = 1
p = 0
for i in range(0, time):
    if i*(time-i)>dist:
        print('Done')
        break
    p += 1
print(p)
q = 0
for i in range(-time, 0):
    if abs(i)*(time-abs(i))>dist:
        print('Done')
        break
    q += 1
print(q)

print(time-q-p)