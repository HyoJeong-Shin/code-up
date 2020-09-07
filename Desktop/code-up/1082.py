# 1082 : [기초-종합] 16진수 구구단?
# A, B, C, D, E, F 중 하나가 입력될 때, 1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
# 입력 : 16진수로 한 자리 수가 입력된다. 단, A ~ F 까지만 입력된다.
# 출력 : 입력된 16진수에 1~F까지 순서대로 곱한, 16진수 구구단을 줄을 바꿔 출력한다. 계산 결과도 16진수로 출력해야 한다.

a = int(input(),16)
for i in range(1, 16):
    print(hex(a)[2:].upper() + '*' + hex(i)[2:].upper() + '=' + hex(a*i)[2:].upper() )

# hex() : 숫자를 16진수 형태의 문자열로 변환
# bin() : 숫자를 2진수 형태의 문자열로 변환
# oct() : 숫자를 8진수 형태의 문자열로 변환


"""
# 스터디 해설 
n = int(input(),16)

for i in range(1, 16):
    print(format(n,'X')+'*'+format(i,'X')+'='+format(n*i,'X'))

'''
- 다른진수 > 10진수
 int('value', 2)   int('value', 8)   int('value', 16)

- 10진수 > 다른진수
 bin(value), oct(value), hex(value)
  *  결과는 0b~, 0o~, 0x~ 형태로

- format
 format(value, 'b')  format(value, 'o')  format(value, 'x')
 깔끔하게 (대소문자 지정 가능)
 #붙이면 0b~ 요런 형태로
 https://dojang.io/mod/page/view.php?id=2300 참고
'''

x=int(input(),16)

for i in range(1,16):
	print(('%X'%x) +'*'+('%X'%i)+'='+('%X'%(x*i)))
"""