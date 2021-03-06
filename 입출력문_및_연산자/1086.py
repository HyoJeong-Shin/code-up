# 1086 : [기초-종합] 그림 파일 저장용량 계산하기
# 일반적인 1024 * 768 사이즈(해상도)의 각점에 대해 24비트(rgb 각각 8비트씩 3개)로 저장하려면 1024 * 768 * 24 bit의 저장 용량이 필요하다.
# 입력 : w, h, b 가 공백을 두고 입력된다.   ex) 1024 768 24
# 출력 : 필요한 저장 공간을 MB 단위로 바꾸어 출력한다. 소수점 이하 셋째 자리에서 반올림해 둘째 자리까지 출력한 뒤 MB를 출력한다.    ex) 2.25 MB

w, h, b = map(int, input().split())
byte = (w * h * b) / 8
mb = byte / (1024**2)
print('%.2f MB' % mb)


'''
# 스터디 해설
W,H,B= map(int,input().split())

print('%.2f MB' % (W*H*B/8/1024/1024))

# round() 함수도 반올림 함수. round(x,2)하면 2번째 자리까지 반올림됨. 주로 변수에 사용될 듯?    %.2f는 출력시 주로 사용될 듯?
'''