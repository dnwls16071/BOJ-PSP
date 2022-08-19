# 위대한 해커 창영이는 모든 암호를 깨는 방법을 발견했다. 그 방법은 빈도를 조사하는 것이다.

# 창영이는 말할 수 없는 방법을 이용해서 현우가 강산이에게 보내는 메시지를 획득했다. 이 메시지는 숫자 N개로 이루어진 수열이고, 숫자는 모두 C보다 작거나 같다. 창영이는 이 숫자를 자주 등장하는 빈도순대로 정렬하려고 한다.

# 만약, 수열의 두 수 X와 Y가 있을 때, X가 Y보다 수열에서 많이 등장하는 경우에는 X가 Y보다 앞에 있어야 한다. 만약, 등장하는 횟수가 같다면, 먼저 나온 것이 앞에 있어야 한다.

# 이렇게 정렬하는 방법을 빈도 정렬이라고 한다.

# 수열이 주어졌을 때, 빈도 정렬을 하는 프로그램을 작성하시오.

N, C = map(int, input().split())
lst = list(map(int, input().split()))

cnt = {}
for i in lst:
    if i not in cnt:
        cnt[i] = 0
    cnt[i] += 1
cnt.sort(cnt.items(), key=lambda x:x[1], reversed=True)

for key, value in cnt:
    for i in range(value):
        print(str(key), end = " ")