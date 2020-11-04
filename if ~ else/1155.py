# 1155 : 7의 배수
# 어떤 정수가 입력되면 그 수가 7의 배수인지 확인하시오.
# 7의 배수일 경우 multiple를 출력하고, 7의 배수가 아니면 not multiple을 출력하시오.

a = int(input())
print('multiple') if (a%7 ==0) else print('not multiple')