# 상근이와 지수는 마트에서 오렌지 주스, 사과 주스, 파인애플 주스를 구매했다. 그들은 인터넷에서 찾은 방법으로 무알콜 칵테일을 만들어 학교에서 팔려고 한다. 하지만, 칵테일을 만드는 방법을 찾기 전에 주스를 구매했기 때문에, 주스가 남을 수도 있다.

# 무알콜 칵테일을 만드는데 필요한 오렌지, 사과, 파인애플 주스의 비율과 구매한 주스의 양이 주어진다. 칵테일을 최대한 많이 만들었을 때, 각 주스가 얼만큼 남는지 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())
I, J, K = map(int, input().split())
min_n = min(A / I, B / J, C / K)
print(A - I*min_n, B - J*min_n, C - K*min_n)