# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 1차 작성한 코드(시간 초과)
# import sys

# N = int(sys.stdin.readline())
# N_lst = list(map(int, sys.stdin.readline().split()))

# M = int(sys.stdin.readline())
# M_lst = list(map(int, sys.stdin.readline().split()))

# for i in range(len(M_lst)):
#     if M_lst[i] in N_lst:
#         print(1)
#     else:
#         print(0)

# 2차 작성한 코드(이진 탐색을 활용해서 푼 코드)
n = int(input())    # 첫째 줄에 자연수 n이 주어진다
# 이진 탐색을 사용하기 위해서 n_arr을 정렬된 상태로 입력한다.
n_arr = sorted(map(int, input().split()))   # n개의 정수가 주어진다.

m = int(input())    # 다음 줄에 자연수 m이 주어진다.
m_arr = list(map(int, input().split())) # m개의 정수가 주어진다.

# 이진 탐색을 수행하는 함수를 정의한다.(인자로는 배열, 찾는값, 시작값, 끝값)
def binary_search(array, target, start, end):
    # 시작값이 끝값보다 작다면 계속 실행
    while start <= end:
        # 중간값은 시작값과 끝값을 더한 값을 2로 나누면 된다.
        mid = (start + end) // 2
        # 만약 중간값이 찾는값과 같다면?
        if array[mid] == target:
            return mid  # 중간값을 리턴
        # 만약 찾는값이 중간값보다 왼쪽에 위치한다면?
        elif array[mid] > target:
            end = mid - 1   # 중간값의 오른쪽 부분은 버리므로 끝값을 mid - 1로 재설정한다.
        # 만약 찾는값이 중간값보다 오른쪽에 위치한다면?
        else:
            start = mid + 1 # 중간값으 왼쪽 부분은 버리므로 시작값을 mid + 1로 재설정한다.
    return None     # 만약 없다면 None을 리턴한다.

for i in m_arr: # m_arr의 요소를 하나하나 받아온다.
    result = binary_search(n_arr, i, 0, n-1)    # result 변수에 이진 탐색 함수 구문을 넣는다.
    # 만약 result가 None이 아니라면?
    if result != None:
        print(1)    # 있다는 것이므로 1을 출력
    # 만약 result가 None이 맞다면?
    else:   
        print(0)    # 없다는 것이므로 0을 출력