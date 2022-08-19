# 상근이는 등차수열을 이루는 정수 4개를 골랐다. 이것은 상근이가 고른 수 4개를 정렬했을 때, 인접한 쌍의 차이가 일정하다는 것을 의미한다. 그 다음 이렇게 고른 수 4개를 노래로 만들어서 외우고 다닌다.

# 어느 날, 상근이는 자신이 고른 4개 수 중 1개를 까먹었다. 상근이가 기억하고 있는 수 세 개가 주어졌을 때, 까먹은 수를 구하는 프로그램을 작성하시오.

lst = list(map(int, input().split()))
lst.sort()

if lst[1] - lst[0] == lst[2] - lst[1]:
    print(lst[2] + (lst[2] - lst[1]))
elif lst[1] - lst[0] < lst[2] - lst[1]:
    print(lst[1] + (lst[1] - lst[0]))
elif lst[1] - lst[0] > lst[2] - lst[1]:
    print(lst[1] - (lst[2] - lst[1]))
