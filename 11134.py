# 철수는 쿠키를 세상에서 제일 좋아한다. 쿠키가 있는 곳이라면 철수도 반드시 있다고 할 정도이다. 철수는 날마다 자신이 가지고 있는 쿠키 중 C개를 먹는다. C개 미만의 쿠키가 남아 있다면 전부 먹는다. 철수가 쿠키 N개를 가지고 있으면 며칠 동안 먹을 수 있는지 구하시오.

T = int(input())

for i in range(T):
    N, C = map(int, input().split())
    
    day = N // C
    if N % C == 0:
        print(day)
    else:
        print(day+1)