# 1068 : [기초-조건/선택실행구조] 정수 1개 입력받아 평가 출력하기
# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.
# 입력 : 정수(0 ~ 100) 1개가 입력된다.  ex) 73
# 출력 : 평가 결과를 출력한다.  ex) B

score = int(input())
if 90 <= score and score <= 100:
    print('A')
elif 70 <= score and score <= 89:
    print('B')
elif 40 <= score and score <= 69:
    print('C')
else:
    print('D')