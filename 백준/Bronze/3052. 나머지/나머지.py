base = []
for _ in range(10):
    a = int(input())
    base.append(a)

new = []
for i in range(10):
    last = base[i] % 42
    new.append(last)


print(len(set(new)))
