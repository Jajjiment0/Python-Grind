h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
t1 = h1*60*60 + m1*60 + s1
t2 = h2*60*60 + m2*60 + s2
dt = t2 - t1
dh = (24 + dt // (60*60)) % 24
dm = (24*60 + dt // 60) % 60
ds = (24*60*60 + dt) % 60
print(str(dh) + ":" + \
 str(dm) + ":" + str(ds))