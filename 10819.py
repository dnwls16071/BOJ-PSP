# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    from itertools import permutations
    N = int(input())
    arr = list(map(int, input().split()))
    lists = permutations(arr)

    max_value = 0   # 배열에 들어있는 수의 순서를 바꿔서 얻을 수 있는 식의 최댓값
    for lst in lists:
        cal_value = 0   # 각 순열의 경우 얻을 수 있는 식의 값
        for i in range(N-1):
            cal_value += abs(lst[i] - lst[i+1])
        if max_value < cal_value:
            max_value = cal_value
    print(max_value)

# itertools 라이브러리에서 permutations(순열)를 사용하여 쉽게 풀었다.
# 다만 라이브러리를 사용하지않고는 어떻게 접근해야할지 아직도 잘 모르는 문제였다.