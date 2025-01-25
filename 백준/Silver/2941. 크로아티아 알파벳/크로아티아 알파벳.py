# 입력받기
word = input()

# 크로아티아 알파벳 목록
croatian_alphabets = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

# 크로아티아 알파벳을 하나의 문자로 치환
for ca in croatian_alphabets:
    word = word.replace(ca, 'a')

# 결과 출력 (치환된 단어의 길이 = 크로아티아 알파벳 개수)
print(len(word))