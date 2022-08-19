# N개의 실수가 있을 때, 한 개 이상의 연속된 수들의 곱이 최대가 되는 부분을 찾아, 그 곱을 출력하는 프로그램을 작성하시오. 예를 들어 아래와 같이 8개의 양의 실수가 주어진다면,

N = int(input())
lst = []
for _ in range(N):
    lst.append(float(input()))

for i in range(1, N):
    lst[i] = max(lst[i-1]*lst[i], lst[i])
print("{:.3f}".format(max(lst)))

# 다이나믹 프로그래밍(동적계획법)에 대해서 잘 알 수 있었다.
# 브루트포스로 접근하는 방식보다도 확실히 시간적인 측면에서 차이가 많이 난다.
# ex_input. 1.1 ,0.7, 1.3, 0.9, 1.4, 0.8, 0.7, 1.4
# ex_output. 1.1, 0.77, 1.3, 1.17, 1.638, 0.8, 0.7, 1.4
# lst[1]은 lst[0]~lst[1]을 곱한 값, lst[3]은 lst[2]~lst[3]을 곱한 값, lst[4]는 lst[2]~lst[4]를 곱한 값인데 이 때 lst[4]가 가장 큰 최댓값이 된다.