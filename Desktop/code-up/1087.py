# 1087 : [기초-종합] 여기까지! 이제 그만~
# 1, 2, 3 ... 을 순서대로 계속 더해나갈 때, 그 합이 입력한 정수보다 작을 동안만 계속 더하는 프로그램을 작성해보자.
# 예를 들어 57을 입력하면 1+2+3+...+8+9+10=55에 다시 11을 더해 66이 될 때, 그 값 66이 출력되어야 한다.
# 입력 : 언제까지 합을 계산할 지, 정수 1개를 입력받는다.
# 출력 : 1, 2, 3, 4, 5 ... 순서대로 계속 더해가다가, 그 합이 입력된 정수보다 커지거나 같아지는 경우, 그때까지의 합을 출력한다.

a = int(input())
sum = 0
i = 1

while sum < a :
    sum += i
    i += 1

print(sum)