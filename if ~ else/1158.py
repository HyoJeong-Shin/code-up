# 1158 : 특별한 공 던지기 2
# 공이 떨어지는 위치 n이 30≤n≤40 이거나 60≤n≤70 이면, win을 출력, 그외에는 lose를 출력한다.

n = int(input())
print('win') if (30<=n and n <=40) or (60<=n and n <=70) else print('lose')