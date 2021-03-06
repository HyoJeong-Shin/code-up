# 1093 : [기초-1차원배열] 이상한 출석 번호 부르기1
# 출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.
# 입력 : 첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
#       두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.
# 출력 : 1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력한다.

n = int(input())
a = input().split()
lst = [0 for i in range(1,24)]

for i in range(n):
    lst[int(a[i]) - 1 ] += 1 

for i in range(23):
    print(lst[i], end=' ') 


'''
# 스터디 풀이 1
n = int(input())
arr = list(map(int, input().split()))

for i in range(1,24):
    print(arr.count(i))     # count()함수 : 배열 안에 i가 몇개 있는지 세어 줌


# 스터디 풀이 2
n = int(input())
a = list(map(int,input().split()))
arr = [0 for _ in range(23)]

for r in a :
    arr[r-1] += 1

print(*arr) #unpacking  --> * : 따옴표, 리스트 벗긴 채 출력 (띄어쓰기 포함 한 줄 출력)
'''