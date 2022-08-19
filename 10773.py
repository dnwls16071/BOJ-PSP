# 나코더 기장 재민이는 동아리 회식을 준비하기 위해서 장부를 관리하는 중이다.

# 재현이는 재민이를 도와서 돈을 관리하는 중인데, 애석하게도 항상 정신없는 재현이는 돈을 실수로 잘못 부르는 사고를 치기 일쑤였다.

# 재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.

# 재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 재민이를 도와주자!

# 시간이 오래 걸렸던 1차 작성 코드
K = int(input())

lst = []
for _ in range(K):
    num = int(input())
    if num == 0:
        lst.pop()
    else:
        lst.append(num)
print(sum(lst))

# 다른 방법을 사용한 2차 작성 코드
import sys

K = int(input())

lst = []
for _ in range(K):
    num = int(sys.stdin.readline())
    if num == 0:
        lst.pop()
    else:
        lst.append(num)
print(sum(lst))