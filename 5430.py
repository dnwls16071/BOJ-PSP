# 선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.
#
# 함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, D는 첫 번째 수를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.
#
# 함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 수를 버리는 함수이다.
#
# 배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.

import sys
from collections import deque

T = int(input())
for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    if '' in arr:
        arr.pop()

    error_cnt = 0
    reverse_cnt = 0
    for i in p:
        if i == "R":    # 만약 (R) => 뒤집기의 경우
            reverse_cnt += 1
        else:   # 만약 (D) => 버리기의 경우
            if arr:
                if reverse_cnt % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                error_cnt = 1
                break

    if error_cnt == 1:
        print("error")
    else:
        if reverse_cnt % 2 == 0:
            print("[" + ','.join(arr) + "]")
        else:
            arr.reverse()
            print("[" + ','.join(arr) + "]")

# 처음에 시간초과가 나왔는데 그 이유를 구글링을 통해서 찾아봤다
# 길이가 길 경우 매번 reverse()를 돌리면 연산시간이 길어져 시간초과가 발생하는것이었다.
# 한 가지 특이한 점을 발견했는데 아무것도 입력하지 않았을때 즉, 리스트에 원소가 없는 경우를 len(arr) == 0 으로 놔뒀는데 그 코드가 잘못된 코드임을 알게되었다.
# ","을 기준으로 입력을 받는 것인데 아무것도 입력을 하지 않게 된다면 arr에 ''(공백)가 삽입되어 WA를 받았다는 사실을 뒤늦게 알게되었다.
# 뒤집기를 짝수번을 시도하면 원래 상태와 동일하고 홀수번 시도하면 한 번만 뒤집으면 된다.

# 파싱이란??
# 입력값으로 정수, 콤마, 공백, 세미콜론 등이 입력될때 컴마는 없애고 공백은 무시하는 등 정수값만 가져올때 사용하는 방법
