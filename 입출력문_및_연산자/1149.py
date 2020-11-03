# 1149 : 두 수 중 큰 수
# 두 정수 중 큰 정수를 출력한다.

a, b = map(int, input().split())
print(a) if a>b else print(b)


'''
data = list(map(int, input().split()))
print(max(data))
'''