# 1069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기
# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.
# 입력 : 영문자 1개가 입력된다. (A, B, C, D 등의 한 문자가 입력된다.)   ex) A
# 출력 : 평가내용에 따라 다른 내용이 출력된다.  ex) best!!!

score = input()
if score == 'A':
    print('best!!!')
elif score == 'B':
    print('good!!')
elif score == 'C':
    print('run!')
elif score == 'D':
    print('slowly~')
else:
    print('what?')