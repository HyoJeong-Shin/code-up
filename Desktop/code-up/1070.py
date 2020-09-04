# 1070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기
# 월이 입력될 때 계절 이름이 출력되도록 해보자.
# 입력 : 월을 의미하는 1개의 정수가 입력된다.(1 ~ 12)   ex) 12
# 출력 : 계절 이름을 출력한다.  ex) winter

month = int(input())
if month == 12 or month == 1 or month == 2:
    print('winter')
elif month == 3 or month == 4 or month == 5:
    print('spring')
elif month == 6 or month == 7 or month == 8:
    print('summer')
else:
    print('fall')


'''
# 스터디 해설
a = int(input())

if a in (12,1,2) :
    print('winter')
elif a in (3,4,5) :
    print('spring')
elif a in (6,7,8) :
    print('summer')
else : print('fall')
'''