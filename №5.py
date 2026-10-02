n = int(input())
k = [i for i in range(2, n + 1)]
for i in range(2, n + 1):
    for j in k:
        if j % i == 0 and j != i:
            k.remove(j)
print(k)