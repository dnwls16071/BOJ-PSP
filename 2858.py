# 상근이는 기숙사 생활을 한다. 상근이의 방의 크기는 L×W 이다.

# 수업시간에 타일 채우기 경우의 수를 계산하던 상근이는 자신의 방도 1×1크기 타일로 채우려고 한다. 이때, 가장자리는 빨간색으로, 나머지는 갈색으로 채우려고 한다.

# 아래 그림은 상근이의 방의 크기가 4×3일 때 이다.

# 어느 날 상근이네 방에 하근이가 놀러왔다. 하근이는 아름다운 타일 배치에 감동받았다. 다시 방으로 돌아온 하근이는 빨간색과 갈색 타일의 개수는 기억했지만, 방의 크기는 기억해내지 못했다.

# 빨간색과 갈색 타일의 개수가 주어졌을 때, 상근이 방의 크기를 구하는 프로그램을 작성하시오.

R, B = map(int, input().split())
size = R + B

for i in range(3, int(size**0.5)+1):
    if (i-2) * (size // i - 2) == B:
        if i >= size // i:
            L = i
            W = size // i
            break
        else:
            L = size // i
            W = i
            break
print(L, W)

# 갈색 타일의 개수가 1개일때 경우를 가정해서 생각해보자.
# 그렇다면 세로의 길이는 최소 3이어야한다. 가운데 갈색 타일이 1개 들어가있고 양쪽 끝에 빨간색 타일이 1개씩 들어가 최소 3개가 되기 때문이다.
# 그렇다면 세로의 길이에서 2를 뺀 값과 가로(전체 사이즈를 세로의 길이로 나눈 값)의 길이에서 2를 뺀 값을 곱하면 가운데에 위치한 갈색 타일의 개수가 나와야한다.
