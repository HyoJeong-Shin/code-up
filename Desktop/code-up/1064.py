# 1064 : [기초-삼항연산] 정수 3개 입력받아 가장 작은 수 출력하기
# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
# 단, 조건문을 사용하지 않고 3항 연산자 ? 를 사용한다.
# 입력 : 3개의 정수가 공백으로 구분되어 입력된다.   ex) 3 -1 5
# 출력 : 가장 작은 값을 출력한다.   ex) -1

a, b, c = input().split()
i1 = int(a)
i2 = int(b)
i3 = int(c)
print( (i1 if i1 < i2 else i2) if (i1 if i1 < i2 else i2) < i3 else i3)