# 1063 : [기초-삼항연산] 두 정수 입력받아 큰 수 출력하기
# 입력된 두 정수 a, b 중 큰 값을 출력하는 프로그램을 작성해보자.
# 단, 조건문을 사용하지 않고 3항 연산자 ? 를 사용한다.
# a>b 의 결과가 참(1)이면 (a>b ? a:b)의 결과는 a가 되고,거짓(0)이면 (a>b ? a:b)의 결과는 b가 된다.
# 입력 : 두 정수가 공백을 두고 입력된다.
# 출력 : 두 정수 중 큰 값을 10진수로 출력한다.

a, b = input().split()
print(a if int(a)>int(b) else b)

# 파이썬에서의 삼항 연산자는 c언어나 자바와 다른 형식을 띄고 있다
# a if a>b else b   :true일 경우 a 반환, false일 경우 b 반환
