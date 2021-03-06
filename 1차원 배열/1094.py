# 1094 : [기초-1차원배열] 이상한 출석 번호 부르기2
# 출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력해 보자.
# 입력 : 번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
#       n개의 랜덤 번호(k, 1 ~ 23)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.
# 출력 : 출석을 부른 번호 순서를 바꾸어 공백을 두고 출력한다.

n = int(input())
a = input().split()

for i in range(n-1,-1,-1):
    print(a[i], end=' ')


'''
# 스터디 해설 1
n = int(input())
a = list(map(int,input().split()))
a.reverse()     # reverse() : 거꾸로 배열   # 영구적으로 바뀜

print(*a)


# 스터디 해설 2
n=int(input())
numbers=list(map(int,input().split()))

for i in reversed(numbers):     # 일회성으로 바뀜 # for문 안에서만 거꾸로 배열됨
    print(i, end=' ')
'''