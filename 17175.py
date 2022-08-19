# 혁진이는 알고리즘 문제를 만들라는 독촉을 받아 스트레스다. 하지만 피보나치 문제는 너무 많이 봐서 지겹기 그지없다. 그러나 문제를 만들 시간이 없는 혁진이는 피보나치 문제를 응용해서 문제를 만들려 한다.
#
# int fibonacci(int n) { // 호출
#   if (n < 2) {
#     return n;
#   }
#   return fibonacci(n-2) + fibonacci(n-1);
# }
# 위와 같이 코딩하였을 때 fibonacci(n)를 입력했을 때에 fibonacci 함수가 호출되는 횟수를 계산해보자.

fibonacci = [1, 1]
n = int(input())
if n < 2:
    print(1)
else:
    a, b = 1, 1
    for _ in range(n-1):
        a, b = a + b + 1, a
    print(a % 1000000007)

# 다이나믹 프로그래밍을 이용한 피보나치 수열 문제였다.