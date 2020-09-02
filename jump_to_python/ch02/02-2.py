# 문자열(String) : 문자, 단어 등으로 구성된 문자들의 집합

## 파이썬에서 문자열을 만드는 방법 4가지
"Hello World"
'Python is fun'
"""Life is too short, You need python"""
'''Life is too short, You need python'''

## 1. 문자열 안에 작은따옴표(')를 포함시키고 싶을 때
food = "Python's favorite food is perl"
print(food)     #'Python's favorite food is perl'처럼 작은따옴표로 둘러싸면 'Python'이 문자열로 인식되어 구문 오류(SyntaxError)가 발생함

## 2. 문자열에 큰따옴표(")를 포함시키고 싶을 때
say = '"Python is very easy." he says.'
print(say)

## 3. 백슬래시(\)를 사용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기
## 백슬래시(\)를 작은따옴표나 큰따옴표 앞에 삽입하면 백슬래시 뒤의 따옴표는 문자열을 둘러싸는 기호의 의미가 아닌 문자('), (") 그 자체를 뜻하게 된다. 
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."
print(food)
print(say)

## 여러 줄인 문자열을 변수에 대입하고 싶을 때

## 1. 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기
multiline = "Life is too short\nYou need python" 
print(multiline)