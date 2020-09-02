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

## 2. 연속된 작은따옴표 3개 또는 큰따옴표 3개 사용하기 -> 더 읽기 쉽고 깔끔한 방법
multiline = '''
Life is too short
You need python
'''
print(multiline)

multiline = """
Life is too short
You need python
"""

print(multiline)

## 이스케이프 코드란? : 프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 "문자 조합" 
## 주로 출력물을 보기 좋게 정렬하는 용도로 사용한다
"""
\n : 문자열 안에서 줄을 바꿀 때 사용
\t : 문자열 사이에 탭 간격을 줄 때 사용
\\ : 문자 \를 그대로 표현할 때 사용
\' : 작은따옴표를 그대로 표현할 때 사용
\" : 큰따옴표를 그대로 표현할 때 사용
\r : 캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
\f : 폼 피드 리턴 (줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
\a : 벨 소리 (출력할 때 PC 스피커에서 '삑' 소리가 난다)
\b : 백 스페이스
\000 : 널 문자
"""


# 문자열 연산하기

## 문자열 더해서 연결하기 (Concatenation)
head = "Python"
tail = " is fun!"
print(head + tail)  #Python is fun!

## 문자열 곱하기 : *는 문자열의 반복을 의미
a = "python"
print(a * 2)    #pythonpython   #a를 두 번 반복하라는 뜻

## 문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)

## 문자열 길이 구하기 : len함수 (공백 포함)
a = "Life is too short"
print(len(a))   #17


# 문자열 인덱싱과 슬라이싱  : 리스트나 튜플에서도 사용 가능

## 문자열 인덱싱이란?
## "파이썬은 0부터 숫자를 센다" 
## a[번호] : 문자열 안의 특정한 값을 뽑아내는 역할 => 이러한 작업 : 인덱싱
a = "Life is too short, You need Python"
print(a[3])     #'e'    # a라는 문자열의 네 번째 문자 e를 말함   #a[0]:'L', a[1]:'i' ...

## 문자열 인덱싱 활용하기
## 문자열을 뒤에서부터 읽기 위해서는 마이너스(-) 기호를 붙임
print(a[12])    #'s'
print(a[-1])    #'n'    # 뒤에서부터 첫 번째 문자는 가장 마지막 문자 'n'
print(a[-2])    #'o'
### 뒤에서부터 첫 번째 문자를 표시할 때도 0부터 세어 "a[-0]이라고 해야 하지 않을까?" 
###  -> 0과 -0은 똑같은 것이기 때문에 a[-0]은 a[0]과 똑같은 값을 보여준다
print(a[0])     #'L'
print(a[-0])    #'L'

## 문자열 슬라이스 : 문자열에서 단어 뽑아내기
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)    #'Life'

### 슬라이싱(Slicing) 기법
### a[시작 번호 : 끝 번호] 지정할 때 끝 번호에 해당하는 것은 포함하지 않음
print(a[0:4])   #'Life' 
print(a[0:3])   #'Lif'

## 문자열을 슬라이싱 하는 방법
print(a[0:5])   #'Life '    # a[4]는 공백 문자이기 때문에 'Life '가 출력됨  # 공백 문자 역시 L, i, f, e 같은 문자와 동일하게 취급된다
print(a[5:7])   #'is'   # 슬라이싱할 때 항상 시작 번호가 0일 필요는 없다
print(a[12:17]) #'short'

print(a[19:])   #'You need Python'  # 끝 번호를 생략하면 시작 번호부터 그 문자열의 끝까지 뽑아낸다
print(a[:17])   #'Life is too short'   # 시작 번호를 생략하면 문자열의 처음부터 끝 번호까지 뽑아낸다
print(a[:])     #'Life is too short, You need Python'   # 시작 번호와 끝 번호를 생략하면 문자열의 처음부터 끝까지 뽑아낸다

print(a[19:-7]) #'You need'     # 인덱싱과 마찬가지로 마이너스 기호를 사용할 수 있다    # a[19]에서부터 a[-8]까지를 말한다. a[-7]은 포함하지 않는다

## 슬라이싱으로 문자열 나누기
a = "20010331Rainy"

### 날짜와 날씨를 나누기
date = a[:8]
weather = a[8:]
print("날짜:" + date + " 날씨:" + weather)

### 연도, 월과 일, 날씨 세 부분으로 나누기
year = a[:4]
day = a[4:8]
weather = a[8:]
print("연도:" + year + " 월/일:" + day + " 날씨:" + weather)

## "Pithon"이라는 문자열을 "Python"으로 바꾸려면?
a = "Pithon"

'''
a[1] = 'y'  # 오류 발생     
# 문자열의 요솟값은 바꿀 수 있는 값이 아니기 때문이다 (문자열 자료형은 그 요솟값을 변경할 수 없다. 그래서 immutable한 자료형이라고도 부른다) 
'''

