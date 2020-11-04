# 1168 : 나이 계산 1
# 성별 정보는 1이면 1900년대 출생 남자, 2이면 1900년대 출생 여자, 3이면 2000년대 출생 남자, 4이면 2000년대 출생 여자를 말한다.
# 생년월일(6자리)과 성별정보(1자리)가 공백으로 분리되어 정수로 주어진다.
# 2012년도에 현재 나이를 출력하시오.

birth, gender = input().split()
gender = int(gender)

if gender == 1 or gender == 2:
    birth = '19'+birth[0:2]
    print(2012-int(birth) + 1)
elif gender == 3 or gender ==4:
    birth = '20'+birth[0:2]
    print(2012-int(birth) + 1)


# 문자열 슬라이스 birth[0:2] 0번째 인덱스부터 1번째 인덱스까지 슬라이스