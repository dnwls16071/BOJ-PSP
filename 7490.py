# 1부터 N까지의 수를 오름차순으로 쓴 수열 1 2 3 ... N을 생각하자.
#
# 그리고 '+'나 '-', 또는 ' '(공백)을 숫자 사이에 삽입하자(+는 더하기, -는 빼기, 공백은 숫자를 이어 붙이는 것을 뜻한다). 이렇게 만든 수식의 값을 계산하고 그 결과가 0이 될 수 있는지를 살피자.
#
# N이 주어졌을 때 수식의 결과가 0이 되는 모든 수식을 찾는 프로그램을 작성하라.

T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(i for i in range(1, N+1))
    