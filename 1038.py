# 음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다. 예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. N번째 감소하는 수를 출력하는 프로그램을 작성하시오. 0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.

# 첫 번째 풀이(배열의 길이 이용)
from itertools import combinations
N = int(input())
arr = []
for i in range(1, 11):  # 조합의 원소 개수는 1~9개까지 나온다.
    for comb in combinations(range(0, 10), i):  # 원소값의 범위는 0~9까지다.
        comb = list(comb)
        comb.sort(reverse=True)
        arr.append(int(''.join(map(str, comb))))
arr.sort()

if len(arr) < N+1:  # 만약 배열의 길이가 구하고자 하는 값보다 짧아서 구할 수 없다면?
    print(-1)   # -1을 출력한다
else:   # 그렇지않다면?
    print(arr[N])   # N번째 원소 값을 출력한다.

# 두 번째 풀이(예외처리 사용)
from itertools import combinations
N = int(input())
arr = []
for i in range(1, 11):
    for comb in combinations(range(0, 10), i):
        comb = list(comb)
        comb.sort(reverse=True)
        arr.append(int(''.join(map(str, comb))))
arr.sort()

try:    # 가능하다면
    print(arr[N])   # N번째 원소 값을 출력한다,
except: # 불가능하다면
    print(-1)   # -1을 출력한다.

# 예외처리 문법을 공부할 수 있었던 문제였다.
# 조합을 활용해서 범위를 설정하는 방법을 좀 더 숙달시켜서 응용할 수 있어야겠다.

