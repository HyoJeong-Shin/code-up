# 1170 : 당신의 학번은? 1
# 학년, 반, 번호가 공백을 기준으로 입력으로 주어진다. (정수)
# 학번을 붙여서 출력한다. 번호가 10번 미만일때는 0을 붙여 출력한다.

grade, classnum, num = map(int, input().split())
print("%d%d0%d" % (grade, classnum, num)) if num < 10 else print("%d%d%d" % (grade, classnum, num)) 