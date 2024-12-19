# 현재 시각과 분 입력받기
A, B = map(int, input().split())

# 조리 시간(분 단위) 입력받기
C = int(input())

# 총 분 계산
total_minutes = B + C

# 시간과 분으로 변환
A = A + (total_minutes // 60)  # 총 시간을 구함
M = total_minutes % 60         # 나머지 분을 구함

# 24시간 형식으로 시간 조정
A = A % 24

# 결과 출력
print(A, M)