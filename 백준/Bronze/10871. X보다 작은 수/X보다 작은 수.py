n,x = map(int,input().split())
arry = list(map(int,input().split()))


for i in range(n) :
    if arry[i] < x :
        print(arry[i] ,end = ' ')