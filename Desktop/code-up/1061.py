# 1061 : [기초-비트단위논리연산] 비트단위로 OR 하여 출력하기
# 입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자.
# 비트단위(bitwise) 연산자 |(or, vertical bar, 버티컬바)를 사용하면 된다.
# 비트단위 or 연산은 둘 중 하나라도 1인 자리를 1로 만들어주는 것과 같다.
# 입력 : 2개의 정수가 공백을 두고 입력된다.     ex) 3 5
# 출력 : 두 정수를 비트단위(bitwise)로 or 계산을 수행한 결과를 10진수로 출력한다.   ex) 7

a, b = input().split()
print(int(a)|int(b))