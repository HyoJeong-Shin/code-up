# 1020 : [기초-입출력] 주민번호 입력받아 형태 바꿔 출력하기
# 주민번호는 다음과 같이 구성된다. XXXXXX-XXXXXXX
# 앞의 6자리는 생년월일(yymmdd)이고 뒤 7자리는 성별, 지역, 오류검출코드이다.
# 입력 : 주민번호 앞 6자리와 뒷 7자리가 '-'로 구분되어 입력된다. ex)110011-0000000
# 출력 : '-'를 제외한 주민번호 13자리를 모두 붙여 출력한다.

id = input().split('-')
print("%06d%06d" % (int(id[0]), int(id[1])))

# %d를 하면 000907처럼 0으로 시작할 경우, 0이 생략되어버리기 때문에 6자리, 7자리에 맞춰서 %06d, %07d라고 설정해준다