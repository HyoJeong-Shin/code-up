# 1067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분석하기
# 정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.
# 입력 : 정수 1개가 입력된다.   ex) -2147483648
# 출력 : 입력된 정수에 대해 첫 줄에 minus 나 plus 를 출력하고, 두 번째 줄에 odd 나 even 을 출력한다.
# ex) minus
#     even 

a = int(input())
if a < 0 :
    print('minus')
else:
    print('plus')

if a%2 == 0 :
    print('even')
else:
    print('odd')