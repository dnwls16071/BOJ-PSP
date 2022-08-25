# 세준이는 도서관에서 일한다. 도서관의 개방시간이 끝나서 세준이는 사람들이 마구 놓은 책을 다시 가져다 놓아야 한다. 세준이는 현재 0에 있고, 사람들이 마구 놓은 책도 전부 0에 있다. 각 책들의 원래 위치가 주어질 때, 책을 모두 제자리에 놔둘 때 드는 최소 걸음 수를 계산하는 프로그램을 작성하시오. 세준이는 한 걸음에 좌표 1칸씩 가며, 책의 원래 위치는 정수 좌표이다. 책을 모두 제자리에 놔둔 후에는 다시 0으로 돌아올 필요는 없다. 그리고 세준이는 한 번에 최대 M권의 책을 들 수 있다.

# Code1
N, K = map(int, input().split())
number = list(input())

tmp = K
stack = []
for i in range(N):
    while tmp > 0 and stack:
        if stack[-1] < number[i]:
            stack.pop()
            tmp -= 1
        else: 
            break
    stack.append(number[i])
print(''.join(stack[:N-K]))

# Code2
N, K = map(int, input().split())
number = list(input())

stack = []
for i in range(N):
    while K > 0 and stack:
        if stack[-1] < number[i]:
            stack.pop()
            K -= 1
        else:
            break
    stack.append(number[i])
print(''.join(stack[:N-K]))

# Code1과 Code2의 차이점을 알아내고자 코드를 순차적으로 봤는데 어디가 틀렸는지 알게되었다.
# tmp변수를 사용하지않고 K가 0이 될때까지 반복문을 돌린 코드
# tmp변수를 사용하고 K가 0이 될때까지 반복문을 돌린 코드

# 4 2
# 9421
# 위 테스트케이스의 경우 출력되는 값은 94여야한다.

# 만약 Code1 방식대로 코드를 작성하면 답은 stack[:4-2]가 된다.
# 그런데 Code2 방식대로 코드를 작성하면 답은 stack[:4-0]이 된다.
# 위의 경우처럼 자세히 따져보았을때 슬라이싱의 범위가 완전히 다르게 나온다.

# 따라서 변수를 사용해서 스택 슬라이싱을 진행해야한다.
