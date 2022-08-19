# 두 정수 n과 m이 주어졌을 때, 0 < a < b < n인 정수 쌍 (a, b) 중에서 (a2+b2+m)/(ab)가 정수인 쌍의 개수를 구하는 프로그램을 작성하시오.

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    T = int(input())
    a = 0
    b = 0
    for _ in range(T):
        count = 0
        n, m = map(int, input().split())
        for a in range(1, n-1):
            for b in range(a+1, n):
                if ((a**2) + (b**2) + m) % (a*b) == 0:
                    count += 1
        print(count)

# 위 코드를 Python3으로 돌렸을때 시간 초과가 나왔다.
# for문(반복문)을 많이 사용하는 복잡한 연산의 경우 PyPy3가 더 적합하여 돌려봤더니 정답으로 처리되었다.
# for문을 위와 같이 설정한 이유 : 0 < a < b < n 이므로
# a의 범위는 1부터 최대 n-2까지, b의 범위는 a+1부터 최대 n-1까지 나올 수 있다.(a, b 모두 n보다 작은 수이기 때문)
