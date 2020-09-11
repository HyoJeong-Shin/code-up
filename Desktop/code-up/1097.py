# 1097 : [기초-2차원배열] 바둑알 십자 뒤집기
# 바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
# n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.
# 입력 : 바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력된다.
#       십자 뒤집기 횟수(n)가 입력된다. 십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수이다.
# 출력 : 십자 뒤집기 결과를 출력한다.
lst = [[0 for col in range (20)] for row in range(20)]

for i in range(19):
    a = list(map(int,input().split()))
    for j in range(19):
        lst[i+1][j+1] = int(a[j])

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(1, 20):
        if lst[x][j] == 0 :
            lst[x][j] = 1
        else:
            lst[x][j] = 0
        if lst[j][y] == 0:
            lst[j][y] = 1
        else:
            lst[j][y] = 0

for i in range(1, 20):
    for j in range(1, 20):
        print(lst[i][j], end=' ')
    print('')

