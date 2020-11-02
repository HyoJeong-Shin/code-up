# 1111 : %출력
# 어떤 정수가 입력되면 %를 붙여 출력

# 나의 방법 : 정수를 문자열로 바꿔주어 붙여 출력
'''
i = int(input())
print(str(i)+"%")
'''
# 또 다른 방법 -> 변수의 정수형 그대로 유지
i = int(input())
print("%d%%" % i)

# 변수를 문자열과 함께 출력할 때는 연결 방식을 사용, 이때 %를 사용
# %출력하기 : %%
'''
%f : 실수(float)
%d : 정수(integer)
%s : 문자열(string)
'''
"""
EX1) name = "Amy"    print("Hello %s" % (name)) => Hello Amy
EX2) day = 7    print("03 - %s - 2018" % (day)) => 03 - 7 - 2018
"""
