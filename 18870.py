# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
#
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
#
# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

import sys
input = sys.stdin.readline

N = int(input())
lst1 = list(map(int, input().split()))
lst2 = list(sorted(set(lst1)))

dict = {lst2[i] : i for i in range(len(lst2))}

for i in lst1:
    print(dict[i], end = " ")

# 결과로부터 역으로 해석해서 문제를 이해했다.
