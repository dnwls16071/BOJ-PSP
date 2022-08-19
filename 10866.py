# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여덟 가지이다.

# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# tip) deque의 자료구조 형태를 알아볼 수 있는 좋은 문제

import sys

from collections import deque
s = deque()
N = int(input())

for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push_front":
        s.appendleft(command[1])
    elif command[0] == "push_back":
        s.append(command[1])
    elif command[0] == "pop_front":
        if s:
            print(s[0])
            s.popleft()
        else:
            print("-1")
    elif command[0] == "pop_back":
        if s:
            print(s[len(s)-1])
            s.pop()
        else:
            print("-1")
    elif command[0] == "size":
        print(len(s))
    elif command[0] == "empty":
        if s:
            print("0")
        else:
            print("1")
    elif command[0] == "front":
        if s:
            print(s[0])
        else:
            print("-1")
    elif command[0] == "back":
        if s:
            print(s[len(s)-1])
        else:
            print("-1")