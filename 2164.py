# N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

# 이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

# 예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.

# N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

# 1차 작성한 코드(TypeError 출력)
N = int(input())
lst = [i for i in range(1, N+1)]

while len(N) != 1:
    lst.remove(lst[0])
    lst.append(lst[0])
    lst.pop(lst[0])
print(*lst)

# 2차 작성한 코드(덱 활용 코드)
from collections import deque
s = deque()
N = int(input())
for i in range(1, N+1):
    s.append(i)

while len(s) != 1:
    s.popleft() # 처음 숫자는 버리고
    move_num = s.popleft() # 그 다음 숫자는 맨 뒤에 추가하기 위해 변수를 지정
    s.append(move_num)  # 변수를 삽입
print(*s)   # 리스트형 타입을 풀기 위한 방법