# 1078 : [기초-종합] 짝수 합 구하기
# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.
# 입력 : 정수 1개가 입력된다.
# 출력 : 1부터 입력된 수까지 짝수의 합을 출력한다.

a = int(input())
sum = 0 
for i in range(1,a+1):
    if i % 2 == 0 :
        sum += i

print(sum)


'''
# 스터디 해설
a = int(input())
sum = 0

for i in range(0,a+1,2) :
    sum = sum + i

print(sum)
'''