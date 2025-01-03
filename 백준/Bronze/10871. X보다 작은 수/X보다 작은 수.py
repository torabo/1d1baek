n,x = map(int,input().split())
arry = list(map(int,input().split()))


for i in range(n) :
    if arry[i] < x :
        print(arry[i] ,end = ' ')

'''sol2
n , x = map(int, input().split())
arry = list(map(int, input().split()))

for i in arry:
    if i < x:
        print(i, end = ' ')
'''

'''sol3
n,x = map(int,input().split())
arry = list(map(int,input().split()))

result = [str(i) for i in arry if i <x]

print(" ".join(result))

'''
