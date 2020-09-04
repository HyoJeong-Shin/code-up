# 1066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기
# 세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
# 입력 : 세 정수 a, b, c 가 공백을 두고 입력된다.   ex) 1 2 8
# 출력 : 입력된 순서대로 짝(even)/홀(odd)을 줄을 바꿔 출력한다.
# ex) odd
#     even
#     even

a, b, c = input().split()
if int(a)%2 == 0 :
    print('even')
else:
    print('odd')

if int(b)%2 == 0 :
    print('even')
else:
    print('odd')

if int(c)%2 == 0 :
    print('even')
else:
    print('odd')