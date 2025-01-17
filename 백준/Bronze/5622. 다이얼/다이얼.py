s = input()
number = 0

for i in s:
  if i in ["A","B","C"]:
    number += 3
  elif i in ["D","E", "F"]:
    number += 4
  elif i in ["G","H" ,"I"]:
    number += 5
  elif i in ["J", "K","L"]:
    number += 6
  elif i in ["M","N" ,"O"]:
    number += 7
  elif i in ["P" ,"Q", "R","S"]:
    number += 8
  elif i in ["T" ,"U", "V"]:
    number += 9
  elif i in ["W","X", "Y","Z"]:
    number += 10

print(number)