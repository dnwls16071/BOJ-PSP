# 백준 온라인 저지의 송년대회 Good Bye BOJ, 2021!의 개최일은 2021년 12월 31일이다. 원이는 대회가 개최된다는 사실이 기뻐 제목을 뚫어져라 보다가 2021이 무언가 특별하다는 사실을 깨달았다.
#
# 그렇다. 2021은 연속한 두 소수 43과 47의 곱이다. 다음에 이런년도가 오려면 무려 470년 뒤인 2491년이 되어야 한다. 원이는 어떤 수가 연속한 두 소수의 곱으로 이루어져 있으면 특별한 수라 부르기로 하였다.
#
# 주어진 수보다 큰 특별한 수 중 가장 작은 수를 구하는 프로그램을 작성하시오.

N = int(input())
arr = [1] * 104
prime_number = []
for i in range(2, 104):
    if arr[i] == 1:
        prime_number.append(i)
        for j in range(2*i, 104, i):
            arr[j] = 0

special_number = []
for i in range(1, len(prime_number)):
    special_number.append(prime_number[i] * prime_number[i-1])

for i in special_number:
    if i > N:
        print(i)
        break


# 우선 소수를 판별해야하므로 에라토스테네스의 체를 이용하여 소수를 저장하는 리스트를 만들었다.
# 소수 리스트에서 연속된 소수의 곱의 결과를 특별한 수 리스트에 저장하였다.
# 특별한 수 리스트에서 값을 받아올 때 N보다 큰 값이 바로 나타나면 break를 통해 탈출하고 N보다 큰 최초의 특별한 수를 출력한다.
# N의 범위는 1보다 크거나 같으며 10000보다 작거나 같은 수이기 때문에 연속한 소수의 곱을 이루는 가장 큰 수는 101*103 = 10403이다.

N = int(input())
arr = [True] * 104
special_number = []
prime_number = []
for i in range(2, 104):
    if arr[i] == True:
        prime_number.append(i)
        for j in range(2*i, 104, i):
            arr[j] = False

for i in range(1, len(prime_number)):
    special_number.append(prime_number[i] * prime_number[i-1])

for i in special_number:
    if i > N:
        print(i)
        break