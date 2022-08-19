# 윤영이는 3의 배수 마니아이다. 그는 모든 자연수를 3개의 3의 배수의 자연수로 분해하는 것을 취미로 가지고 있다. 문득 그는 자신에게 주어진 수를 3개의 3의 배수로 분리하는 경우의 수가 몇 개인지 궁금해졌다. 하지만 윤영이는 마지막 학기이기 때문에 이런 계산을 하기에는 너무 게을러졌다. 그래서 당신에게 이 계산을 부탁했다.
#
# 즉, 임의의 3의 배수 자연수 n이 주어졌을 때, 해당 수를 3의 배수의 자연수 3개로 분리하는 방법의 개수를 출력해라. 단 분해한 수의 순서가 다르면 다른 방법으로 간주한다. 예를 들어 12 = 3 + 6 + 3 과 12 = 3 + 3 + 6 은 다른 방법이다.

if __name__ == "__main__":
    from itertools import combinations_with_replacement
    import sys
    input = sys.stdin.readline
    n = int(input())
    numbers = combinations_with_replacement(range(3, n+1, 3), 3)

    res = []
    for num in numbers:
        if sum(num) == n:
            res.append(num)

    cnt = 0
    for i in res:
        if i[0] == i[1] == i[2]:
            cnt += 1
        elif i[0] == i[1] or i[0] == i[2] or i[1] == i[2]:
            cnt += 3
        else:
            cnt += 6
    print(cnt)

# 위와 같은 방법으로 작성해봤는데 시간초과가 나왔다.

from math import factorial
def nCr(n, r):
    return factorial(n)//(factorial(n-r)*factorial(r))
def nHr(n, r):
    return nCr(n+r-1, r)
n = int(input())
print(nHr(3, n//3-3))

# 고등학교 수학인 팩토리얼 개념(중복조합, 조합)을 이용해서 작성해보았다.