a[:1]   #'P'
a[2:]   #'thon'
print(a[:1] + 'y' + a[2:])  #'Python'


# 문자열 포매팅 (Formatting) : 문자열 안에 어떤 값을 삽입하는 방법

## 1. 숫자 바로 대입
print("I eat %d apples." % 3)   # %d : 문자열 포맷 코드  # 문자열 안에 정수 3을 삽입     # 문자열 안에서 숫자를 넣고 싶은 자리에 %d 문자를 넣어 주고, 삽입할 숫자 3은 가장 뒤에 있는 % 문자 다음에 써 넣었다

## 2. 문자열 바로 대입
print("I eat %s apples." % "five")

## 3. 숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples." % number)

## 4. 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))    # 2개 이상의 값을 넣으려면 마지막 % 다음 괄호 안에 콤마(,)로 구분하여 각각의 값을 넣어 주면 된다

## 문자열 포맷 코드
'''
%s : 문자열 (String)
%c : 문자 1개 (character)
%d : 정수 (Integer)
%f : 부동소수 (floating-point)
%o : 8진수
%x : 16진수
%% : Literal % (문자 % 자체)
'''

## %s 포맷 코드는 어떤 형태의 값이든 변환해 넣을 수 있다. 왜냐하면 %s는 자동으로 % 뒤에 있는 값을 문자열로 바꾸기 때문이다
print("I have %s apple" % 3)
print("rate is %s" % 3.234)

### [포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다]
'''
print("Error is %d%." % 98)    # 값이 올바르지 않다는 값 오류(Value Error) 메시지를 보여 준다
# 이유는 문자열 포맷 코드인 %d와 %가 같은 문자열 안에 존재하는 경우, %를 나타내려면 반드시 %%로 써야 하는 법칙이 있기 떄문이다
'''
print("Error is %d%%." % 98)    #'Error is 98%'

## 포맷 코드와 숫자 함께 사용하기
## 1. 정렬과 공백
print("%10s" % "hi")    #'        hi'   # 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 그 앞의 나머지는 공백으로 남겨 두라는 의미이다
print("%-10sjane." % 'hi')   #'hi        jane.' # hi를 왼쪽 정렬하고 나머지는 공백으로 채웠다

## 2. 소수점 표현하기
print("%0.4f" % 3.42134234) #'3.4213'   # 소수점 네 번째 자리까지만 나타내고 싶은 경우  # '.'의 의미는 소수점 포인트를 말하고 그 뒤의 숫자 4는 소수점 뒤에 나올 숫자의 개수를 말한다
print("%10.4f" % 3.42134234)    #'    3.4213'   # 소수점 네 번째 자리까지만 표시하고 전체 길이가 10개인 문자열 공간에서 오른쪽으로 정렬한다

##format 함수를 사용한 포매팅
## 1. 숫자 바로 대입하기
print("I eat {0} apples".format(3))     #'I eat 3 apples'

## 2. 문자열 바로 대입하기
print("I eat {0} apples".format("five"))    #'I eat five apples'

## 3. 숫자 값을 가진 변수로 대입하기
number = 3
print("I eat {0} apples".format(number))    #'I eat 3 apples'

## 4. 2개 이상의 값 넣기
## 문자열의 {0}, {1}과 같은 인덱스 항목이 format 함수의 입력값으로 순서에 맞게 바뀐다. ex){0}은 format 함수의 첫 번째 입력값인 number로 바뀜
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))  #'I ate 10 apples. so I was sick for three days.'

## 5. 이름으로 넣기
## {name} 형태를 사용할 경우 format 함수에는 반드시 name = value 와 같은 형태의 입력값이 있어야만 한다
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))  #'I ate 10 apples. so I was sick for 3 days.'

## 6. 인덱스와 이름을 혼용하여 넣기
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))

## 7. 왼쪽 정렬
print("{0:<10}".format("hi"))   #'hi         '  #:<10 표현식을 사용하면 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞출 수 있다

## 8. 오른쪽 정렬
print("{0:>10}".format("hi"))   #'        hi'   # 오른쪽 정렬은 :>을 사용   # 화살표 방향을 생각하면 어느 쪽으로 정렬되는 지 알 수 있다

## 9. 가운데 정렬
print("{0:^10}".format("hi"))   #'    hi    '   # :^ 기호 사용하면 가운데 정렬

## 10. 공백 채우기
## 정렬할 때 공백 문자 대신에 지정한 문자 값으러 채워 넣는 것도 가능하다. 채워 넣을 문자 값은 정렬 문자 <, >, ^ 바로 앞에 넣어야 한다
print("{0:=^10}".format("hi"))  #'====hi===='
print("{0:!^10}".format("hi"))  #'!!!!hi!!!!'

## 11. 소수점 표현하기
y = 3.42134234
print("{0:0.4f}".format(y))     #'3.4213'
print("{0:10.4f}".format(y))    #'    3.4213'

