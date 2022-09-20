# 알파벳 소문자로 이루어진 두 문자열 a와 b에 대해, a의 부분 수열의 순열이자 b의 부분 수열의 순열이 되는 가장 긴 문자열 x를 구하여라.

from collections import defaultdict
while True:
    try:
        a = input()
        b = input()
        lst1 = defaultdict(int)
        lst2 = defaultdict(int)
        ans = ""
        for i in a:
            lst1[i] += 1
        for i in b:
            lst2[i] += 1
        s = []
        for j in lst1:
            if j in lst2:
                s.append(j)
        s.sort()
        for t in s:
            ans += t * min(lst1[t], lst2[t])
        print(ans)
    except:
        break