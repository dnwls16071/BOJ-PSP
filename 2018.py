# 어떠한 자연수 N은, 몇 개의 연속된 자연수의 합으로 나타낼 수 있다. 당신은 어떤 자연수 N(1 ≤ N ≤ 10,000,000)에 대해서, 이 N을 몇 개의 연속된 자연수의 합으로 나타내는 가지수를 알고 싶어한다. 이때, 사용하는 자연수는 N이하여야 한다.

# 예를 들어, 15를 나타내는 방법은 15, 7+8, 4+5+6, 1+2+3+4+5의 4가지가 있다. 반면에 10을 나타내는 방법은 10, 1+2+3+4의 2가지가 있다.

# N을 입력받아 가지수를 출력하는 프로그램을 작성하시오

# 1차(메모리 초과)
# N = int(input())
# lst = [i for i in range(1, N+1)]

# cnt = 0
# start = 0
# end = 1
# for i in range(N//2):
#     if sum(lst[start:end]) == N:
#        cnt += 1
#     elif sum(lst[start:end]) > N:
#         start += 1
#     else:
#         end += 1
# print(cnt+1)

# 2차
# N = int(input())
# cnt = 0 # 만약에 합의 값이 N이랑 동일하게 나온다면 카운팅되는 변수
# start = 0 # 시작값
# end = 1 # 끝값
# sum_numbers = 1 # 합값
# while start <= N//2 + 1:
#     if sum_numbers < N:
#         end += 1
#         sum_numbers += end
#     elif sum_numbers == N :
#         cnt += 1
#         end += 1
#         sum_numbers += end
#         sum_numbers -= start
#         start += 1
#     else:
#         sum_numbers -= start
#         start += 1
# print(cnt+1)

# 3차
N = int(input())
cnt = 0
start = 0
end = 1
total = 1
while end <= N and start <= end:    # 끝값이 15보다 작거나 같고 시작값이 끝값보다 작거나 같은 경우
    if total == N:  # 총 누적값 합이 N과 같다면
        end += 1    # 끝값 1 증가
        total = total - start + end #
        start += 1
        cnt += 1
    elif total > N:
        total -= start
        start += 1
    else:
        end += 1
        total += end
print(cnt)