# 세 정수 A, B, C의 평균은 (A+B+C)/3이다. 세 정수의 중앙값은 수의 크기가 증가하는 순서로 정렬했을 때, 가운데 있는 값이다.

# 두 정수 A와 B가 주어진다. 이때, A, B, C의 평균과 중앙값을 같게 만드는 가장 작은 정수 C를 찾는 프로그램을 작성하시오.

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    # C는 A보다 작으면서
    # B와 A의 차이값을 구해서 C도 A보다 그 차이값만큼 작으면 된다.
    # 그러면 A, B, C의 평균값은 A가 되고, 중앙값도 A가 된다.
    else:
        print(a - (b - a))