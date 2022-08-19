# 1부터 N까지의 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻을 수 있다.
#
# 1234567891011121314151617181920212223...

N, k = map(int, input().split())
ans = ""
for i in range(1, N+1):
    ans += str(i)

if len(ans) < k:
    print(-1)
else:
    print(ans[k-1])