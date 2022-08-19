# N개의 정수가 주어진다. 이때, N개의 정수를 오름차순으로 정렬하는 프로그램을 작성하시오. 같은 정수는 한 번만 출력한다.

# 1차 작성한 코드
N = int(input())
num_list = list(map(int, input().split()))
num_list = list(set(num_list))  # 1차적으로 집합형으로 변환하여 중복을 방지하고 다시 리스트형으로 변환
num_list.sort() # 리스트형이므로 sort()함수를 사용하여 오름차순 정렬함

for i in num_list:
    print(i, end = " ")

# 2차 작성한 코드
N = int(input())
number_list = list(map(int, input().split()))

for i in sorted(list(set(number_list))): #set으로 중복 방지, sorted로 정렬
    print(i, end = ' ')