# 양의 정수 N과, N보다 큰 소수 P가 주어질 때, N!을 P로 나눈 나머지를 구하여라.

N, P = map(int, input().split())

ans = 1
for i in range(2, N+1):
    ans = (ans*i)%P
print(ans % P)

# 팩토리얼 라이브러리를 그대로 사용했더니 역시나 시간초과가 나왔다.
# 팩토리얼 대신에 반복문을 사용해서 구현하는 문제였다.
# 위 코드는 Python3에서는 시간초과가 나왔지만 PyPy3에서는 통과됐다.

# 재귀함수로도 코드를 작성했지만 역시나 최대 재귀 깊이를 초과했다는 경고문이 출력되었다,
# RecursionError : maximum recursion depth exceeded in comparison
