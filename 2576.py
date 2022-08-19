# 7개의 자연수가 주어질 때, 이들 중 홀수인 자연수들을 모두 골라 그 합을 구하고, 고른 홀수들 중 최솟값을 찾는 프로그램을 작성하시오.

# 예를 들어, 7개의 자연수 12, 77, 38, 41, 53, 92, 85가 주어지면 이들 중 홀수는 77, 41, 53, 85이므로 그 합은
# 77 + 41 + 53 + 85 = 256이 되고, 41 < 53 < 77 < 85이므로 홀수들 중 최솟값은 41이 된다.

#1차 작성 코드
# lst = list(map(int, input()))
# result = []

# sum = 0
# for i in lst:
#     if i % 2 != 0:
#         result.append(i)
#         sum += i
#     print(sum)
#     print(min(result))
    
# for i in range(7):
#     if lst[i] % 2 != 0:
#         print(-1)

#2차 작성 코드

lst = []
for _ in range(7):
    num = int(input())
    if num % 2 != 0:
        lst.append(num)

if lst == []:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))