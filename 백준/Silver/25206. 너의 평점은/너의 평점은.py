grade_dict = {'A+' : 4.5 , 'A0' : 4.0, 'B+' : 3.5 , 'B0': 3.0, 'C+' : 2.5 , 'C0':2.0 , 'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0}
fin_score = 0
fin_num = 0
for i in range(20):
    name , num , grade = input().split()
    num = float(num)
    

    if grade != 'P' :
        fin_num += num
        fin_score += num * grade_dict[grade]
print(round(fin_score / fin_num , 6))

