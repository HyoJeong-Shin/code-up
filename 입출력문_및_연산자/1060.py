# 1060 : [기초-비트단위논리연산] 비트단위로 AND 하여 출력하기
# 입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.
# 비트단위(bitwise)연산자 &를 사용하면 된다.(and, ampersand, 앰퍼센드라고 읽는다.)
# 비트단위 and 연산은 두 비트열이 주어졌을 때, 둘 다 1인 부분의 자리만 1로 만들어주는 것과 같다.
# 입력 : 2개의 정수가 공백을 두고 입력된다.
# 출력 : 두 정수를 비트단위(bitwise)로 and 계산을 수행한 결과를 10진수로 출력한다.

a, b = input().split()
print(int(a)&int(b))