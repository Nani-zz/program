n = int(input())
m = ''
for i in range(1, 10**9):
    if len(m) < n:
        m += str(i)
    if len(m) >= n:
        break
print(m[n - 1])
