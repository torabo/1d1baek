a, b ,c =map(int,input().split())

if (a==b)&(b==c)&(a==c)  : price = 10000+ (a * 1000)
elif a == b : price = 1000+a*100
elif b == c : price = 1000+b*100
elif a == c : price = 1000+c*100
elif (a!=b)&(b!=c)&(a!=c) : price =max(a,b,c) * 100


print(price)