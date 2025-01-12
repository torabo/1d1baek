while True :
    case = list(map(int, input().split()))
    case.sort()
    if case[0] == 0 and case[1] == 0 and case[2] == 0 : break
    if case[0]**2+ case[1]**2 == case[2]**2 :
        print('right')
    else : print('wrong')
    
