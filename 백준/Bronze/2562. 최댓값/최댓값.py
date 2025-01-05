list = []

for i in range(9):
    list.append(int(input()))

M = max(list)
print(M)
print(list.index(M)+1)

'''
list = [int(input()) for _ in range(9)]

print(max(list))
print(list.index(max(list)) + 1)
'''