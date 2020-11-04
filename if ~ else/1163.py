# 1163 : 당신의 사주를 봐 드립니다 2
# 년도 + 월 + 일의 100의 자리가 숫자가 짝수이면 "대박"을 , 그렇지 않으면 "그럭저럭"을 출력하시오.

year, month, day = map(int, input().split())
hun = ((year + month +day) %1000 ) //100
print("대박") if(hun %2 ==0) else print("그럭저럭")