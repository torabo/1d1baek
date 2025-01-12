case= list(map(int, input().split()))
case.sort()
print(abs(case[1]-case[0]))
