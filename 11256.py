T = int(input())

for _ in range(T):
    J, N = map(int, input().split())
    tmp = []
    for _ in range(N):
        R, C = map(int, input().split())
        tmp.append(R * C)

    tmp.sort(reverse=True)
    BOX_cnt = 0
    for i in tmp:
        if J - i > 0:
            J -= i
            BOX_cnt += 1
        else:
            BOX_cnt += 1
            break
    
    print(BOX_cnt)