alph = input().upper()

alph_lst = list(set(alph))
cnt = []
for i in alph_lst :
    cnt.append(alph.count(i))

if cnt.count(max(cnt)) >= 2 :
    print('?')
else : print(alph_lst[cnt.index(max(cnt))])

