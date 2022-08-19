# 영훈이는 태형이에게 어떤 수 N과 K를 주었다.

# 태형이는 N을 종이에 쓰기 시작했다. 태형이는 자신이 이 수를 몇 번 써야 그 수가 K로 나누어지는지 궁금해지기 시작했다.

# N=10일 때, 이 수를 한 번 쓰면 10이고, 두 번 쓰면 1010이고, 세 번쓰면 101010이고,... 이런식이다.

# 어떤 수 N과 K가 주어졌을 때, N을 몇 번 써야 K로 나누어 떨어지는지 구하는 프로그램을 작성하시오.

N, K = map(int, input().split())
N = str(N)

result = []
while True:
    for i in range(1, 100):
        temp = int(N*i) % K
        if temp == 0:
            result.append(i)
        else:
            print(-1)

print(min(result))