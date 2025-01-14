t = int(input())

for i in range(t) :
    r, s = input().split()
    r = int(r)
    for j in range(len(s)) : 
        print(s[j]*r , end = '')
    print()
# inner 반복에서 마지막에 print() 안쓰면 줄 안바뀌고 한줄에 다 출력됨