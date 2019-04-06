n = int(input())
strings = []

for i in range(n):
    strings.append(input().strip())
    
i = 0
s = ''

min_length = min([len(x) for x in strings])

while(i < min_length):
    a = strings[0][i]
    c = 0
    for j in range(1,n):
        if a == strings[j][i]:
            c+=1
    if c==n-1:
        s = s + strings[0][i]
        i+=1
    else:
        break
print(s)