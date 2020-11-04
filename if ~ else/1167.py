# 1167 : 두 번째로 작은 수
# 세 개의 숫자가 주어질 때 두번째로 작은 수를 출력

a, b, c = map(int, input().split())
if a <= b and a <=c :
    if b <= c:
        print(b)
    else:
        print(c)
elif b <= a and b <= c:
    if a <= c:
        print(a)
    else:
        print(c)
else:
    if a <= b:
        print(a)
    else:
        print(b)


'''
# sort정렬 사용하여 두번째로 작은 수 찾기
data = list(map(int, input().split()))
data.sort()
print(data[1])
'''