## 12. { 또는 } 문자 표현하기
## {}와 같은 중괄호(brace) 문자를 포매팅 문자가 아닌 문자 그대로 사용하고 싶은 경우에는 {{}}처럼 2개를 연속해서 사용하면 된다
print("{{ and }}".format())     #'{ and }'
print("{{{0:0.4f}}}".format(y)) #'{3.4213}'

## f 문자열 포매팅 (파이썬 3.6버전부터 f 문자열 포매팅 기능 사용 가능)
## 문자열 앞에 f 접두사를 붙이면 f 문자열 포매팅 기능을 사용할 수 있다
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')     #'나의 이름은 홍길동입니다. 나이는 30입니다.'

print(f'나는 내년이면 {age+1}살이 된다.')   #'나는 내년이면 31살이 된다.'   #f 문자열 포매팅은 표현식을 지원하기 때문에 문자열 안에서 변수와 +, -와 같은 수식을 함께 사용할 수 있다 

## 1. 딕셔너리에서 f 문자열 포매팅 사용
## 딕셔너리 : Key와 Value라는 것을 한 쌍으로 갖는 자료형
d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')   #'나의 이름은 홍길동입니다. 나이는 30입니다.'

## 2. 정렬
print(f'{"hi":<10}')    #'hi        '   # 왼쪽 정렬
print(f'{"hi":>10}')    #'        hi'   # 오른쪽 정렬
print(f'{"hi":^10}')    #'    hi    '   # 가운데 정렬

## 3. 공백 채우기
print(f'{"hi":=^10}')   #'====hi===='
print(f'{"hi":!<10}')   #'hi!!!!!!!!'

## 4. 소수점
y = 3.42134234
print(f'{y:0.4f}')  #'3.4213'   # 소수점 4자리까지만 표현
print(f'{y:10.4f}') #'    3.4213'   # 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤

## 5. { }문자 표시
print(f'{{ and }}') #'{ and }'


# 문자열 관련 함수들
# 문자열 자료형은 자체적으로 함수를 가지고 있다. 이를 문자열 내장 함수라고 한다. 
# 이 내장 함수를 사용하려면 문자열 변수 이름 뒤에 '.'를 붙인 다음에 함수 이름을 써주면 된다

## 문자 개수 세기 (count)
a = "hobby"
print(a.count('b'))     #'2'

## 위치 알려주기1 (find)
a = "Python is the best choice"
print(a.find('b'))  #'14'   # 문자열 중 문자 b가 처음으로 나온 위치를 반환한다
print(a.find('k'))  #'-1'   # 찾는 문자나 문자열이 존재하지 않는다면 -1을 반환한다

## 위치 알려주기2 (index)
a = 'Life is too short'
print(a.index('t')) #'8'    # 문자열 중 문자 t가 맨 처음으로 나온 위치를 반환한다
#print(a.index('k')) # error    # 문자열 안에 존재하지 않는 문자를 찾으면 오류가 발생한다

## 문자열 삽입 (join)
print(",".join('abcd'))     #'a,b,c,d'  # abcd 문자열의 각각의 문자 사이에 ","를 삽입한다
print(",".join(['a','b','c','d']))  #'a,b,c,d'  # join 함수는 문자열뿐만 아니라 리스트나 튜플도 입력으로 사용할 수 있다

## 소문자를 대문자로 바꾸기 (upper)
a = "hi"
print(a.upper())    #'HI'   # 만약 문자열이 이미 대문자라면 아무 변화도 일어나지 않는다

## 대문자를 소문자로 바꾸기 (lower)
a = "HI"
print(a.lower())    #'hi'

## 왼쪽 공백 지우기 (lstrip)
a = " hi "
print(a.lstrip())   #'hi '  # 문자열 중 가장 왼쪽에 있는 한 칸 이상의 연속된 공백들을 모두 지운다

## 오른쪽 공백 지우기 (rstrip)
a = " hi "
print(a.rstrip())   #' hi'  # 문자열 중 가장 오른쪽에 있는 한 칸 이상의 연속된 공백들을 모두 지운다

## 문자열 바꾸기 (replace)
## replace(바뀌게 될 문자열, 바꿀 문자열)
a = "Life is too short"
print(a.replace("Life", "Your leg"))    #'Your leg is too short'

## 문자열 나누기 (split)
## 나눈 값은 리스트에 하나씩 들어가게 된다
a = "Life is too short"
print(a.split())    #['Life', 'is', 'too', 'short'] # 괄호 안에 아무 값도 넣어 주지 않으면 공백을 기준으로 문자열을 나누어 준다
b = "a:b:c:d"
print(b.split(':')) #['a', 'b', 'c', 'd']   # 괄호 안에 특정 값이 있는 경우 괄호 안의 값을 구분자로 해서 문자열을 나누어 준다