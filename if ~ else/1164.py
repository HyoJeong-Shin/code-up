# 1164 : 터널 통과하기 1
# 터널의 높이가 차례대로 3개 주어진다. (정수)
# 170보다 같거나 작으면 "CRASH"를 출력, 그 보다 크면 "PASS"를 출력하시오.

a, b, c = map(int, input().split())
print("CRASH") if(a<=170 or b<=170 or c<=170 ) else print("PASS")
