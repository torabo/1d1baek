while True: 
    a, b, c = map(int, input().split())
    if a == 0 and b== 0 and c == 0:
        break
    
    sides = [a, b, c]
    max_side = max(sides)
    sides.remove(max_side)

    if sum(sides) <= max_side:
        print('Invalid')
    elif a == b == c : 
        print('Equilateral')
    elif (a == b) or (b == c) or (a == c):
        print('Isosceles')
    else :
        print('Scalene')