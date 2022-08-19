# 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

N, S = map(int, input().split())
lst = list(map(int, input().split()))

ans = 100001
p1 = p2 = 0
total = lst[0]

while True:
    if total >= S:
        total -= lst[p1]
        ans = min(ans, p2-p1+1)
        p1 += 1
    else:
        p2 += 1
        if p2 == N:
            break
        total += lst[p2]

if ans == 100001:   # 만약 ans가 그대로 나온다면? => 이것보다 작은 값이 나오지 않는다는 소리이므로
    print(0)
else:
    print(ans)

# 부분합 문제는 투포인터로 접근하면 될 것 같다.
# 투포인터 이용 방법은 두 가지가 있다.
# 첫째, start = 0, end = len(lst)와 같은 방식으로 포인터 초기값을 지정한다.
# 둘째, start = end = 0과 같은 방식으로 조건별로 start, end 값을 +1씩 증가하거나 -1씩 감소한다.

