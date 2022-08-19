# 창영이는 매일 밤 하루동안 일어난 일을 일기장에 남긴다. 일기장을 쓰면서 영어 공부도 같이 하기 위해서 영어로 일기를 쓴다. 또, 남들이 자신의 일기장을 보는 것을 막기 위해서 모음('a','e','i','o','u')의 다음에 'p'를 하나 쓰고,  그 모음을 하나 더 쓴다.

# 예를 들어, "kemija" 는 "kepemipijapa"가 되고, "paprika"는 "papapripikapa"가 된다.

# 창영이가 일기장에 작성한 문장이 하나 주어졌을 때, 원래 문장은 무엇인지 구하는 프로그램을 작성하시오.

lst = ['a', 'e', 'i', 'o', 'u']
sentence = list(input())

for i in range(len(sentence)):
    if sentence[i] == "p":
        sentence.remove(sentence[i:i+2])
print(*sentence)