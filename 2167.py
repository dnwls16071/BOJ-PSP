# 2차원 배열이 주어졌을 때 (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합을 구하는 프로그램을 작성하시오. 배열의 (i, j) 위치는 i행 j열을 나타낸다.

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N, M = map(int, sys.stdin.readline().split())
    lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    K = int(sys.stdin.readline())
    for _ in range(K):
        res = 0
        b = list(map(int, sys.stdin.readline().split()))
        i, j, x, y = map(int, b)
    
        for a in range(i, x+1):
            for b in range(j, y+1):
                res += lst[a-1][b-1]
        print(res)


