# A보다 크거나 같고 B보다 작거나 같은 모든 수를 종이에 썼을 때, 각 숫자를 몇 번씩 쓰게 되는지 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

arr = [0] * 10
while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    for i in range(A, B+1):
        i = str(i)
        if len(i) == 1:
            arr[int(i)] += 1
        else:
            for j in range(0, len(i)):
                arr[int(i[j])] += 1
                
    for k in arr:
        print(k, end = " ")
    print()
    arr = [0] * 10