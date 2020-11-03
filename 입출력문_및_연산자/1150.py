# 1150 : 세 수 중 가장 작은 수
# 세 정수가 주어지면 그 중 가장 작은 수를 출력한다.

data = list(map(int, input().split()))
print(min(data))

# 세 정수를 리스트에 저장하여 리스트 값 중 가장 작은 값을 출력

'''
a, b, c = map(int, input().split())
if a>b & a>c:
    print(a)
elif b>a & b>c:
    print(b)
else:
    print(c)
'''