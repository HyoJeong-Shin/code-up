# 1065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기
# 세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.
# 입력 : 세 정수 a, b, c 가 공백을 두고 입력된다.   ex) 1 2 4
# 출력 : 짝수만 순서대로 줄을 바꿔 출력한다.    
# ex) 2
#     4

a, b, c = input().split()
if int(a)%2 == 0:
    print(a)

if int(b)%2 == 0:
    print(b)

if int(c)%2 == 0:
    print(c)