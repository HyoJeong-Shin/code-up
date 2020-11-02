# 1117 : 두 실수의 곱
# 두 실수를 입력받아 두 실수의 곱을 출력하되 소수 둘째자리까지 출력하시오.

a, b = map(float, input().split())
print('%.2f'%(a+b))

# 소수 둘째자리까지 출력하기 %.2f
# 소수 넷째자리까지 출력하기 %.4f

# 또 다른 방법 - 파이썬 내장 함수 round 함수 이용 (반올림 결과 출력)
a, b = map(float, input().split())
print(round((a+b),2))

# round(a, 출력 원하는 자릿수)