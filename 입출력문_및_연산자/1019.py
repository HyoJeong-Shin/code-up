# 1019 : [기초-입출력] 연월일 입력받아 그대로 출력하기
# 입력 : 연, 월, 일이 ".(닷)"으로 구분되어 입력된다. ex) 2013.8.5
# 출력 : 입력받은 연, 월, 일을 yyyy.mm.dd 형식으로 출력한다.    ex) 2013.08.05
# (%02d를 사용하면 2칸을 사용해 출력하는데, 한 자리 수인 경우 앞에 0을 붙여 출력한다.)

year, month, day = input().split(".")
print("%04d.%02d.%02d" % (int(year), int(month), int(day)))



"""
# 스터디 해설

date = input().split('.')
year = '%04d' % int(date[0])
month = '%02d' % int(date[1])
day = '%02d' % int(date[2])
print(year + "." + month + "." + day)


''' 방법2
date = input().split('.')
print( '%04d' % int(date[0]), '%02d' % int(date[1]) ,'%02d' % int(date[2]),sep=".")
'''

''' 방법3
yyyy, mm, dd = input().split('.');
print(yyyy.zfill(4), mm.zfill(2), dd.zfill(2), sep='.');
'''

'''모범답안
a,b,c=input().split('.')
print('%04d' % int(a), end='.')
print('%02d' % int(b), end='.')
print('%02d' % int(c))
'''
"""