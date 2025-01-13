s = input()

for i in range(97,123) :
    if chr(i) in s :
        print(s.index(chr(i)) , end = ' ')
    else :
        print(-1, end = ' ')


# index는 없는거 받으면 오류 뜨지만 find쓰면 없는거 -1로 변환함. 아마 find쓰는걸 원하는 문제 였던것 같음.
