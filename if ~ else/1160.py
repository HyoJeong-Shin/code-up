# 1160 : 아르바이트 가는 날
# 월, 수, 금, 일 아르바이트를 감
# 1 = 월, 2= 화 .... 7 = 일
# 아르바이트 가는 날이면 "oh my god"를 가는 날이 아니면 "enjoy"를 출력하시오.

day = int(input())
print("enjoy") if (day == 2 or day == 4 or day == 6) else print("oh my god")