X = int(input())
N = int(input())
ss = 0
for _ in range(N) :
    price, num = map(int,input().split())
    ss += price*num

if X == ss : print("Yes") 
else : print("No")
