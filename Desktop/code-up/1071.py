# 1071 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기1
# 정수가 순서대로 입력된다. 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
# 입력 : 정수가 순서대로 입력된다. 단 개수는 알 수 없다.
# 출력 : 입력된 정수를 줄을 바꿔 하나씩 출력하는데, 0이 입력되면 종료한다. (0은 출력하지 않는다.)

a = input().split()
for i in a:
    if(i == '0'):
        break
    else:
        print(i)


'''
# 스터디 해설
a = map(int,input().split())
for i in a :
    if i == 0:
        exit()
    else: print(i)


b = list(map(int,input().split()))
a = 0
for i in b:
    if(b[a] == 0):
        break
    else:
        print(b[a])
    a = a + 1


arr = [int(x) for x in input().strip().split()] # for문 돌려서 정수형으로 리스트에 저장

for i in arr:
    if(i==0): break
    print(i)
'''


