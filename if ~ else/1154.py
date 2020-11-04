# 1154 : 큰수 - 작은수
# 정수 두개가 입력으로 들어오면 큰수 - 작은수의 값을 출력

a, b = map(int, input().split())
print(a-b) if a>b else print(b-a)