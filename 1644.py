# 하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다. 몇 가지 자연수의 예를 들어 보면 다음과 같다.
#
# 3 : 3 (한 가지)
# 41 : 2+3+5+7+11+13 = 11+13+17 = 41 (세 가지)
# 53 : 5+7+11+13+17 = 53 (두 가지)
# 하지만 연속된 소수의 합으로 나타낼 수 없는 자연수들도 있는데, 20이 그 예이다. 7+13을 계산하면 20이 되기는 하나 7과 13이 연속이 아니기에 적합한 표현이 아니다. 또한 한 소수는 반드시 한 번만 덧셈에 사용될 수 있기 때문에, 3+5+5+7과 같은 표현도 적합하지 않다.
#
# 자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램을 작성하시오.

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N = int(input())
    arr = [1 for _ in range(N+1)]

    prime_number = []
    for i in range(2, N+1):
        if arr[i] == 1:
            prime_number.append(i)
            for j in range(2*i, N+1, i):
                arr[j] = 0

    left = 0
    right = 0
    cnt = 0
    while right <= len(prime_number):
        value_sum = sum(prime_number[left:right])
        if value_sum == N:
            cnt += 1
            right += 1
        elif value_sum > N:
            left += 1
        else:
            right += 1
    print(cnt)

# 문제에 접근하는 방법은 한 번에 생각해냈지만 구현하는데 인덱스 오류가 자주 떠서 조금 시간이 걸렸던 문제였다.
# 일단 소수를 구하는 것이 관건이므로 에라토스테네스의 체를 이용해서 소수를 담은 리스트를 따로 만들었다.
# 그 다음 투 포인터를 이용해서 오른쪽 지점의 인덱스 값이 끝 지점에 도달하는 순간까지 루프를 돌려서 소수의 연속합을 만족시키는 경우를 찾아냈다.
