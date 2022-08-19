# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
#
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

from collections import Counter
import sys
input = sys.stdin.readline
N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))
lst.sort()

# 산술평균 코드
print(round(sum(lst)/N))

# 중앙값 코드
start = 0
end = len(lst)
mid = (start + end) // 2
print(lst[mid])

# 최빈값 코드
# 최빈값이 여러 개 있을 경우 최빈값 중 두 번째로 작은 값을 출력
cnt = Counter(lst).most_common(2)
if len(lst) > 1:    # 만약 들어있는 원소가 2개 이상이라면?
    if cnt[0][1] == cnt[1][1]:  # 만약 최빈값 빈도가 두 원소 다 같다면?
        print(cnt[1][0])    # 최빈값 중 두 번째 값 출력
    else:   # 만약 최빈값 빈도가 다르다면?
        print(cnt[0][0])    # 그대로 최빈값 출력
else:   # 만약 들어있는 원소가 1개뿐이라면 그 원소가 최빈값이 된다.
    print(cnt[0][0])

# 범위 코드
print(max(lst) - min(lst))

# 외관상 문제는 정말 쉬운 문제로 보였다. 왜 정답률이 21%인지 이해가 안갔다.
# 정답률이 잔인했던 이유는 문제 중에서 최빈값을 못 구하는 경우가 많아서였다고 한다.
# 최빈값 코드를 작성하면서 Counter 라이브러리에 대해서 알게 되었다.

# from collections import Counter
# Counter 클래스는 작업을 좀 더 쉽게 처리하도록 하기 위해서 데이터의 개수가 많은 순서대로 정렬된 배열을 리턴하는 most_common 이라는 메서드도 사용가능하다.

from collections import Counter
Counter("hello world").most_common()
# [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]

from collections import Counter
Counter("hello world").most_common(1)
# [('l', 3)]