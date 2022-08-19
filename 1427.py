# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

N = str(input())

lst = []
for i in N:
    lst.append(int(i))

# sort() 안에 reverse=True를 넣으면 내림차순 정렬을 하게 된다.
lst.sort(reverse=True)  #sort() 오름차순 정렬(디폴트 값)

for i in lst:
    print(i, end = "")