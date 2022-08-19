# 자연수 n개가 주어진다. 이 자연수의 공약수를 모두 구하는 프로그램을 작성하시오.

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n = int(input())
    result = []
    if n == 2:
        lst = list(map(int, input().split()))
        for i in range(1, min(lst)+1):
            if lst[0] % i == 0 and lst[1] % i == 0:
                result.append(i)
    elif n == 3:
        lst = list(map(int, input().split()))
        for i in range(1, min(lst)+1):
            if lst[0] % i == 0 and lst[1] % i == 0 and lst[2] % i == 0:
                result.append(i)

    for j in result:
        print(j)

# 위 코드를 Python3로 돌려보면 시간초과가 나왔다.
# 브루트포스의 탐색 범위가 넓다보니 나올 수 있는 결과라고 생각하여 어떻게 하면 시간초과를 해소할 수 있을지 고민했다.
# 위 코드를 PyPy3로 돌려보면 맞았다는 결과가 출력되었다.

