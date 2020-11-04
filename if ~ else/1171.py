# 1171 : 당신의 학번은? 2
# 학년, 반, 번호가 공백을 기준으로 입력된다.(정수)
# 학년은 한자리, 반은 두자리, 번호는 세자리로 출력
# 빈 부분은 0으로 채운다

grade, classnum, num = map(int, input().split())
print("%d%02d%03d" %(grade, classnum, num))

# %02d : 두자리, 빈 부분은 0으로 채움