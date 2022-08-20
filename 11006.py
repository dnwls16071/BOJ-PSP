# 계란집을 운영하는 남욱이는 매일 닭장에서 달걀을 수거해간다. 어느 날 닭장에 들어가보니 일부 닭의 다리가 하나씩 사라졌다. 남욱이는 얼마나 많은 닭들이 한 다리를 잃었는지 알고싶었지만 닭이 너무 많아 셀 수 없었고, 대신 모든 닭의 다리수를 셌다. 고민하는 남욱이를 위해 모든 닭의 다리수의 합과 닭의 수를 가지고 이것을 해결해주자.

T = int(input())

for i in range(T):
    N, M = map(int, input().split())    # 모든 닭의 다리수의 합, 닭의 수

    res = 2 * M - N
    print(res, M - res)