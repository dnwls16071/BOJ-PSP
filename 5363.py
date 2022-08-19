# 어린 제다이들은 요다와 대화하는 법을 배워야 한다. 요다는 모든 문장에서 가장 앞 단어 두 개를 제일 마지막에 말한다.

# 어떤 문장이 주어졌을 때, 요다의 말로 바꾸는 프로그램을 작성하시오.

N = int(input())
for i in range(N):
    sentence = list(input().split(" "))
    for i in range(2):
        sentence.append(sentence[0])
        sentence.remove(sentence[0])
    
    print(' '.join(sentence))