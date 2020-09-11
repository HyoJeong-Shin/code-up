# 1096 : [기초-2차원배열] 바둑판에 흰 돌 놓기
# 바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때, n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.
# 입력 : 바둑판에 올려 놓을 흰 돌의 개수(n)가 첫 줄에 입력된다.
#       둘째 줄 부터 n+1 번째 줄까지 힌 돌을 놓을 좌표(x, y)가 n줄 입력된다.
#       n은 10이하의 자연수이고 x, y 좌표는 1 ~ 19 까지이며, 같은 좌표는 입력되지 않는다.
# 출력 : 흰 돌이 올려진 바둑판의 상황을 출력한다. 흰 돌이 있는 위치는 1, 없는 곳은 0으로 출력한다.

n = int(input())

lst = [[0 for col in range (20)] for row in range(20)]

for i in range(n):
    x,y = map(int,input().split())
    lst[x][y] = 1

for i in range(1,20):
    for j in range(1,20):
        print(lst[i][j], end=' ')
    print('')

