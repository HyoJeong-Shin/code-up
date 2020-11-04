# 1166 : 윤년 판별
# 1. 해(year)가 4의 배수이면서 100의 배수가 아니면 윤년.
# 2. 400의 배수이면 윤년.

year = int(input())
print("yes") if(year % 4 ==0 and year % 100 != 0) or (year % 400 == 0) else print("no")
