# 아래 그림처럼 높이만 다르고 (같은 높이의 막대기가 있을 수 있음) 모양이 같은 막대기를 일렬로 세운 후, 왼쪽부터 차례로 번호를 붙인다. 각 막대기의 높이는 그림에서 보인 것처럼 순서대로 6, 9, 7, 6, 4, 6 이다. 일렬로 세워진 막대기를 오른쪽에서 보면 보이는 막대기가 있고 보이지 않는 막대기가 있다. 즉, 지금 보이는 막대기보다 뒤에 있고 높이가 높은 것이 보이게 된다. 예를 들어, 그림과 같은 경우엔 3개(6번, 3번, 2번)의 막대기가 보인다.

# N개의 막대기에 대한 높이 정보가 주어질 때, 오른쪽에서 보아서 몇 개가 보이는지를 알아내는 프로그램을 작성하려고 한다.

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N = int(input())
    stack = []
    for _ in range(N):
        stack.append(int(input()))

    standard_height = stack[-1]
    cnt = 1
    for i in range(N-1, -1, -1):
        if stack[i] > standard_height:
            standard_height = stack[i]
            cnt += 1
    print(cnt)

# sys 라이브러리 사용 >> 시간초과 방지
# 오른쪽에서 보았을때 첫 번째 막대기보다 높은 막대기가 가장 높은 막대기 뒤에 있는 경우 카운팅되지않는것을 생각해야한다.