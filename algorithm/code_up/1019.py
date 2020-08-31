#[기초-입출력] 연월일 입력받아 그대로 출력하기

date = input().split('.')
year = '%04d' % int(date[0])
month = '%02d' % int(date[1])
day = '%02d' % int(date[2])
print(year + "." + month + "." + day)


""" 방법2
date = input().split('.')
print( '%04d' % int(date[0]), '%02d' % int(date[1]) ,'%02d' % int(date[2]),sep=".")
"""

""" 방법3
yyyy, mm, dd = input().split('.');
print(yyyy.zfill(4), mm.zfill(2), dd.zfill(2), sep='.');
"""

"""모범답안
a,b,c=input().split('.')

print('%04d' % int(a), end='.')
print('%02d' % int(b), end='.')
print('%02d' % int(c))
"""
