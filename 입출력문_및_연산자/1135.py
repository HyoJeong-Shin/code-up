# 1135 : 관계연산자 1
# 두 정수 a, b가 공백을 두고 입력된다.(a,b는 int형 범위)
# a가 b보다 크거나 같을 경우 1, 그렇지 않은 경우 0을 출력한다.

a, b = map(int, input().split())
if a >= b :
    print(1)
else:
    print(0) 

# print(1) if a>=b else print(0)