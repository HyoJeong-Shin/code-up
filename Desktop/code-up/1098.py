# 1098 : [기초-2차원배열] 설탕과자 뽑기
# 입력 : 첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고, 
#       두 번째 줄에 놓을 수 있는 막대의 개수(n)
#       세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.
# 출력 : 모든 막대를 놓은 격자판의 상태를 출력한다. 막대에 의해 가려진 경우 1, 아닌 경우 0으로 출력한다.
#       단, 각 숫자는 공백으로 구분하여 출력한다.

h, w = map(int,input().split())
n = int(input())
lst = [[0 for i in range(w+1)] for i in range(h+1)]

for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0:
            lst[x][y+j] = 1
        else:
            lst[x+j][y] = 1

for i in range(1, h+1):
    for j in range(1, w+1):
        print(lst[i][j], end=' ')
    print(' ')
            