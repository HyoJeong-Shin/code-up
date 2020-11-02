# 1099 : [기초-2차원배열] 성실한 개미
# 입력 : 10*10 크기의 미로 상자의 구조와 먹이의 위치가 입력된다.
# 출력 : 성실한 개미가 이동한 경로를 9로 표시해 출력한다.

lst = [[0 for i in range(11)] for j in range(11)]

for i in range(10):
    a = list(map(int, input().split()))
    for j in range(10):
        lst[i+1][j+1] = a[j]

x = 2
y = 2

while True:
    if(lst[x][y] == 0):
        lst[x][y] = 9
    elif(lst[x][y] == 2):
        lst[x][y] = 9
        break
    if((lst[x][y+1] == 1 and lst[x+1][y] ==1) or (x == 9 and y == 9)):
        break
    if(lst[x][y+1] != 1):
        y+=1
    elif(lst[x+1][y] != 1):
        x += 1

for i in range(1, 11):
    for j in range(1, 11):
        print(lst[i][j], end=' ')
    print('')



'''
# 스터디 해설
arr = [[0]*10 for i in range(10)]

for i in range(10):
    arr[i] = list(map(int,input().split()))
    

x = 1
y = 1

while True:
    if arr[x][y] > 0:
        break
    
    arr[x][y] = 9
    
    # 아래쪽보다 오른쪽이 우선 : 오른쪽이 1이 아니면 무조건 오른쪽으로 가고, 오른쪽이 1이면 아래로 감 
    if arr[x][y+1] == 1:
        x = x+1
    elif arr[x][y+1] == 0 or 2:
        y = y+1
    
if arr[x][y] == 2: arr[x][y] = 9    

for i in arr:
    for j in i:
        print(j, end=' ')
    print()
'''