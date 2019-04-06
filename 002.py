nk = list(map(int, input().strip().split()))

n = list(str(nk[0]))
k = nk[1]

for i in range(k):
    c=0
    for j in range(len(n)-1):
        if n[j] >= n[j+1]:
            c=1
            n.pop(j)
            break
    if c==0:
        n.pop(-1)
print(int(''.join(n)))