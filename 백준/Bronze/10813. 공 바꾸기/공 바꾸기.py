n, m = map(int, input().split())

basket = [idx+1 for idx in range(n)]

for _ in range(m):
    i , j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1],  basket[i-1]

print(*basket)