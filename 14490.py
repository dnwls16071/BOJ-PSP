# 대열이는 욱제의 친구다.

# “야 백대열을 약분하면 뭔지 알아?”
# “??”
# “십대일이야~ 하하!”
# n:m이 주어진다. 욱제를 도와주자. (...)

# 나는 편의상 N이 M보다 크다고 가정하고 코드를 작성하였다.

# 1차 작성 코드
from sys import stdin
from math import gcd
    
N, M = map(int, stdin.readline().split(":"))
gcd_num = gcd(N, M)

print(str(N//gcd_num) + ":" + str(M//gcd_num))

#2차 작성 코드
from sys import stdin
from math import *

N, M = map(int, stdin.readline().split(":"))
def gcd(N, M):
    while M:
        N, M = M, N % M
    return N
print(str(N//gcd(N, M)) + ":" + str(M//gcd(N, M)))
