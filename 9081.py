# BEER라는 단어를 이루는 알파벳들로 만들 수 있는 단어들을 사전 순으로 정렬하게 되면
#
# BEER
# BERE
# BREE
# EBER
# EBRE
# EEBR
# EERB
# ERBE
# EREB
# RBEE
# REBE
# REEB
# 와 같이 된다. 이러한 순서에서 BEER 다음에 오는 단어는 BERE가 된다. 이와 같이 단어를 주면 그 단어를 이루는 알파벳들로 만들 수 있는 단어들을 사전 순으로 정렬할 때에 주어진 단어 다음에 나오는 단어를 찾는 프로그램을 작성하시오.

from itertools import permutations

N = int(input())
for i in range(N):
    word = input()
    lst = permutations(word, len(word))
