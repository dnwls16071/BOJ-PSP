# 상근이는 망가진 전투 드로이드를 고치려고 하고 있다. 전투 드로이드의 각 부품의 가격은 다음과 같다.

# 블래스터 라이플	$350.34
# 시각 센서	$230.90
# 청각 센서	$190.55
# 팔	$125.30
# 다리	$180.90

T = int(input())

for i in range(T):
    A, B, C, D, E = map(int, input().split())
    res = A*350.34 + B*230.90 + C*190.55 + D*125.30 + E*180.90
    print("$%0.2f" % res)