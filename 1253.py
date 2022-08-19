# N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.
#
# N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.
#
# 수의 위치가 다르면 값이 같아도 다른 수이다.

N = int(input())
result = list(map(int, input().split()))
result.sort()

cnt = 0
for i in range(len(result)):
    tmp = result[:i] + result[i+1:]
    start = 0
    end = len(tmp)-1
    while start < end:
        total = tmp[start] + tmp[end]
        if total == result[i]:
            cnt += 1
            break
        elif total > result[i]:
            end -= 1
        else:
            start += 1
print(cnt)

# N개의 수 중에서 어떤 수가 다른 두 개의 수의 합으로 나타낼 수 있는 것을 확인하기 위해서 해당 수를 리스트에서 제외시킨다.
# 다른 방법도 많이 떠올랐지만 아직 구현을 하지 못한 문제였다.
