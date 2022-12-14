# 세준이는 정수 S와 K가 주어졌을 때, 합이 S인 K개의 양의 정수를 찾으려고 한다. 만약 여러개일 경우 그 곱을 가능한 최대로 하려고 한다.
#
# 가능한 최대의 곱을 출력한다.
#
# 만약 S=10, K=3이면, 3,3,4는 곱이 36으로 최대이다.
#

S, K = map(int, input().split())

a = S // K
b = S % K

ans = 1
for _ in range(K):
    if b > 0:
        ans *= (a + 1)
        b -= 1
    else:
        ans *= a
print(ans)

# 처음엔 조합론의 방식을 이용하여 생각하여 직관적으로 문제를 해결했지만 코딩으로 구현하려니 많이 시간이 걸려서 애먹었던 문제였다.
# ex. 10을 3개의 고른 수로 나누면 3 3 3이 되고 나머지는 1이 남게 된다.
# 이 때 나머지 1을 아무 수에나 더해주고 다시 곱을 계산하면 최대곱인 3*3*4=36이 나온다.
# K번 반복문을 돌려서 만약 b > 0 이면 반복문을 돌릴때마다 남는 나머지를 더해줘서 곱해줘야한다.

# ex. 합이 11인 3개의 양의 정수를 찾으려고 하는 경우를 예로 설명해보자.
# 우선 11을 3개의 고른 수로 나누면 3 3 3이 되고 나머지는 2가 남게 된다.
# 반복문을 두 번 돌려서 1을 아무 수에나 더해준다. 이 때 남는 나머지가 0보다 크다면 계속 1씩 더해줘서 곱해줘야한다.
# 그렇다면 결과는 3 * 4 * 4 = 48이 나오게된다.