# 준하는 기초통계학 수업에서 너비가 a, 높이가 ​​​​​b인 격자판의 좌하단 점으로부터 우상단 점까지 최단경로로 가는 방법의 수를 구하라는 과제를 받았어.
#
# 알고 있겠지만 정답은
#  \(\begin{pmatrix}a+b\\b\end{pmatrix}\)이야. 보기만 해도 벌써 조합을 계산할 생각에 신이 나지? 사실 조합을 구하는 문제도 코딩으로 해결할 수 있대. 코딩으로 과제를 해결해주자!

from math import factorial
import sys
input = sys.stdin.readline
N, R = map(int, input().split())
result = factorial(N) // (factorial(N-R) * factorial(R))
print(result % 1000000007)

# 팩토리얼을 통해서 코드를 작성했는데 어떤 부분에서 10점을 못 받았는지 알 수가 없었다.