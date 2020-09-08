# 1027 : [기초-입출력] 년월일 입력 받아 형식 바꿔 출력하기
# 년월일(yyyy.mm.dd)를 입력받아, 일월년(dd-mm-yyyy)로 출력해보자.
# (단, 한 자리 일/월은 0을 붙여 두자리로, 년도도 0을 붙여 네자리로 출력한다.) 
# 입력 : 년월일이 '.'(닷)으로 구분되어 입력된다.
# 출력 : 년월일을 일월년으로 바꾸어 '-'(대쉬, 마이너스)로 구분해 출력한다.

y, m, d = map(int,input().split('.'))
print('%02d-%02d-%04d' % (d,m,y))