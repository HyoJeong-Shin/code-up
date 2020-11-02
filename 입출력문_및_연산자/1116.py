# 1116 : 사칙연산 계산기
# 두 정수를 입력받아 사칙연산을 출력하시오

a, b = map(int, input().split())
print("%d+%d=%d" % (a, b, a+b))
print("%d-%d=%d" % (a, b, a-b))
print("%d*%d=%d" % (a, b, a*b))
print("%d/%d=%d" % (a, b, a/b))
