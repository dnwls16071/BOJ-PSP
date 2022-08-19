# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
#
# 명령은 총 여섯 가지이다.
#
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

if __name__ == "__main__":
    from collections import deque
    import sys
    N = int(sys.stdin.readline())
    lst = deque()
    for _ in range(N):
        command = sys.stdin.readline().split()
        if command[0] == "push":
            lst.append(command[1])  # 정수 X를 큐에 넣는 연산
        elif command[0] == "pop":
            if not lst:     # 큐에 들어있는 정수가 없는 경우
                print(-1)
            else:           # 큐에 들어있는 정수가 있는 경우
                print(lst.popleft())  # 큐에서 가장 앞에 있는 정수를 빼고 그 수를 출력
        elif command[0] == "size":
            print(len(lst)) # 큐에 들어있는 정수의 개수
        elif command[0] == "empty":
            if not lst:
                print(1)    # 큐가 비어있으면
            else:
                print(0)    # 큐가 채워져있으면
        elif command[0] == "front":
            if not lst:   # 큐에 들어있는 정수가 없는 경우
                print(-1)
            else:           # 큐에 들어있는 정수가 있는 경우
                print(lst[0])
        elif command[0] == "back":
            if not lst:   # 큐에 들어있는 정수가 없는 경우
                print(-1)
            else:
                print(lst[-1])

# 이 문제는 자료구조 중에서 deque(데크)에 관한 문제이다.
# 문제 내용 중에서 가장 앞에 있는 정수를 뺄 때 pop(0)을 사용한 경우와 popleft()를 사용한 경우의 수행 속도는 차이가 있다.
# pop(0)보다 popleft()를 사용하는것이 적절하다.