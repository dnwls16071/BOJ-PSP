# 승재는 인간-컴퓨터 상호작용에서 생체공학 설계를 공부하다가 키보드 자판이 실용적인지 궁금해졌다. 이를 알아보기 위해 승재는 다음과 같은 생각을 했다.
#
# 문자열에서 특정 알파벳이 몇 번 나타나는지 알아봐서 자주 나타나는 알파벳이 중지나 검지 위치에 오는 알파벳인지 확인하면 실용적인지 확인할 수 있을 것이다.'
#
# 승재를 도와 특정 문자열 $S$, 특정 알파벳 $\alpha$와 문자열의 구간 $[l,r]$이 주어지면 $S$의 $l$번째 문자부터 $r$번째 문자 사이에 $\alpha$가 몇 번 나타나는지 구하는 프로그램을 작성하여라. 승재는 문자열의 문자는 $0$번째부터 세며, $l$번째와 $r$번째 문자를 포함해서 생각한다. 주의할 점은 승재는 호기심이 많기에 (통계적으로 크게 무의미하지만) 같은 문자열을 두고 질문을 $q$번 할 것이다.

import sys
input = sys.stdin.readline
print = sys.stdout.write
S = input()
q = int(input())
for _ in range(q):
    cnt = 0
    a, l, r = map(str, input().split())
    l = int(l)
    r = int(r)
    lst = S[l:r+1]
    for i in lst:
        if a == i:
            cnt += 1
    sys.stdout.write(str(cnt))
    print()

# 50점 나온 코드 : 그 말인즉슨 문자열의 길이는 2000자 이하, 질문의 수는 2000자 이하일때만 맞고 그 이상일때는 시간초과가 발생한다는것

import sys
input = sys.stdin.readline
from string import ascii_lowercase

S = input().rstrip()
q = int(input())
char_lst = {}
lst = ascii_lowercase
for i in lst:
    char_lst[i] = [0]
    count = 0
    for j in range(len(S)):
        if S[j] == i:
            count += 1
        char_lst[i].append(count)

for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    print(char_lst[a][r+1] - char_lst[a][l])

# 문자열에서 알파벳 등장횟수를 알파벳별로 딕셔너리로 추가해 횟수를 배열로 저장한다.
# 문자열의 길이만큼 돌렸을 때 만약 해당 인덱스의 알파벳과 똑같다면 그 값을 1만큼 증가하고
# 그 다음 동일문자가 똑같이 나올때까지 1로 채워넣고 그 다음부터는 나올때마다 1씩 추가해준다.
# from string import ascii_lowercase를 통해서 a, b, c, d, e... 알파벳 26자를 받아올 수 있다.