# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.
# tip) 변수를 만드는 위치가 전역인지 아님 지역인지에 따라서 결과값이 달라진다.

M = int(input())
N = int(input())

sosu_list = []
for i in range(M, N+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
           count += 1
           if count > 2:
               break
    if count == 2:
        sosu_list.append(i)
if len(sosu_list) != 0:
    print(sum(sosu_list))
    print(min(sosu_list))
else:
    print('-1')