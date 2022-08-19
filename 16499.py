# 소문자로 이루어진 단어 N개가 주어졌을 때, 단어가 총 최소 몇 개의 그룹으로 이루어져 있는지 구하는 프로그램을 작성하시오.

# 그룹에 속한 단어는 모두 같은 알파벳으로 이루어져 있어야 하고, 개수도 같아야 한다. 즉, 단어를 구성하는 알파벳의 순서만 달라야 한다.

N = int(input())

word = []
for i in range(N):
    word.append(input())
    word[i] = list(word[i])
    word[i].sort()
    word[i] = str(word[i])

word = set(word)
print(len(word))