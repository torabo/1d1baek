n = int(input())
cnt = n
for _ in range(n):
    l = input()
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            pass
        elif l[i] in l[i+1:]:
            cnt -= 1
            break

print(cnt)

