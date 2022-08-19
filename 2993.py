# 독서를 싫어하는 원섭이는 책에서 단어 하나를 임의로 선택한다. 그 다음, 단어를 세 부분으로 나눈다.

# 세 부분으로 나눈 단어를 각각 순서를 뒤집는다. (첫 번째 글자와 마지막 글자의 위치를 바꾸고, 두 번째 위치와 뒤에서 두 번째 글자의 위치를 바꾸고... 이런 식으로 계속)

# 마지막으로, 이 세 단어를 나누기 전과 같은 순서로 합쳐 하나로 만든다.

# 원섭이는 사전순으로 가장 앞서는 단어를 만들려고 한다. 원섭이가 고른 단어가 주어졌을 때, 만들 수 있는 단어 중 가장 앞서는 단어를 출력하는 프로그램을 작성하시오.

word = input()
lst = []
# 파이썬 슬라이싱 위치의 끝값은 포함되지 않는다는 것을 명심
for i in range(len(word)-2):
    for j in range(i+1, len(word)-1):
        for k in range(j+1, len(word)):
            # i가 들어가면 안되는 이유 : 맨 첫 번째에서 시작한다는 것을 보장 못하므로 
            tmp = word[:j][::-1] + word[j:k][::-1] + word[k:][::-1]
            lst.append(tmp)
lst.sort()
print(lst[0])