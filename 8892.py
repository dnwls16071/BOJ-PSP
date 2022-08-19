# 팰린드롬은 어느 방향으로 읽어도 항상 같은 방법으로 읽을 수 있는 단어이다. 예를 들어, civic, radar, rotor, madam은 팰린드롬이다.

# 상근이는 단어 k개 적혀있는 공책을 발견했다. 공책의 단어는 ICPC 문제가 저장되어 있는 서버에 접속할 수 있는 비밀번호에 대한 힌트이다. 비밀번호는 k개의 단어 중에서 두 단어를 합쳐야 되고, 팰린드롬이어야 한다. 예를 들어, 단어가 aaba, ba, ababa, bbaa, baaba일 때, ababa와 ba를 합치면 팰린드롬 abababa를 찾을 수 있다.

# 단어 k개 주어졌을 때, 팰린드롬을 찾는 프로그램을 작성하시오.

# itertools를 사용한 방법
from itertools import combinations
T = int(input())
for _ in range(T):
    k = int(input())
    words = [input() for _ in range(k)]
    combination = list(combinations(words, 2))
    for a, b in combination:    # 이런 방법으로 2개를 한꺼번에 가져와서 비교
        tmp_a = a + b
        tmp_b = b + a
        if tmp_a == tmp_a[::-1]:
            print(tmp_a)
            break
        if tmp_b == tmp_b[::-1]:
            print(tmp_b)
            break
    else:
        print(0)
        
# itertools를 사용하지않은 방법
T = int(input())
palin = []
for _ in range(T):
    k = int(input())
    words = []
    for _ in range(k):
        b = input()
        words.append(b)
    for i in range(0, len(words)):
        for j in range(0, len(words)):
            if i == j:
                continue
            else:
                word = words[i] + words[j]
                if word == word[::-1]:
                    palin.append(word)
    if len(palin) > 0:
        print(palin[0])
    elif len(palin) == 0:
        print(0)
    palin = []  # palin 리스트를 초기화