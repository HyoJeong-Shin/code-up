# 1021 : [기초-입출력] 단어 1개 입력받아 그대로 출력하기
# 입력 : 한 단어가 입력된다.(단, 단어의 길이는 50자 이하이다.) ex) Informatics
# 출력 : 입력된 단어를 그대로 출력한다. ex) Informatics

word = str(input())
if len(word) <= 50:
    print(word)
