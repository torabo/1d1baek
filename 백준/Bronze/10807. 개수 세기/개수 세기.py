'''
sol1)
n = int(input())
list = input().split()
v = input()
a=0
for i in range(n):
    if list[i] == v :
       a+=1
print(a)'''

#sol2
N = int(input())
arr = list(map(int,input().split()))
v = int(input())
print(arr.count(v))


'''sol3
n = int(input())
list = input().split()
v = input()
a=0
for i in list :
    if i == v:
       a+=1
print(a)'''

