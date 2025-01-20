chess = list(map(int,input().split()))

fin_chess = []

for i in range(0,2):
    if abs(chess[i]-1) == 0 :
        fin_chess.append(chess[i]-1)
    else :
        fin_chess.append(1-chess[i])

for i in range(2,5):
    if abs(chess[i]-2) == 0 :
        fin_chess.append(chess[i]-2)
    else :
         fin_chess.append(2-chess[i])

if chess[5] == 8 :
    fin_chess.append(0)
else :
        fin_chess.append(8-chess[5])

print(*fin_chess)
