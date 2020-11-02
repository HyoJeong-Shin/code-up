# 1112 : 두 정수 출력
# 입력 받은 두 정수를 출력

a, b = map(int, input().split())
print(a, b)


# input 한 번에 값을 여러 개 입력 받기
'''
변수1, 변수2 = input().split()  # 입력 받은 값을 공백을 기준으로 분리
변수1, 변수2 = input().split('기준 문자열') # 입력 받은 값을 기준 문자열을 기준으로 분리
변수1, 변수2 = input('문자열').split()
변수1, 변수2 = input('문자열').split('기준문자열')
'''
"""
EX1) b = input('문자열 두 개를 입력하세요: ').split()   
        print(a)    print(b)
        문자열 두 개를 입력하세요: Hello Python
        Hello
        Python

EX2) a, b = input('숫자 두 개를 입력하세요: ').split()
        print(a + b)
        숫자 두 개를 입력하세요: 10 20
        1020
"""

# map을 사용하여 정수로 변환하기 (실수 변환시 int 대신 float)
'''
변수1, 변수2 = map(int, input().split())
변수1, 변수2 = map(int, input().split('기준문자열'))
변수1, 변수2 = map(int, input('문자열').split())
변수1, 변수2 = map(int, input('문자열').split('기준문자열'))
'''
"""
a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
        print(a + b)
        숫자 두 개를 입력하세요: 10 20
        30
"""

