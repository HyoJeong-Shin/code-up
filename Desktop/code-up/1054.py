# 1054 : [기초-논리연산] 둘 다 참일 경우만 참 출력하기
# 두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 참일 때에만 참을 출력하는 프로그램을 작성해보자.
# 입력 : 1 또는 0의 값만 가지는 2개의 정수가 공백을 두고 입력된다.  ex) 1 1
# 출력 : 둘 다 참(1)일 경우에만 1을 출력하고, 그 외의 경우에는 0을 출력한다. ex) 1

a, b = input().split()
if int(a)==1 and int(b)==1:
    print('1')
else:
    print('0')


'''
# 스터디 해설
 a,b = map(int,input().split())
if a == 1 and b ==1 : print(1)
else : print(0)

# m = map(int, x)        
# 리스트의 요소를 int로 변환, 결과는 맵 객체
'''