# 1095 : [기초-1차원배열] 이상한 출석 번호 부르기3
# 출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.
# 입력 : 번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
#       n개의 랜덤 번호(k, 1 ~ 23)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.
# 출력 : 출석을 부른 번호 중에 가장 빠른 번호를 1개만 출력한다.

n = int(input())
a = input().split()
mn = 23

for i in range(0,n):
    if mn > int(a[i]) :
        mn = int(a[i])

print(mn)

'''
# 스터디 해설
n = int(input())
a = list(map(int,input().split()))

print(min(a))   # 최솟값 함수
'''