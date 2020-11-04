# 1165 : 축구의 신 1

time, score = map(int, input().split())
if (time %10 ==0):
    print((90-time)//5 + score)
else:
    print((90-time)//5 + score + 1)