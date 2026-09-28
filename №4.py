n = input().lower()
k = [i for i in n]
i = [y for y in set(k)]
l = []
m = []
for u in i:
    l.append([u, n.count(u)])
l = sorted(l, key=lambda x: x[1])
for j in range(0, 3):
    if j < len(l):
        m.append(l[j][0])
print(l, m)